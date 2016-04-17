# -*- coding: utf-8 -*-

""" decoders.py

Contains decoders for data ingested via the stream.
"""


import re

import requests

from loki_processor.foursquare_wrapper import FoursquareWrapper


__author__ = 'Jared M Smith'
__license__ = 'MIT'
__version__ = '0.1.0'
__maintainer__ = 'Jared M Smith'
__email__ = 'jared@jaredsmith.io'


fs_checkin_re = re.compile(".*I'm at.*(http.*\Z)")
fs_checkin_url_re = re.compile("https://.*/.*/(.*)")

whatifs_whatif_general_re = re.compile(".*What if.*", re.IGNORECASE)
whatifs_whatif_question_mark_re = re.compile(".*\?.*What if.*\?.*",
                                             re.IGNORECASE)
whatifs_how_re = re.compile(".*how.*", re.IGNORECASE)
whatifs_why_re = re.compile(".*why.*", re.IGNORECASE)
whatifs_when_re = re.compile(".*when.*", re.IGNORECASE)

fsw = FoursquareWrapper()


def twitter_swarm_decoder(data):
    payload = 'Not a swarm match'
    match = fs_checkin_re.match(data)
    if match is not None:
        twitter_url = match.group(1)
        swarm_url = requests.get(twitter_url).url
        fs_shortid = fs_checkin_url_re.match(swarm_url).group(1)
        checkin = fsw.resolve_checkin(fs_shortid)
    else:
        return payload


def twitter_whatifs_decoder(data):
    match = whatifs_whatif_general_re.match(data)
    if match is not None:
        return data
    else:
        return None
