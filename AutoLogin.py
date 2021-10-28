from math import e
from requests.exceptions import ConnectTimeout
import utils.req
import requests
import re
import logging
import os
logging.basicConfig(filename="Autologin.log",level=logging.INFO,format="%(asctime)s - %(message)s")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 " \
     "Safari/537.36 "
headers = {
    "User-Agent": UA,
    "Connection": "keep-alive"
}
logger = logging.getLogger(__name__)


def net_check():
    try:
        res = requests.get("http://myip.ipip.net", headers=headers)
        text = res.text
        result = re.search("\d+.\d+\.\d+\.\d+", text)
        if result is None:
            raise ConnectionRefusedError("公网连接拒绝")
    except ConnectionRefusedError as e:
        logger.info(e)
        
    except Exception as e:
        logger.error("网络连接异常,登录终止")
        return None
    else:
        logging.info("已连接公网")
        return None
    try:
        ip, status = utils.req.getStatus()
    except ConnectTimeout as e:
        logger.error("非校园网环境")
        return None
    else:
        return ip, status
def login(ip):
    username = os.getenv("SRUN_LOGIN_USERNAME")
    password = os.getenv("SRUN_LOGIN_PASSWORD")
    if not username or not password:
        logger.error("用户名或密码未设置")
        return;
    try:
        res = utils.req.login(username, password, 20, ip)
    except Exception as e:
        logging.error(e)
    else:
        if "res" in res and res['res'] == "ok":
            logger.info("login finish")
        elif "ecode" in res and res['ecode'] == "E2901":
            logger.info(
                "login fail, Please check your account or password")
        elif "error" in res:
            logger.error(res['error'])
        else:
            logger.error(res)
def judge_login(res):
    if res == None:
        return
    else:
        ip,status = res
    if status == False:
        login(ip)
    else:
        logging.info("已登录")
if __name__ == "__main__":
    judge_login(net_check())
    
