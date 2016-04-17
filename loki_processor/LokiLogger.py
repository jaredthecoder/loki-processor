# -*- coding: utf-8 -*-

""" LokiLogger.py

Logger class for Loki
"""


# Python standard library assets
import logging
import logging.handlers


__author__ = 'Jared M Smith'
__license__ = 'MIT'
__version__ = '0.1.0'
__maintainer__ = 'Jared M Smith'
__email__ = 'jared@jaredsmith.io'


class LokiLogger:

    def setup(self, logfile_name):
        self.__logger = logging.getLogger('LokiLogger')
        self.__logfile_name = logfile_name
        self.__setup_logger()

    def log(self, message, level='INFO'):
        if level == 'INFO':
            self.__logger.info(message)
        elif level == 'DEBUG':
            self.__logger.debug(message)
        elif level == 'WARNING':
            self.__logger.warning(message)
        elif level == 'ERROR':
            self.__logger.error(message)

    def __setup_logger(self):
        self.__logger.setLevel(logging.DEBUG)
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        stream_handler.setFormatter(formatter)
        self.__logger.addHandler(stream_handler)
        rotating_file_handler = logging.handlers.RotatingFileHandler(
            self.__logfile_name,
            maxBytes=20000000, backupCount=5)
        self.__logger.addHandler(rotating_file_handler)
