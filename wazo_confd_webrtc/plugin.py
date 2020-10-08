# -*- coding: utf-8 -*-
# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_calld.auth import required_acl
from wazo_calld.http import AuthResource


class WebRTCResource(AuthResource):

    @required_acl('confd.users.me.read')
    def get(self):
        return {
            'stun_server': [
                'stun.wazo.io:443',
                'stun.l.google.com:19302'
            ],
            'turn_server': [],
            'ice_timeout': 300,
            'debug': {
                'fluentd': 'https://myfluentd',
                'level': 'verbose'
            }
        }, 200

class Plugin(object):

    def load(self, dependencies):
        api = dependencies['api']
        api.add_resource(WebRTCResource, '/configuration/webrtc', resource_class_args=[])
