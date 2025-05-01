'''Decorators here.'''
import logging

from .settings import LOG_MESSAGES_INFO


def info_log(func):
    '''Decorator for
    accept_requests(),
    get_server_object(),
    client_request_handler(),
    server_bind().'''
    def wrapped(*args):
        func_name = func.__name__
        logging.info(
            LOG_MESSAGES_INFO[func_name][0],
            args
        )
        result = func(*args)
        logging.info(
            LOG_MESSAGES_INFO[func_name][1],
            args
        )
        return result
    return wrapped
