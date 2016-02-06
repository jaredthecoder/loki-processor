# -*- coding: utf-8 -*-


""" LokiDataObject.py
"""


__author__ = 'Jared M Smith'
__license__ = 'MIT'
__version__ = '0.1.0'
__maintainer__ = 'Jared M Smith'
__email__ = 'jared@jaredsmith.io'


import json
import sys


class LokiDataObject(object):

    def __init__(self, **kwargs):
        self.source_attributes = json.loads(kwargs['data'])
        self.entity_attributes = dict()
        self.content_attributes = dict()
        self.location_attributes = dict()

        self.generic_attributes = self.map_source_attributes()

    def map_source_attributes(self):
        generic_attributes = dict()
        for key, val in self.source_attributes.items():
            if 'user' in key:
                self.entity_attributes[key] = val
            elif 'location' in key:
                self.location_attributes[key] = val
            else:
                self.content_attributes[key] = val

        generic_attributes['entity'] = self.entity_attributes
        generic_attributes['content'] = self.content_attributes
        generic_attributes['location'] = self.location_attributes

        return generic_attributes
