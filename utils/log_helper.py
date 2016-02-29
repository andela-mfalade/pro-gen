"""Customize logging messages.

This module serves to customize the inbuild Python Logging Module.
"""

import logging


class CustomLogger():
    """Custom Logger class.

    Class to add custom behavior to the Logging Module.
    """

    format = '[%(levelname)s] %(asctime)s [ %(pathname)s:%(lineno)d ] ' + \
        '  - %(message)s'

    def __init__(self, option=None):
        """Init method.

        Args:
            option: The option specified when initializing the default
            logging module.
        Usage:
            Could be left blank. e.g: CustomLogger()
            Could be the name of the file running e.g: CustomLogger(__file__),
            Could be the name of the main filee.g:  CustomLogger(__main__)
        """
        self.logger = logging.getLogger(option)
        logging.basicConfig(
            format=self.format,
            level=logging.DEBUG,
            datefmt='%H:%M:%S'
        )

    def info(self, *args):
        """Info method.

        Binds the logging info method to CustomLogger
        """
        return self.logger.info(*args)

    def debug(self, *args):
        """Debug method.

        Binds the logging debug method to CustomLogger
        """
        return self.logger.debug(*args)

    def warn(self, *args):
        """Info method.

        Binds the logging info method to CustomLogger
        """
        return self.logger.warn(*args)

    def error(self, *args):
        """Error method.

        Binds the logging error method to CustomLogger
        """
        return self.logger.error(*args, exc_info=True)

    def critical(self, *args):
        """Critical method.

        Binds the logging critical method to CustomLogger
        """
        return self.logger.critical(*args)
