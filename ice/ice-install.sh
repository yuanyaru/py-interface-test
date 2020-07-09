#!/usr/bin/bash
# author： yyr

cd /etc/yum.repos.d
sudo wget https://zeroc.com/download/Ice/3.7/el7/zeroc-ice3.7.repo
sudo yum install -y ice-all-runtime ice-all-devel
icebox -v
# 卸载
# yum remove -y ice*
