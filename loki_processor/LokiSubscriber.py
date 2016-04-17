# -*- coding: utf-8 -*-


""" LokiSubscriber.py
"""


# Python Standard Libraries
import pickle
import time

# 3rd Party Libraries
import redis

# Project Assets
from loki_processor.LokiDataObject import LokiDataObject
# from loki_processor.decoders import twitter_swarm_decoder
from loki_processor.decoders import twitter_whatifs_decoder


__author__ = 'Jared M Smith'
__license__ = 'MIT'
__version__ = '0.1.0'
__maintainer__ = 'Jared M Smith'
__email__ = 'jared@jaredsmith.io'


class LokiSubscriber:
    def __init__(self, args, logger=None):
        self.cli_args = args
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.p = self.r.pubsub(ignore_subscribe_messages=True)
        self.channel = self.cli_args.redis_channel
        self.logger = logger

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
        content = loki_object.content_attributes
        if 'text' in content:
            # print('Found text in content')
            # print('Text: {}'.format(content['text']))
            # payload = twitter_swarm_decoder(content['text'])
            # print(content['text'])
            text = twitter_whatifs_decoder(content['text'])
            if text is not None:
                user = loki_object.entity_attributes
                print("What if found in: {}".format(content['text']))
                payload = "{},,,{},,,{}".format(text, user['user_screen_name'],
                                            user['user_profile_image_url'])
                print(payload)
                self.r.publish('loki_whatifs', payload)
