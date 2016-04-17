# -*- coding: utf-8 -*-

""" foursquare_wrapper.py
"""


import requests


__author__ = 'Jared M Smith'
__license__ = 'MIT'
__version__ = '0.1.0'
__maintainer__ = 'Jared M Smith'
__email__ = 'jared@jaredsmith.io'


class FoursquareWrapper:

    def __init__(self):
        self.root = 'https://api.foursquare.com/v2'
        self.oauth_token = 'ZALMMBTUVGFMUJ5TOJ5SHLVQ1R2XQM3JBB12UAPOR24V45OI'
        self.v = '20160301'

    def decode_json(self, response):
        json_data = None
        try:
            json_data = response.json()
        except ValueError:
            print('Could not decode JSON in response.')
        return json_data

    def check_status(self, response):
        if not response.status_code == requests.codes.ok:
            print('Error recieved: {}'.format(response.status_code))
            return False
        return True

    def resolve_checkin(self, short_id):
        url = '{}/checkins/resolve'.format(self.root)
        params = {'oauth_token': self.oauth_token, 'v': self.v, 'shortId': short_id}
        response = requests.get(url, params=params)
        if self.check_status(response):
            data = self.decode_json(response)
            if data is not None:
                return data

    def get_checkin(self, checkin_id):
        url = '{}/checkins/CHECKIN_ID'.format(self.root)
        params = {'oauth_token': self.oauth_token, 'v': self.v, 'CHECKIN_ID': checkin_id}
        response = requests.get(url, params=params)
        if self.check_status(response):
            data = self.decode_json(response)
            if data is not None:
                return data
