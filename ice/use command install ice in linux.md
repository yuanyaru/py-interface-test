#### 配置yum仓库
``` bash
cd /etc/yum.repos.d
sudo wget https://zeroc.com/download/Ice/3.7/el7/zeroc-ice3.7.repo
sudo wget https://zeroc.com/download/rpm/zeroc-ice-el6.repo
```

#### Install Ice for C++, Python, PHP, and all Ice services.
``` bash
sudo yum install -y ice-all-runtime ice-all-devel
```

#### 通过 ``` bash icebox -v ``` 查看安装的版本号

