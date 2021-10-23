# CmdLoginPrototype

北京化工大学校园网命令行登录原型

### 开发环境

Python 3.7.6

### 使用说明

```bash
pip install -r requirements.txt
python main.py {username} {password}
```



### 文件说明

```file
├── LICENSE
├── README.md 
├── main.py --- 入口文件
├── requirements.txt --- 前置库
└── utils
    ├── Xencode.py --- Xencode加密方法
    ├── __init__.py --- python包基础文件
    ├── base64.py --- jQuery base64加密方法
    ├── req.py --- 请求方法
    └── utils.py --- 工具方法
```



### 待完成功能

- logout方法
- 获取当前系统平台及其标识
- 日志系统
- 用户数据获取
- 登录状态获取
