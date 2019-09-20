google cloud platform shadowsocks

# 价格

Google云提供新用户1年的试用期以及300$的试用金。
<img src="/assets/images/gcp_shadowsocks/gcp-free-strategy.png" width="60%">

试用结束后，可以选择升级为付费用户（没有月租，使用资源就扣费），这时候GCP也会提供一定量的免费资源。

# 免费资源的限制条件
<table>
<tr>
<td><img src="/assets/images/gcp_shadowsocks/lifelong-free.png" width="60%"></td>
<td><img src="/assets/images/gcp_shadowsocks/limit-lifelong-free.png" width="60%"></td>
</tr>
</table>

免费资源之外的收费标准（每月）
<table>
<tbody>
<tr>
<th>流量来源-目的地地理位置</th>
<th>0-10 TB</th>
<th>10-150 TB</th>
<th>150-500 TB</th>
</tr>
<tr>
<th>北美洲-北美洲、欧洲-欧洲</th>
<td>$0.105</td>
<td>$0.08</td>
<td>$0.06</td>
</tr>
<tr>
<th>亚洲-亚洲</th>
<td rowspan="4" align="center" valign="middle">$0.12</td>
<td rowspan="4" align="center" valign="middle">$0.085</td>
<td rowspan="4" align="center" valign="middle">$0.08</td>
<tr>
<th>大洋洲-大洋洲</th>
</tr>
<tr>
<th>南美洲-南美洲</th>
</tr>
<tr>
<th>洲际<br>（不包括进出大洋洲和中国的流量）</th>
</tr>
<tr>
<th>进出大洋洲的洲际流量</th>
<td rowspan="2" align="center" valign="middle">$0.19</td>
<td rowspan="2" align="center" valign="middle">$0.16</td>
<td rowspan="2" align="center" valign="middle">$0.15</td>
</tr>
<tr>
<th>任何位置-中国</th>
</tr>
</tbody>
</table>


# 搭建Shadowsocks服务器
## 防火墙规则

<img src="/assets/images/gcp_shadowsocks/firewall-rules.png" width="60%">

## 创建VM实例
## 安装shadowsocks并启动ssserver
- VM中安装了python3，但是没有pip。首先安装pip
```shell
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
- 安装shadowsocks

  ```shell
  pip install shadowsocks --user #
  ```

- 启动ssserver服务

  ssserver配置文件
  config文件
  ```json
  {
    "server":"VM server ip",
    "server_port": port_number,
    "local_address":"127.0.0.1",
    "local_port":1080,
    "password":"",
    "timeout":300, "method":"aes-256-ctr",
    "fast_open":false, "workers":1
  }
  ```
  **server的ip**设置为gcp分配的外部ip时，报错`socket.error: [Errno 99] Cannot assign requested address`

  根据[chenweikang的blog](https://www.chenweikang.top/?p=679)，GCP在`/etc/hosts`文件中进行了网络映射（还不明白）
  查看hosts文件
  ```shell
  $ cat /etc/hosts
  127.0.0.1 localhost
  # The following lines are desirable for IPv6 capable hosts
  ::1 ip6-localhost ip6-loopback
  fe00::0 ip6-localnet
  ff00::0 ip6-mcastprefix
  ff02::1 ip6-allnodes
  ff02::2 ip6-allrouters
  ff02::3 ip6-allhosts
  169.254.169.254 metadata.google.internal metadata
  10.128.0.4 sss.us-central1-a.c.aerobic-acronym-253312.internal sss  # Added by Google
  169.254.169.254 metadata.google.internal  # Added by Google
  ```
  其中`sss`是VM实例的名字。ssserver config文件中的server ip应该设置为`sss.us-central1-a.c.aerobic-acronym-253312.internal`

  后台启动ssserver
  ```shell
  nohup shadowsocks -c config_file_path
  ```
