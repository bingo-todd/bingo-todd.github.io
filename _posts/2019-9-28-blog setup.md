---
layout: post
title:  "blog setup"
categories: network
tags: blog
author: Todd
description: setup static blog using jekyllw
---

<!-- TOC -->

- [安装gem环境](#%E5%AE%89%E8%A3%85gem%E7%8E%AF%E5%A2%83)
- [安装Jekyll](#%E5%AE%89%E8%A3%85jekyll)
- [启动Jekyll](#%E5%90%AF%E5%8A%A8jekyll)

<!-- /TOC -->

使用jekyll托管blog，首先需要配置环境

# 安装gem环境

- Ubuntu &nbsp; [(official doc)](https://jekyllrb.com/docs/installation/ubuntu/)

  主要命令
  ```shell
  sudo apt-get install ruby-full build-essential zlib1g-dev
  # 环境变量
  echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
  echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
  echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
  source ~/.bashrc
  # 安装Jekyll
  gem install jekyll bundler
  ```

- Windows &nbsp; [(official doc)] (https://jekyllrb.com/docs/installation/windows/)

  主要过程
  - 安装gem

    下载ruby安装包，官方教程推荐 2.4版本的[**Ruby+Devkit**](https://rubyinstaller.org/downloads/)
    > We only cover RubyInstaller-2.4 and newer here, older versions need to install the Devkit manually.

    安装之后，在终端执行`ridk install`以安装`gem`以及扩展包
    > Run the `ridk install` step on the last stage of the installation wizard. This is needed for installing gems with native extensions.

# 安装Jekyll

  新打开一个命令行窗口（gem安装过程会将修改`PATH`，修改在之后的终端才起效）
  ```shell
  gem install jekyll bundler
  ```

# 启动Jekyll

  可以使用`jekyll new blog_dir`初始化一个空白的blog，或者在github上下载别人的模板，
  `blog_dir`下启动服务
  ```shell
  jekyll serve
  # 在vps上指定端口`-P 80`，可以在浏览器中根据ip访问blog
  ```
