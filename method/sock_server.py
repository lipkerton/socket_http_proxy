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
    client_address: tuple[str, int]
) -> None:
    '''Han dle client's request.'''
    request = b''  # save first chunk.
    while True:
        # здесь блокирующая функция остановит
        # работу потока и будет ждать данных,
        # тогда управление перейдет на другой поток,
        # который уже, возможно, данных дождался.
        chunk = client.recv(1024)
        if not chunk:
            break
        request += chunk  # make one message.
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
