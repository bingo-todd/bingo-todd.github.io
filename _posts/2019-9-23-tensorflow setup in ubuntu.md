深度学习环境搭建

步骤
1. nvida驱动
2. cuda
3. cuDNN
4. tensorflow-gpu


## Nvida驱动
- 查看显卡型号
  ```shell
  lspci | grep -i nvidia
  # -i = --ignore-case
  ```

  3种安装方法<https://blog.csdn.net/tjuyanming/article/details/80862290>
  1. 基于ubuntu仓库的自动安装
      - 检测显卡的型号以及推荐的驱动

          ```shell
          ubuntu-driver devices
          ```

      - 安装推荐的驱动程序

          ```shell
          sudo apt-get install nvida-driver-418
          ```

  2. 基于PPA仓库的自动安装

      通过图形界面安装NVIDA的beta驱动
      1. 添加PPA存储库

          ```shell
          $ sudo add-apt-repository ppa:graphics-drivers/ppa
          $ sudo apt update
          ```
          接下来的步骤与第一种安装方法一致
      2. 识别显卡型号以及推荐驱动版本
      3. apt安装

  3. 下载nvida官方驱动进行手动安装

      Ubuntu会默认安装Nouveau驱动，因此首先应该ia卸载第三方驱动，再进行安装
      - 设置禁用Nouveau驱动
        创建blacklist文件，`/etc/modprobe.d/blacklist-nouveau.conf`，添加以下内容
        ```shell
        blacklist nouveau
        options nouveau modeset=0
        ```
      - 重新生成kernel initramfs（还没查是啥）

      ```shell
      sudo update-initramfs -u
      ```

      - 重启进入text mode，就可以安装了

      >The reboot is required to completely unload the Nouveau drivers and prevent the graphical interface from loading. The CUDA driver cannot be installed while the Nouveau drivers are loaded or while the graphical interface is active.

## 安装cuda

  从官网<https://developer.nvidia.com/cuda-toolkit-archive>下载的cuda10，安装之后，还需要配置环境变量（曾经因为没有配置lib路径，导致import tensorflow报错，卡了一天多）
  - 安装cuda

    ```shell
    wget http://developer.download.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.243_418.87.00_linux.run
    sudo chmod +x cuda_10.1.243_418.87.00_linux.run
    sudo ./cuda_10.1.243_418.87.00_linux.run
    ```

  - 配置环境

      ```shell
      export PATH=/usr/local/cuda-10.1/bin:/usr/local/cuda-10.1/NsightCompute-2019.1${PATH:+:${PATH}}
      export LD_LIBRARY_PATH=/usr/local/cuda-10.1/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
      ```

      查看cuda版本
      cat /usr/local/cuda/version.txt

## 安装cuDNN

  其实只需要将其中的文件copy到cuda安装目录下就可以了
  ```shell
  sudo cp cuda/include/cudnn.h /usr/local/cuda/include/
  sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64/
  ```

  `import tensorflow`能运行但是warning，没有加载很多`xxx.so.10.0`文件，其实lib64目录下有对应的`xxx.so.10`以及其他同名但后缀不同的文件/link，可以在该文件夹下创建`xxx.so.10.0`链接到'xxx.so'。不过,该文件夹下并没有`libbulas.so`文件，而系统其实已经在某处安装，因此只需要找到并链接到该文件即可
  ```shell
  $ ldconfig -p | grep cublas

    libcublasLt.so.10 (libc6,x86-64) => /usr/lib/x86_64-linux-gnu/libcublasLt.so.10
    libcublasLt.so (libc6,x86-64) => /usr/lib/x86_64-linux-gnu/libcublasLt.so
    libcublas.so.10 (libc6,x86-64) => /usr/lib/x86_64-linux-gnu/libcublas.so.10
    libcublas.so.9.0 (libc6,x86-64) => /usr/local/cuda/lib64/libcublas.so.9.0
    libcublas.so (libc6,x86-64) => /usr/local/cuda/lib64/libcublas.so
    libcublas.so (libc6,x86-64) => /usr/lib/x86_64-linux-gnu/libcublas.so
  ```

## 安装tensorflow-gpu

  直接使用pip安装
  ```shell
  pip install tensorflow-gpu
  ```
