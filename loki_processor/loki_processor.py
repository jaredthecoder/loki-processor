# -*- coding: utf-8 -*-

""" loki_processor.py

This file contains the main routine for the entire package.
Orchestrates the rest of the files.
"""


# Project assets
from loki_processor.Cli import Cli
from loki_processor.LokiSubscriber import LokiSubscriber


__author__ = 'Jared M Smith'
__license__ = 'MIT'
__version__ = '0.1.0'
__maintainer__ = 'Jared M Smith'
__email__ = 'jared@jaredsmith.io'



def main():
    cli = Cli()
    subscriber = LokiSubscriber('loki01')
    subscriber.setup()
    subscriber.receive_messages()
