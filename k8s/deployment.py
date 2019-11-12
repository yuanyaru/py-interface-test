# -*- encoding:utf-8 -*-

# 完成对deployment服务的增删改查
from kubernetes import client, config

DEPLOYMENT_NAME = "kubectl-client-test"


def create_deployment_object():
    # docker镜像版本，监听端口
    # Config Pod template container
    container = client.V1Container(
        name="httpd-client",
        image="httpd",
        ports=[client.V1ContainerPort(container_port=80)])

    # Create and config a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "nginx"}),
        spec=client.V1PodSpec(containers=[container]))

    # 应用的副本数
    # Create the specification of deployment
    spec = client.ExtensionsV1beta1DeploymentSpec(
        replicas=2,
        template=template)

    # api的版本
    # Instantiate the deployment object
    deployment = client.ExtensionsV1beta1Deployment(
        api_version="extensions/v1beta1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=DEPLOYMENT_NAME),
        spec=spec)

    return deployment


def create_deployment(api_instance, deployment):
    # Create deployment
    api_response = api_instance.create_namespaced_deployment(
        body=deployment,
        namespace="default")
    print("Deployment created. status='%s'" % str(api_response.status))


def update_deployment(api_instance, deployment):
    # Update container image
    deployment.spec.template.spec.containers[0].image = "nginx:1.9.1"
    # Update the deployment
    api_response = api_instance.patch_namespaced_deployment(
        name=DEPLOYMENT_NAME,
        namespace="default",
        body=deployment)
    print("Deployment update. status='%s'" % str(api_response.status))


def delete_deployment(api_instance):
    # Delete deployment
    api_response = api_instance.delete_namespaced_deployment(
        name=DEPLOYMENT_NAME,
        namespace="default",
        body=client.V1DeleteOptions(
            propagation_policy='Foreground',
            grace_period_seconds=5))
    print("Deployment deleted. status='%s'" % str(api_response.status))


def main():
    # 1. 加载配置文件，找到endpoint和获取权限
    # if no argument provided, the config will be loaded from default location.
    config.load_kube_config(config_file="kubeconfig.yaml")
    # 2. 创建python客户端api
    extensions_v1beta1 = client.ExtensionsV1beta1Api()
    # 3. 创建客户端对象
    # Create a deployment object with client-python API. The deployment we
    # created is same as the `nginx-deployment.yaml` in the /examples folder.
    deployment = create_deployment_object()
    # 4. 调用客户端对象，完成创建具体请求
    # kubectl get deployment
    # create_deployment(extensions_v1beta1, deployment)

    # update_deployment(extensions_v1beta1, deployment)
    # 调用客户端对象，完成删除具体请求
    delete_deployment(extensions_v1beta1)


if __name__ == '__main__':
    main()
