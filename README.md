# CmdLoginPrototype

北京化工大学校园网命令行登录原型

## 开发环境

Python 3.7.6

## 环境安装

```bash
pip install -r requirements.txt
```

### 文件说明

```file
├── LICENSE
├── README.md 
├── main.py --- 主脚本
├── AutoLogin.py ---自动登录脚本
├── requirements.txt --- 前置库
└── utils --- 校园网api调用库
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
- [x] 自动登录





## 使用说明
### main.py

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



### AutoLogin.py



#### 预配置

使用自动登录需要向环境变量中写入你的账户名与密码,请自行决定是否接受

用户名: `SRUN_LOGIN_USERNAME`

密码:`SRUN_LOGIN_PASSWORD`



##### Windows

请前往控制面板寻找



##### bash/zsh

临时变量:

```bash
export SRUN_LOGIN_USERNAME = {用户名}
export SRUN_LOGIN_USERNAME = {密码}
```



配置完后直接运行AutoLogin.py即可

