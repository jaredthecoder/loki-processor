# -*- coding: utf-8 -*-


""" LokiSubscriber.py
"""


__author__ = 'Jared M Smith'
__license__ = 'MIT'
__version__ = '0.1.0'
__maintainer__ = 'Jared M Smith'
__email__ = 'jared@jaredsmith.io'


# Python Standard Libraries
import pickle
import sys
import time

# 3rd Party Libraries
import redis

# Project Assets
from loki_processor.LokiDataObject import LokiDataObject


class LokiSubscriber:

    def __init__(self, channel):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.p = self.r.pubsub(ignore_subscribe_messages=True)
        self.channel = channel

    def setup(self):
        self.p.subscribe(**{str(self.channel): self.message_handler})

    def receive_messages(self):
        while True:
            result = self.p.get_message()
            if result:
                pass
            time.sleep(0.001)

    def convert_message(self, message):
        new_message = dict()
        for key, val in message.items():
            if key == 'data':
                new_message[key] = pickle.loads(val)
            elif key == 'channel':
                new_message[key] = val.decode('utf-8')
            elif key == 'pattern':
                if val is None:
                    continue
                else:
                    new_message[key] = val
            elif key == 'type':
                new_message[key] = val
        return new_message

    def message_handler(self, message):
        serialized_data = self.convert_message(message)
        loki_object = LokiDataObject(**serialized_data)
        print(loki_object.generic_attributes)
