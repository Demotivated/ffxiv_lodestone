import logging


class ParsingException(Exception):

    def __init__(self, message, exc_info=True):
        super(ParsingException, self).__init__(message, exc_info)
        self.message = message
        logging.error(message)
