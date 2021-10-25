# CmdLoginPrototype

北京化工大学校园网命令行登录原型

### 开发环境

Python 3.7.6

### 环境安装

```bash
pip install -r requirements.txt
```

### 使用说明


#### 登录

```bash
python main.py login
```

#### 查询

```bash
python main.py info
```

#### 登出

```bash
python main.py logout
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

- [x] logout方法
- [ ] 获取当前系统平台及其标识
- [ ] 日志系统
- [x] 用户数据获取
- [x] 登录状态获取
- [x] 登录密码秘文输入

