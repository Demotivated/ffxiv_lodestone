import logging


class ParsingException(Exception):

    def __init__(self, message, **kwargs):
        super(ParsingException, self).__init__(message, **kwargs)
        self.message = message
        logging.error(message)
