# Copyright 2019 Elevate Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
import requests
from os import environ as ENV
from flask import request
from flask import jsonify

WEBHOOK_URL = ENV['WEBHOOK_URL']


def make_payload(rax_json):
    target = rax_json['details']['target']
    alarm_state = rax_json['details']['state']
    alarm_status = rax_json['details']['status']
    check_label = rax_json['check']['label']
    entity_label = rax_json['entity']['label']
    dashboard_link = rax_json['dashboard_link']

    payload = {'attachments': [
        {
            'fallback': "Rackspace Monitoring Alert: %s - %s" % (check_label, entity_label),
            'text': 'Rackspace Monitoring Alert!',
            'fields': [
                {'title': 'Target',
                 'value': target,
                 'short': True},
                {'title': 'Check',
                 'value': check_label,
                 'short': True},
                {'title': 'Entity Label',
                 'value': entity_label,
                 'short': True},
                {'title': 'Status',
                 'value': "%s - %s" % (alarm_state, alarm_status),
                 'short': False}],
            'color': '#5555AA'
        },
        {
            'fallback': "View Alert: %s" % dashboard_link,
            'actions': [
                {
                    'type': 'button',
                    'text': "View Alert",
                    'style': 'primary',
                    'url': dashboard_link
                }],
            'color': '#5555AA'
        }]}
    return payload


def send_slack_message(rax_json):
    req_data = make_payload(rax_json)
    logging.warn('sending to slack: %s' % req_data)
    resp = requests.post(WEBHOOK_URL, json=req_data)
    logging.warn('Got: %s' % resp.text)


def handleRequest(request):
    resp = {'status': 'OK'}
    json = request.json

    logging.warn('Got request: %s' % request.json)
    send_slack_message(json)

    return jsonify(resp)
