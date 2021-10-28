---
layout: post
title:   SSL/TLS certificate
categories: Work
tags: jekyll
author: Todd
description: Change python version
---

# SSL/TLS 认证

NameSilo不提供SSL/TLS认证，很良心的推荐了[两种**free**的认证方式](https://www.namesilo.com/Support/Why-we-do-not-offer-SSL%2FTLS-certificates)
- [LetsEncrypt](https://letsencrypt.org/getting-started/)
- CloundFlare

我选择了第一种，LetsEncrypt

过程比较简单，安装并运行'certbot'，根据提示走即可

1. 安装certbot

     ```shell
      sudo apt-get update
      sudo apt-get install software-properties-common
      sudo add-apt-repository universe
      sudo add-apt-repository ppa:certbot/certbot
      sudo apt-get update
      # install
      sudo apt install certbot
     ```

2. 运行certbot

    官方给的运行指令

    ```shell
    sudo certbot certonly --standlone
    ```

    运行过程需要输入一些配置，但是刚开始不是很明白配置的含义。后来参考了一篇[blog](https://www.geosynopsis.com/post/ssl-for-jekyll-rendered-static-site)

    ```shell
    certbot certonly --manual --server https://acme-v01.api.letsencrypt.org/directory -d your_domain.com -d www.your_domain.com
    ```

  - 设置紧急提醒邮箱

    ```shell
    Saving debug log to /var/log/letsencrypt/letsencrypt.log
    Plugins selected: Authenticator manual, Installer None
    Enter email address (used for urgent renewal and security notices) (Enter 'c' to
    cancel): you_email_address
    ```

  - 是否可以给你发邮件

    ```shell
    Would you be willing to share your email address with the Electronic Frontier
    Foundation, a founding partner of the Let's Encrypt project and the non-profit
    organization that develops Certbot? We'd like to send you email about our work
    encrypting the web, EFF news, campaigns, and ways to support digital freedom.
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    (Y)es/(N)o: N
    ```

  - 是否使用本机ip

    ```shell
    NOTE: The IP of this machine will be publicly logged as having requested this
    certificate. If you're running certbot in manual mode on a machine that is not
    your server, please ensure you're okay with that.

    Are you OK with your IP being logged?
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    (Y)es/(N)o: Y
    ```

  - 在网站指定路经下生成file

    ```shell
    Create a file containing just this data:
    XXXXXXXXXXXXXXXXXXXXXXX #file的内容
    And make it available on your web server at this URL:
    http://www.your_domain.com/.well-known/acme-challenge/XXXXX # file的路经
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Press Enter to Continue
    ```

    我是使用jekyll搭建静态blog，如果想将额外的文件/文件夹放到server中，需要将该文件的路经写道`_config.yml`文件中。

    首先，创建并将指定内容写入文件;之后，将该文件对应的文件夹include到配置文件中
    ```
    include: [".well-known"]
    ```
