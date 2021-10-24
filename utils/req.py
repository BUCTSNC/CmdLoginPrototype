from . import utils
import requests

baseIP = utils.IPDetect()
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 " \
     "Safari/537.36 "

headers = {
    "User-Agent": UA,
    "Cookie": "lang=zh-CN; _ga=GA1.3.1108883948.1583300884",
    "Referer": "http://"+baseIP+"/srun_portal_pc?ac_id=20&theme=basic",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive"
}



def reloadBaseUrl():
    global baseIP
    baseIP = utils.IPDetect()


def getChallenge(JSONP,username, ip):
    url = "http://" + baseIP + "/cgi-bin/get_challenge"
    params = {
        "username": username,
        "ip": ip,
        "callback": JSONP[0],
        "_": JSONP[1],
    }
    res = requests.get(url, params)
    data = utils.filterJSONP(JSONP[0], res.text)
    return data['challenge']


def getLocalIP():
    JSONP = utils.JSONPGenerator()
    url = "http://" + baseIP + "/cgi-bin/rad_user_info"
    res = requests.get(url, {"callback": JSONP[0], "_": JSONP[1]}, headers=headers)
    text = res.text
    data = utils.filterJSONP(JSONP[0], text)
    return data['online_ip']


def login(data):
    url = "http://" + baseIP + "/cgi-bin/srun_portal"
    JSONP = utils.JSONPGenerator()
    ip = getLocalIP()
    challenge = getChallenge(JSONP,data["username"],ip)
    msg = '{"username":"' + data["username"] + '","password":"' + data["password"] + '","ip":"'+ip+'","acid":"20","enc_ver":"srun_bx1"}'
    i = utils.info(msg,challenge)
    hmd5 = utils.md5(data["password"],challenge)
    data['password'] = "{MD5}" + hmd5
    device,platform = utils.getOS()
    params = {
        'callback':JSONP[0],
        "action": "login",
        "username":data["username"],
        "password":data["password"],
        "ac_id":data["acid"],
        "ip": ip,
        "chksum": utils.get_chksum(challenge,data["username"],hmd5,data["acid"],ip,200,1,i),
        "info":i,
        "n":"200",
        "type":"1",
        "os":device,
        "name":platform,
        "double_stack":"0",
        '_':JSONP[1]
    }
    # print(params)
    res = requests.get(url,params,headers=headers)
    text = res.text
    data = utils.filterJSONP(JSONP[0], text)
    # print(data)


def getUserInfo():
    JSONP = utils.JSONPGenerator()
    url = "http://" + baseIP + "/cgi-bin/rad_user_info"
    res = requests.get(url, {"callback": JSONP[0], "_": JSONP[1]}, headers=headers)
    text = res.text
    data = utils.filterJSONP(JSONP[0], text)
    return data