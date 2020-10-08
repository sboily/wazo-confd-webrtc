Add webrtc configuration for Wazo app to wazo-confd

Installation
------------

    wazo-plugind-cli -c "install git https://github.com/sboily/wazo-confd-webrtc"

Use
---

Check the API in your wazo in calld section in http://wazo_ip/api

return:

    {
        'stun_server': [
             'stun.wazo.io:443',
             'stun.l.google.com:19302
         ],
         'turn_server': [
             'toto@tutu:turn.wazo.io:443
         ],
         ice_timeout: 300,
         debug: {
             'fluentd': 'https://myfluentd',
             'level': 'verbose'
         }
    }
