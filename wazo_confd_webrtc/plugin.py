# -*- coding: utf-8 -*-
# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_confd.auth import required_acl
from wazo_confd.helpers.restful import ItemResource


class WebRTCResource(ItemResource):

    def __init__(self):
        pass

    @required_acl('confd.users.me.read')
    def get(self):
        return {
            'stun_server': [
                {'urls': 'stun.wazo.io:443'},
                {'urls': 'stun.l.google.com:19302}'
            ],
            'turn_server': [{
                'urls': 'turn.wazo.io:443',
                'username': 'toto',
                'credential': 'toto'
            }],
            'ice_timeout': 300,
            'debug': {
                'fluentd_uri': 'https://myfluentd',
                'level': 'verbose'
            }
        }, 200

class Plugin(object):

    def load(self, dependencies):
        api = dependencies['api']
        api.add_resource(WebRTCResource, '/configuration/webrtc')
