## /cgi-bin/rad_user_info

Request Params

| 参数名   | 参考值                                          | 解释              |
| -------- | ----------------------------------------------- | ----------------- |
| callback | jQuery{jQueryVersion}{randomNumber}_{TimeStamp} | JSONP跨域返回函数 |
| _        | {TimeStamp + 1}                                 | 时间戳            |



Response

#### 登录后:

| 字段名                                  | 可能的返回值   | 解释                                     |
| --------------------------------------- | -------------- | ---------------------------------------- |
| ServerFlag                              | 10位十进制整数 | 位置                                     |
| add_time                                | 时间戳         | 登入时间                                 |
| <font color="red">all_bytes</font>      | 整数           | 此次登入后使用的总流量(可能只计算下载？) |
| <font color="red">bytes_in</font>       | 整数           | 此次登入后下载流量                       |
| <font color="red">bytes_out</font>      | 整数           | 此次登入后上传流量                       |
| checkout_date                           | 0              | 不确定                                   |
| domain                                  | ‘’             | 不确定                                   |
| error                                   | 'ok'           | 返回状态                                 |
| keepalive_time                          | 时间戳         | 当前时间                                 |
| online_ip                               | IPV4           | 在线ip                                   |
| real_name                               | ‘’             | 不确定                                   |
| remain_seconds                          | 0              | 不确定                                   |
| sum_bytes                               | 整数           | 当前月份消耗bytes                        |
| sum_seconds                             | 整数           | 当前月份使用时长                         |
| sysver                                  | 一段字符串     | 后台版本                                 |
| user_balance                            | 浮点数         | 用户余额                                 |
| user_charge                             | 浮点数         | 用户消耗金额                             |
| user_mac                                | mac            | 当前连通设备mac                          |
| user_name                               | 学号/账户      | 用户账户                                 |
| <font color="red">wallet_balance</font> | 0              | 用户电子钱包余额                         |

标红为合理怀疑，但不确定真实含义

#### 登录前:

| 字段名    | 可能的返回值                         | 解释     |
| --------- | ------------------------------------ | -------- |
| error     | "not_online_error"                   | 状态     |
| ecode     | 0                                    | 错误代号 |
| client_ip | IPV4                                 | 当前ip   |
| online_ip | IPV4                                 | 当前ip   |
| res       | not_online_error                     | 返回状态 |
| srun_ver  | "SRunCGIAuthIntfSvr V1.18 B20190701" | 后台版本 |
| st        | 时间戳                               | 当前时间 |
| error_msg | ‘’                                   | 错误信息 |

