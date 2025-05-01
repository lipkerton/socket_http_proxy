'''Socket-server class in here.'''
import logging
import select
import socket
import threading

from method.decorator import info_log
from method.settings import CLIENT_REQUESTS_COUNTER


@info_log
def client_request_handler(
    client: socket.socket,
    client_address: tuple[str, int]):
    '''Han dle client's request.'''
    request = b''  # save first chunk.
    client.setblocking(False)
    while True:
        try:
            # если я буду тупо считывать данные так
            # то в неблокирующем режиме socket
            # сразу выкинет мне ошибку, если данные
            # не придут мгновенно
            chunk = client.recv(1024)
            if not chunk:
                break
            request += chunk  # make one message.
        except BlockingIOError as message:
            logging.error(
                'The data is absent: %s',
                message
            )
            # поэтому нужно подождать данные.
            check_readiness, _, _ = select.select(
                [client], [], [], 0.5
            )
            if not check_readiness:
                continue
    print(request, client_address)


@info_log
def accept_requests(
    server_object: socket.socket
) -> None:
    '''Accept client requests.'''
    while True:
        client, client_address = server_object.accept()
        client_handler = threading.Thread(
            target=client_request_handler, args=(client, client_address)
        )
        client_handler.start()


@info_log
def get_server_object(
    server_address: tuple[str, int]
) -> socket.socket:
    '''Create socket object of server.'''
    server = socket.socket()
    server.bind(server_address)
    server.listen(CLIENT_REQUESTS_COUNTER)
    return server
