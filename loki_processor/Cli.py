# -*- coding: utf-8 -*-

""" Cli.py

Command Line Interface for Loki Processor
"""


# Python standard library assets
import argparse
import textwrap
from argparse import RawTextHelpFormatter


__author__ = 'Jared M Smith'
__license__ = 'MIT'
__version__ = '0.1.0'
__maintainer__ = 'Jared M Smith'
__email__ = 'jared@jaredsmith.io'


class Cli:

    def __init__(self):
        self.__parser = self.__setup_argparser()
        self.args = self.__parser.parse_args()

    def __setup_argparser(self):
        parser = argparse.ArgumentParser(prog='loki',
                                         formatter_class=RawTextHelpFormatter,
                                         description=textwrap.dedent('''\
                                                    __        __    _
                                                   / /  ___  / /__ (_)
                                                  / /__/ _ \/  '_// /
                                                 /____/\___/_/\_\/_/
                                            ------------------------------------
                                            Processor Component
                                            Version: 0.1.0
                                            ------------------------------------
                                            '''),
                                         epilog=textwrap.dedent('''\
                                            Author: Jared M Smith
                                            Contact: jared@jaredsmith.io
                                            ''')
                                         )

        parser.add_argument('--redis-channel', dest='redis_channel', required=False,
                            type=str, default='loki01',
                            help=textwrap.dedent('''\
                                 The name of the redis channel to subscribe
                                 to.'''))
        parser.add_argument('--sql-db-path', dest='sql_db_path', required=False,
                            type=str,  default='/tmp/loki.db',
                            help=textwrap.dedent('''\
                                 Path to SQLite3 database to collect statistics
                                 and other data in.'''))
        parser.add_argument('--log', required=False, action='store_true',
                            dest='log', default=True,
                            help=textwrap.dedent('''\
                                Whether to enable logging.'''))
        parser.add_argument('--quiet', required=False, action='store_false',
                            dest='log', default=False,
                            help=textwrap.dedent('''\
                                Whether to silence logging.'''))
        parser.add_argument('--logfile', required=False,
                            dest='logfile', default='/tmp/lokilog.out', type=str,
                            help=textwrap.dedent('''\
                                If logging is enabled, log to
                                this filename.'''))
        return parser
