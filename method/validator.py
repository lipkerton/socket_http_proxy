'''Validators of the program.'''
import ipaddress
import logging
import socket


def validate_ip_address(
    address: str
) -> bool:
    '''Check is IP valid.'''
    try:
        ipaddress.ip_address(address)
    except ValueError:
        logging.error(
            'IP address is not valid: %s',
            ValueError
        )
        return False
    return True


def validate_port(
    address_port: tuple[str, int]
) -> bool:
    '''Check port is open and valid.'''
    with socket.socket() as sock:
        # connect_ex returns 0 if connect is successful.
        # overwise the error wiil be arised.
        check_port = sock.connect_ex(address_port)
        if not check_port:
            logging.error(
                'Port is not valid (or it is already in use): %s',
                ValueError
            )
            return False
        return True
