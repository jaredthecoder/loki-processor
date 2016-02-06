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
        self.parser = self.setup_argparser()
        self.args = self.parser.parse_args()

    def setup_argparser(self):
        parser = argparse.ArgumentParser(prog='loki',
                                         formatter_class=RawTextHelpFormatter,
                                         description=textwrap.dedent('''\
                                                    __        __    _
                                                   / /  ___  / /__ (_)
                                                  / /__/ _ \/  '_// /
                                                 /____/\___/_/\_\/_/
                                            ------------------------------------
                                            Processor Component
                                            Version: 0.0.1
                                            ------------------------------------
                                            '''),
                                         epilog=textwrap.dedent('''\
                                            Author: Jared M Smith
                                            Contact: jared@jaredsmith.io
                                            ''')
                                         )

        parser.add_argument('--log', required=False, type=bool,
                            choices=(True,False),
                            dest='log', default=True,
                            help=textwrap.dedent('''\
                                Whether to enable logging.
                                Defaults to True. Possible options are
                                (True, False).'''))
        parser.add_argument('--logfile', required=False,
                            dest='log_file', type=str,
                            help=textwrap.dedent('''\
                                If logging is enabled, log to
                                this file.'''))
        return parser
