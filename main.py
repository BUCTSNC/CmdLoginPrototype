from math import inf
import time
from utils import req
import sys
import logging
import getpass
logging.basicConfig(level=logging.INFO,format="%(message)s")
# logging.basicConfig(level=logging.DEBUG,format="%(asctime)s - %(module)s - %(filename)s - %(levelname)s : %(message)s")

logger = logging.getLogger("main")

def handleByte(byte):
    tail = "b"
    if byte >= 1024*1024*1024:
        byte /= 1024*1024*1024
        tail = "GB"
    elif byte >= 1024*1024:
        byte /= 1024*1024
        tail = "MB"
    elif byte >= 1024:
        byte /= 1024
        tail = "KB"
    return str(byte) + tail
def getUsername():
    print("账户:")
    username = input()
    if username == "" or username == None :
        raise UserWarning("账户输入为空")
    return username

def getPassword():
    password = getpass.getpass("密码:")
    if password == "" or password == None :
        raise UserWarning("密码输入为空")
    return password


def handleLogin():
    ip = req.getLocalIP()
    logging.info("Local IP: " + ip)
    if ip == None :
        logging.error("Fail to get ip")
        return

    logger.info("start login")
    try:
        username = getUsername()
        password = getPassword()
        res = req.login(username=username,password=password,acid="20",ip=ip)
    except UserWarning as warring:
        logging.error(warring)
    except Exception as e:
        logging.error(e)
    else:
        if "res" in res and res['res'] == "ok":
            logger.info("login finish")
        elif "ecode" in res and res['ecode'] == "E2901":
            logger.info("login fail, Please check your account or password")
        elif "error" in res:
            logger.error(res['error'])
        else:
            logger.error(res)

def handleLookup():
    logger.info("Lookup")
    info = req.getUserInfo()
    logging.debug(info)
    if "error" in info and info['error'] == "not_online_error":
        logging.error("not login")
        return
    elif "error" not in info or info['error'] != "ok":
        logging.error(info)
        return
    msg = "登录时间: {}\n登入后使用流量: {}\n在线IP: {}\n当前mac: {}\n当前账户: {}\n已使用流量: {}\n已使用时长: {}\n用户余额: {}\n本月已使用金额: {}\n".format(
            time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(info['add_time'])),
            handleByte(info['all_bytes']),
            info['online_ip'],
            info['user_mac'],
            info['user_name'],
            handleByte(info['sum_bytes']),
            "{}:{}:{}".format(info['sum_seconds']//(60*60),(info['sum_seconds']%(60*60))//60,info['sum_seconds']%60),
            str(info['user_balance'])+"元",
            str(info['user_charge'])+"元"
        )
    logging.info(msg)
    

def handleLogout():
    ip = req.getLocalIP()
    if ip == None :
        logging.error("Fail to get ip")
        return
    logging.info("Local IP: " + ip)

    logger.info("start logout")
    ret = req.logout(ip,"20")
    if "error" in ret and ret['error'] == "ok":
        logging.info("logout ok")
    elif "error" in ret:
        logging.error(ret['error'])
    else:
        logging.error(ret)
    logging.debug(ret)


def handleArgs(argv):
    functionMap = {
        "login":handleLogin,
        "info":handleLookup,
        "logout":handleLogout
    }
    if argv[1] not in functionMap:
        logger.error("not found operation")
        return
    functionMap[argv[1]]()
    

    
def main(argv):
    if len(argv) < 2:
        print("参数过少")
        return
    handleArgs(argv)

if __name__ == "__main__":
    main(sys.argv)