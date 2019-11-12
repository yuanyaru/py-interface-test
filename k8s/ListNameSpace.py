#!/usr/bin/python
# -*- encoding:utf-8 -*-

from kubernetes import client, config
# cp $HOME/.kube/config  deamon/config/kubeconfig.yaml
config.kube_config.load_kube_config(config_file="kubeconfig.yaml")


class K8s:
  def __init__(self):
    self.Connect = client.CoreV1Api()

  def ListNameSpace(self):
    data = []
    for ns in self.Connect.list_namespace().items:
      data.append(ns)
    return data

  def CreateNameSpace(self, name):
    body = client.V1Namespace()
    body.metadata = client.V1ObjectMeta(name=name)
    return self.Connect.create_namespace(body=body)


if __name__ == '__main__':
    k = K8s()
    print(k.ListNameSpace())
