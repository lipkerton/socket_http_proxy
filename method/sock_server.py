'''Socket-server class in here.'''
import logging
import email

from gevent import socket
import gevent

from method.decorator import info_log
from method.settings import CLIENT_REQUESTS_COUNTER


@info_log
def connect_to_the_destination_point(
    request_data: dict[str, bytes],
    request: bytes
):
    '''Sending client request to the destination point.'''
    host, port = request_data['Host']

    destination_connection = socket.socket()
    # использую connect вместо bind - bind ожидает локальный интерфейс,
    # а connect подключается по имени хоста.
    destination_connection.connect((host, int(port)))
    destination_connection.sendall(request)

    response = b''

    while True:
        chunk = destination_connection.recv(1024)
        if not chunk:
            break
        response += chunk

    destination_connection.close()
    return response


@info_log
def form_request_data(chunk: bytes):
    '''Split chunk in parts,
    form dictionary with request info.'''
    headers, _, _ = chunk.partition(b'\r\n\r\n')
    method, header_parts = headers.split(b'\r\n', 1)
    method, destination, protocol = method.split()

    request_data = {
        'Method': method,
        'Destination': destination,
        'Protocol': protocol
    }
    # получаем словарь из заголовков пользовательского запроса
    # и добавляем его к request_data.
    request_data.update(email.message_from_bytes(header_parts))

    if ':' in request_data['Host']:
        request_data['Host'] = request_data['Host'].split(':')
    else:
        request_data['Host'] = [request_data['Host'], 80]

    logging.info('Request data formed: %s', request_data)
    return request_data



@info_log
def request_handler(
    client: socket.socket,
) -> bytes:
    '''Han dle client's request.'''
    while True:
        # здесь блокирующая функция остановит
        # работу потока и будет ждать данных,
        # тогда управление перейдет на другой поток,
        # который уже, возможно, данных дождался.
        chunk = client.recv(1024)
        if not chunk:
            break
        request_data = form_request_data(chunk)
        response = connect_to_the_destination_point(
            request_data,
            chunk
        )
        if response:
            client.sendall(response)
    client.close()
    return response



@info_log
def accept_requests(
    server_object: socket.socket
) -> None:
    '''Accept client requests.'''
    while True:
        client, _ = server_object.accept()
        gevent.spawn(request_handler, client)



@info_log
def get_server_object(
    server_address: tuple[str, int]
) -> socket.socket:
    '''Create socket object of server.'''
    server = socket.socket()
    server.bind(server_address)
    server.listen(CLIENT_REQUESTS_COUNTER)
    return server
