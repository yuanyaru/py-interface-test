# -*- coding:utf-8 -*-

import requests
import json
import time
from leader import get_time


def mem():
    URL = 'http://192.168.100.61:18080/countmem'
    while True:
        response = requests.get(URL)
        dsm = json.loads(response.text)
        foo = dsm['foo']
        hello = dsm['hello']
        print str(foo) + "-" + get_time() + "---" + str(hello) + "-" + get_time()
        time.sleep(1)


# Leader节点写入（64）
def leader_write_mem():
    leader_URL = 'http://192.168.100.64:18080/mem'
    leader_data = {"foo": "bar"}
    leader_response = requests.post(leader_URL, json=leader_data)
    print leader_response.json()


# Follower节点邪写入（63）
def follower_write_mem():
    follower_URL = 'http://192.168.100.63:18080/mem'
    follower_data = {"hello": "world"}
    follower_response = requests.post(follower_URL, json=follower_data)
    print follower_response.text


# 查询foo
def foo_read_mem():
    read_URL_61 = 'http://192.168.100.61:18080/mem/foo'
    read_URL_62 = 'http://192.168.100.62:18080/mem/foo'
    read_URL_63 = 'http://192.168.100.63:18080/mem/foo'
    read_URL_64 = 'http://192.168.100.64:18080/mem/foo'
    read_URL = [read_URL_61, read_URL_62, read_URL_63, read_URL_64]
    for url in read_URL:
        response = requests.get(url)
        print response.text


# 查询hello
def hello_read_mem():
    read_URL_61 = 'http://192.168.100.61:18080/mem/hello'
    read_URL_62 = 'http://192.168.100.62:18080/mem/hello'
    read_URL_63 = 'http://192.168.100.63:18080/mem/hello'
    read_URL_64 = 'http://192.168.100.64:18080/mem/hello'
    read_URL = [read_URL_61, read_URL_62, read_URL_63, read_URL_64]
    for url in read_URL:
        response = requests.get(url)
        print response.text


def hello_delete_mem():
    leader_URL = 'http://192.168.100.64:18080/mem/hello'
    response = requests.delete(leader_URL)
    print response.text


def foo_delete_mem():
    URL_61 = 'http://192.168.100.61:18080/mem/foo'
    response = requests.delete(URL_61)
    print response.text


if __name__ == '__main__':
    mem()
    # leader_write_mem()
    # follower_write_mem()
    # hello_delete_mem()
    # foo_delete_mem()
    # foo_read_mem()
    # hello_read_mem()
