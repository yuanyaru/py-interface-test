# -*- coding:utf-8 -*-

import requests


# Leader节点写入（64）
def leader_write_log():
    leader_URL = 'http://192.168.100.64:18080/log'
    leader_data = {"debug": "debug log test"}
    leader_response = requests.post(leader_URL, json=leader_data)
    print leader_response.json()


# Follower节点邪写入（63）
def follower_write_log():
    follower_URL = 'http://192.168.100.63:18080/log'
    follower_data = {"info": "info log test"}
    follower_response = requests.post(follower_URL, json=follower_data)
    print follower_response.text


# 通过时间戳查询
def leader_read_log():
    read_URL_61 = 'http://192.168.100.61:18080/log/1565576462'
    read_URL_62 = 'http://192.168.100.62:18080/log/1565576462'
    read_URL_63 = 'http://192.168.100.63:18080/log/1565576462'
    read_URL_64 = 'http://192.168.100.64:18080/log/1565576462'
    read_URL = [read_URL_61, read_URL_62, read_URL_63, read_URL_64]
    for url in read_URL:
        response = requests.get(url)
        print response.text


def follower_read_log():
    read_URL_61 = 'http://192.168.100.61:18080/log/1565576089'
    read_URL_62 = 'http://192.168.100.62:18080/log/1565576089'
    read_URL_63 = 'http://192.168.100.63:18080/log/1565576089'
    read_URL_64 = 'http://192.168.100.64:18080/log/1565576089'
    read_URL = [read_URL_61, read_URL_62, read_URL_63, read_URL_64]
    for url in read_URL:
        response = requests.get(url)
        print response.text


# 范围查询
def scope_read_log():
    read_URL_61 = 'http://192.168.100.61:18080/log/'
    read_URL_62 = 'http://192.168.100.62:18080/log/'
    read_URL_63 = 'http://192.168.100.63:18080/log/'
    read_URL_64 = 'http://192.168.100.64:18080/log/'
    read_URL = [read_URL_61, read_URL_62, read_URL_63, read_URL_64]
    data = '{"from": "2019 08 12"}'
    for url in read_URL:
        response = requests.put(url, data)
        print response.json()


def delete_log():
    """
    URL_61 = 'http://192.168.100.61:18080/log/1565581471'
    URL_62 = 'http://192.168.100.62:18080/log/1565581471'
    URL_63 = 'http://192.168.100.63:18080/log/1565581471'
    follow_URL = [URL_61, URL_62, URL_63]
    for url in follow_URL:
        response = requests.delete(url)
        print response.text
    """
    leader_URL = 'http://192.168.100.64:18080/log/1565590430'
    response = requests.delete(leader_URL)
    print response.json()


if __name__ == '__main__':
    # leader_write_log()
    # follower_write_log()
    # leader_read_log()
    # follower_read_log()
    # delete_log()
    scope_read_log()
