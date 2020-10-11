# OpenDOTA Api

import logging as log

import requests


def refresh(uid):
    try:
        url = 'https://api.opendota.com/api/players/{}/refresh'.format(uid)
        r = requests.post(url)
        return r.json().get('length')
    except requests.HTTPError as e:
        log.error(e)


def get_matches(uid):
    try:
        url = 'https://api.opendota.com/api/players/{}/recentMatches'.format(
            uid)
        r = requests.get(url)
        return r.json()
    except requests.HTTPError as e:
        log.error(e)


def get_user(uids: list):
    try:
        url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/'
        r = requests.get(url, params={
            'key': '',
            'steamids': ','.join(uids)
        })
        return r.json().get('response')
    except requests.HTTPError as e:
        log.error(e)
