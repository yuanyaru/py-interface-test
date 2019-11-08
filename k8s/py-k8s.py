#!/usr/bin/python
# -*- encoding:utf-8 -*-

# pip2 install python-k8sclient
from k8sclient.client import api_client
from k8sclient.client.apis import apiv_api
import urllib3

k8s_url = '192.168.100.244:443'


# 判断k8s是否正常运行
def is_k8s_running():
    try:
        urllib3.PoolManager().request('GET', k8s_url)
        return True
    except urllib3.exceptions.HTTPError:
        return False


# 列举k8s中所有Service
def list_SVC():
    client = api_client.ApiClient(k8s_url)
    api = apiv_api.ApivApi(client)

    svcs = api.list_namespaced_service(namespace='default')
    # print "service数量：" + str(len(svcs.items))
    print(svcs)


# 列举k8s中所有RC
def list_RC():
    client = api_client.ApiClient(k8s_url)
    api = apiv_api.ApivApi(client)

    rcs = api.list_namespaced_replication_controller(namespace='default')
    # print("RC数量：" + str(len(rcs.items)))
    print(rcs)


if __name__ == '__main__':
    # is_k8s_running()
    list_SVC()
    list_RC()
