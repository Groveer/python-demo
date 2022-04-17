#!/usr/bin/python3
import json
import requests
from datetime import datetime


def get_app_access_token():
    url = 'https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal/'
    header = {
        'Content-Type': 'application/json'
    }
    data = {
        'app_id': 'cli_a056996788f9500b',
        'app_secret': 'AqYWgReOA0DUYcVEDhlFsUwIjI3pd7NH'
    }
    res = requests.post(url, data=json.dumps(data), headers=header)
    print('get_app_access_token:{}'.format(res.content.decode()))
    return res.content.decode()


def get_user_access_token(code):
    url = 'https://open.feishu.cn/open-apis/authen/v1/access_token'
    header = {
        'Content-Type': 'application/json'
    }
    data = {
        'app_access_token': get_app_access_token(),
        'grant_type': 'authorization_code',
        'code': code
    }
    res = requests.post(url, data=json.dumps(data), headers=header)
    content = res.content.decode()
    tokens = {
        'user_access_token': content['data']['access_token'],
        'refresh_token': content['data']['refresh_token']
    }
    print('get_user_access_token:{}'.format(json.dumps(tokens)))
    return tokens


time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
print(time)
