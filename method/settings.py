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
    'connect_to_the_destination_point': (
        'Sending client request to the destination point. Client request: %s',
        'Response formed on client request: %s'
    ),
    'request_handler': (
        'Request accepted. Client: %s!',
        'Request resolved: %s'
    ),
    'get_server_object': (
        'Making server object at address: %s...',
        'Server object was made at: %s!'
    ),
    'form_request_data': (
        'Recieved chunk with data: %s',
        'Chunk was resolved: %s'
    )
}
