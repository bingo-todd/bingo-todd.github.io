---
layout: post
title:  "Change python version"
categories: Work
tags: python
author: Todd
description: Change python version
---


# methods

## update-alternate
```shell
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.4 priority_number
```
查看已有的 python alternatives
```shell
sudo update-alternatives --config python
```

**问题**
更新python的版本之后，会导致奇怪的问题
```shell
st@st-MS-7918:~$ add-apt-repository --help
Traceback (most recent call last):
  File "/usr/bin/add-apt-repository", line 11, in <module>
    from softwareproperties.SoftwareProperties import SoftwareProperties, shortcut_handler
  File "/usr/lib/python3/dist-packages/softwareproperties/SoftwareProperties.py", line 28, in <module>
    import apt_pkg
ModuleNotFoundError: No module named 'apt_pkg'
```

## 软链接
在搜索路径下，将python链接到目标python版本下的可执行文件
```shell
sudo ln -sfn path_to_tar_python/bin/python3.6 /usr/bin/python3
```
`ln`的基本用法
```shell
ln [options] TARGET LINK_NAME
```
Options
- s: symbolic, make symbolic links instead of hard links
- f: force
- n: no-dereference, treat LINK_NAME as a normal file if it is a symbolic link to a directory

**同样存在上述问题**
