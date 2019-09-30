# Tensorflow usages

<!-- TOC -->

- [Tensorflow usages](#tensorflow-usages)
  - [多卡环境指定gpu](#%E5%A4%9A%E5%8D%A1%E7%8E%AF%E5%A2%83%E6%8C%87%E5%AE%9Agpu)
  - [按需占用显存](#%E6%8C%89%E9%9C%80%E5%8D%A0%E7%94%A8%E6%98%BE%E5%AD%98)

<!-- /TOC -->


## 多卡环境指定gpu

  首先确定gpu的编号`nvidia-smi`

  <img src='/assets/images/tensorflow_tricks/nvidia-smi.png'>

  - 在import module时指定

    ```python
    import tensorflow as tf
    import os
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    os.environ["CUDA_VISIBLE_DEVICES"] = "".format(gpu_index)
    ```

  - 创建session时指定

    ```python
    config = tf.ConfigProto()
    config.gpu_options.visible_device_list = '{}'.format(gpu_index)
    sess = tf.Session(config=config)
    ```

## 按需占用显存

  ```python
  config = tf.ConfigProto()
  config.gpu_options.allow_growth = True
  sess = tf.Session(config=config)
  ```
