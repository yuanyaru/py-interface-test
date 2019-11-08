#!/usr/bin/python
# -*- encoding:utf-8 -*-

# pip3 install kubernetes
from kubernetes import client


def main():
    with open('token.txt', 'r') as file:
        Token = file.read().strip('\n')

    APISERVER = 'https://192.168.100.244:443'

    # Create a configuration object
    configuration = client.Configuration()

    # Specify the endpoint of your Kube cluster
    configuration.host = APISERVER

    # Security part.
    # In this simple example we are not going to verify the SSL certificate of
    # the remote cluster (for simplicity reason)
    configuration.verify_ssl = False

    # Nevertheless if you want to do it you can with these 2 parameters
    # configuration.verify_ssl = True
    # ssl_ca_cert is the filepath to the file that contains the certificate.
    # configuration.ssl_ca_cert = "certificate"
    configuration.api_key = {"authorization": "Bearer " + Token}

    # configuration.api_key["authorization"] = "bearer " + Token
    # configuration.api_key_prefix['authorization'] = 'Bearer'
    # configuration.ssl_ca_cert = 'ca.crt'
    # Create a ApiClient with our kubeconfig.yaml
    client.Configuration.set_default(configuration)

    # 将所有namespace下的pod的基本信息打印出来
    # kubectl get pods --all-namespaces
    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


if __name__ == '__main__':
    main()