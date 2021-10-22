import random
import time
import json
import hmac
import hashlib
from . import base64,Xencode

jQueryVersion = "1.12.4"
def JSONPTitleGenerator():
    title = "{}{}{}".format(random.random(), random.randint(0, 9), random.randint(0, 9))
    title = "jQuery" + (jQueryVersion + title).replace(".", "")
    return title


def TimeStampGenerator():
    timestamp = time.time()
    return int(round(timestamp * 1000))


def JSONPGenerator():
    return JSONPTitleGenerator() + "_" + str(TimeStampGenerator()), TimeStampGenerator() + 1


def IPDetect():
    List = ["202.4.130.95", "202.4.130.82"]
    # for ip in List:
    #     result = os.system("ping "+ip)
    # for i in dns.resolver.resolve("tree.buct.edu.cn").response.answer:
    #     print(i)
    return List[0]


def filterJSONP(JSONPTitle, data):
    return json.loads(data.replace(JSONPTitle, "")[1: -1])

def get_chksum(token,username,hmd5,ac_id,ip,n,ltype,i):
	chkstr = token+username
	chkstr += token+hmd5
	chkstr += token+str(ac_id)
	chkstr += token+ip
	chkstr += token+str(n)
	chkstr += token+str(ltype)
	chkstr += token+i
	return sha1(chkstr)


def md5(password,challenge):
    return hmac.new(challenge.encode(), password.encode(), hashlib.md5).hexdigest()

def sha1(v):
    # print(v)
    return hashlib.sha1(v.encode()).hexdigest()

def info(params,challenge):
    return "{SRBX1}" + base64.get_base64(Xencode.xEncode(params,challenge))

def getOS():
    return "Windows 95","Windows"


