#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#             .''
#   ._.-.___.' (`\
#  //(        ( `'
# '/ )\ ).__. )
# ' <' `\ ._/'\
#    `   \     \
# example_weather_api.py
# YahooWeatherAPI
#
# Created by Chyi Yaqing on 04/07/19 12:42.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the MIT
import os
import time
import uuid
import urllib.request
import urllib.parse
import hmac
import hashlib
from base64 import b64encode


"""
Basic info
"""
env_dist = os.environ
url = 'https://weather-ydn-yql.media.yahoo.com/forecastrss'
method = 'GET'
app_id = env_dist.get('YAHOO_WEATHER_APP_ID')
consumer_key = env_dist.get('YAHOO_WEATHER_CLIENT_ID')
consumer_secret = env_dist.get('YAHOO_WEATHER_CLIENT_SECRET')
concat = '&'
query = {'location': 'shanghai,cn', 'format': 'json'}
oauth = {
            'oauth_consumer_key': consumer_key,
            'oauth_nonce': uuid.uuid4().hex,
            'oauth_signature_method': 'HMAC-SHA1',
            'oauth_timestamp': str(int(time.time())),
            'oauth_version': '1.0'
        }

"""
Prepare signature string (merge all params and SORT them)
"""
merged_params = query.copy()
merged_params.update(oauth)
sorted_params = [k + "=" + urllib.parse.quote(
    merged_params[k], safe='') for k in sorted(merged_params.keys())]
signature_base_str = method + concat + urllib.parse.quote(
        url, safe='') + concat + urllib.parse.quote(
                concat.join(sorted_params), safe='')

"""
Generate signature
"""
composite_key = urllib.parse.quote(
        consumer_secret, safe='', encoding="utf-8") + concat
oauth_signature = b64encode(hmac.new(bytes(composite_key, 'utf-8'), bytes(
    signature_base_str, 'utf-8'), hashlib.sha1).digest())

"""
Prepare Authorization header
"""
oauth['oauth_signature'] = oauth_signature
auth_header = 'OAuth ' + ', '.join(
        ['{}="{}"'.format(k, v) for k, v in oauth.items()])

"""
Send request
"""
url = url + '?' + urllib.parse.urlencode(query)
request = urllib.request.urlopen(url)
request.add_header('Authorization', auth_header)
request.add_header('X-Yahoo-App-Id', app_id)
response = urllib.request.urlopen(request).read()
print(response)
