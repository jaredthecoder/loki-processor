# -*- coding: utf-8 -*-

""" loki_processor.py

This file contains the main routine for the entire package.
Orchestrates the rest of the files.
"""


# Project assets
from loki_processor.Cli import Cli
from loki_processor.LokiSubscriber import LokiSubscriber
from loki_processor.LokiLogger import LokiLogger


__author__ = 'Jared M Smith'
__license__ = 'MIT'
__version__ = '0.1.0'
__maintainer__ = 'Jared M Smith'
__email__ = 'jared@jaredsmith.io'


def start_subscriber(args, logger=None):
    subscriber = LokiSubscriber(args, logger)
    subscriber.setup()
    subscriber.receive_messages()


def main():
    logfile_name = None
    cli = Cli()
    if cli.args.log:
        try:
            logfile_name = cli.args.logfile
        except KeyError:
            raise ValueError(
                    'Logging is enabled by the logfile name is undefined.')
        finally:
            if logfile_name is None:
                raise ValueError(
                        'Logging is enabled by the logfile name is undefined.')
        logger = LokiLogger()
        logger.setup(logfile_name)
        start_subscriber(cli.args, logger)
    else:
        start_subscriber(cli.args)
