'''main doc'''
# pylint: disable=redefined-outer-name
import logging
import sys

from method.settings import FORMAT
from method.sock_server import accept_requests, get_server_object
from method.validator import validate_ip_address, validate_port

logger = logging.getLogger(__name__)


def main(server_address: tuple):
    '''main func.'''
    if (
        validate_ip_address(server_address[0])
        and validate_port(server_address)
    ):
        server = get_server_object(server_address)
        accept_requests(server)


if __name__ == "__main__":
    logging.basicConfig(
        filename='socket_log.log',
        level=logging.INFO,
        format=FORMAT
    )
    address, port = sys.argv[1:]
    port = int(port)
    main((address, port))
