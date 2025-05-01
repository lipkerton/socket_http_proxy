'''Constants and settings of the programm.'''
# How many requests can server to listen at once.
CLIENT_REQUESTS_COUNTER = 10
# Format for logs.
FORMAT = '%(asctime)s %(message)s'
# logs messges.
LOG_MESSAGES_INFO = {
    'accept_requests': (
        'Accepting requests at: %s...',
        'Accepting finished at: %s.'
    ),
    'client_request_handler': (
        'Request accepted. Client: %s!',
        'Request resolved: %s'
    ),
    'get_server_object': (
        'Making server object at address: %s...',
        'Server object was made at: %s!'
    )
}
