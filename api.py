import json
import urllib
import base64
import logging
import requests
from config import ROUTER_IP, ROUTER_PASS, TOTAL_BW, REQ_COOKIE


logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

proxies = urllib.request.getproxies()
session = requests.Session()
_DEVICES = []  # donot edit! used as memo internaly


def _ask_modem_something(modem_address, modem_password, data, api_path):
    if not modem_address.startswith('http'):
        modem_address = 'http://' + modem_address.strip('/')
        # modem_address = modem_address.strip('/')
    api_path = api_path.lstrip('/')

    ecos_pwd = base64.b64encode(modem_password.encode('utf-8')).decode()

    if REQ_COOKIE == None:
        cookies = {
            # 'Authorization': f'Basic {pswd.decode()}'
            # 'Authorization': 'Basic YWRtaW46YWRtaW4='
            # for lan connection mji language=en; ecos_pw=YWRtaW4=5gk:language=en
            "Authorization": f"language=en; ecos_pw={ecos_pwd}mji:language=en"
        }
    else: 
        print("using req cookie")
        cookies = {
            # 'Authorization': f'Basic {pswd.decode()}'
            # 'Authorization': 'Basic YWRtaW46YWRtaW4='
            # for lan connection mji language=en; ecos_pw=YWRtaW4=5gk:language=en
            
            "Authorization": REQ_COOKIE
        }

    # logging.warning(cookies)
    # f"http://{ROUTER_IP}/goform/updateIptAccount"
    # referer: http://192.168.0.1/sys_iptAccount.asp

    headers = {
        'Referer': '{}/'.format(modem_address)
    }

    global session
    try:
        r = session.post('{}/{}'.format(modem_address, api_path),
                         headers=headers, cookies=cookies, data=data)
    except:
        logging.info("using proxy")
        r = session.post('{}/{}'.format(modem_address, api_path),
                         headers=headers, cookies=cookies, data=data, proxies=proxies)
    # logging.debug(r.content)
    return r.content


def _getTrafficStats(api_path="goform/updateIptAccount", data="something"):
    resp = _ask_modem_something(ROUTER_IP, ROUTER_PASS, data, api_path)
    return resp.decode()


def getTrafficStatsJson(api_path="goform/updateIptAccount", data="something"):
    resp = _getTrafficStats(api_path, data)
    jsonResponse = []

    try:
        splitLines = resp.split('\n')
        for line in splitLines:
            ip, upKB, downKB, sentMsg, sentMB, recievedMsg, recievedMB = line.split(
                ';')
            jsonResponse.append({
                "ip": ip,
                "upKB": float(upKB),
                "downKB": float(downKB),
                "sentMsg": float(sentMsg),
                "sentMB": float(sentMB),
                "recievedMsg": float(recievedMsg),
                "recievedMB": float(recievedMB)})
    except Exception as e:
        logging.info(e)

    return jsonResponse


def _getDhcpList(api_path="lan_dhcp_clients.asp"):
    h = _getTrafficStats(api_path)
    start = 'dhcpList=new Array('
    startPtr = h.find(start)
    _dhcplist = h[startPtr + len(start): h.find(")", startPtr)]
    # print(_dhcplist)
    return _dhcplist


def getDhcpListJson(api_path="lan_dhcp_clients.asp"):
    devices = []
    jsonResponse = []

    for device in _getDhcpList().split(','):
        devices.append(device[1:-1])

    # name , ip , mac , lease time
    for device in devices:
        try:
            name, ip, mac, jank, leaseTime = device.split(';')
            jsonResponse.append({
                "name": name,
                "ip": ip,
                "mac": mac,
                "jank": jank,
                "leaseTime": float(leaseTime)
            })
        except Exception as e:
            logging.debug(e)

    return jsonResponse


def getDeviceParamFromIp(ip, param):
    global _DEVICES
    if _DEVICES == []:
        _DEVICES = getDhcpListJson()
    for device in _DEVICES:
        if(device["ip"] == ip):
            return device[param]
    _DEVICES = []


def getAllStatsJson():
    devices = getTrafficStatsJson("goform/updateIptAccount")
    jsonResponse = {}
    devicesArr = []
    totalDownKB = 0
    totalUpKB = 0
    totalRecievedMB = 0
    totalSentMB = 0

    for device in devices:
        deviceIP = device["ip"]
        
        _name = getDeviceParamFromIp(deviceIP, "name")
        if _name == "" or _name == None:
            device["name"] = getDeviceParamFromIp(deviceIP, "mac")
        else:
            device["name"] = _name
            
        device["mac"] = getDeviceParamFromIp(deviceIP, "mac")
        device["jank"] = getDeviceParamFromIp(deviceIP, "jank")
        device["leaseTime"] = getDeviceParamFromIp(deviceIP, "leaseTime")
        device["totalSpeed"] = device["upKB"] + device["downKB"]
        device["totalUsedMB"] = round(device["sentMB"] + device["recievedMB"], 2)
        devicesArr.append(device)

        totalDownKB += device["downKB"]
        totalUpKB += device["upKB"]
        totalSentMB += device["sentMB"]
        totalRecievedMB += device["recievedMB"]

    # calculated params
    metrics = {}
    totalSpeed = totalDownKB + totalUpKB
    totalUsedGB = (totalSentMB + totalRecievedMB)/1024
    metrics["totalDownKB"] = round(totalDownKB, 2)
    metrics["totalUpKB"] = round(totalUpKB, 2)
    metrics["totalSpeed"] = round(totalSpeed, 2)
    metrics["totalSentMB"] = round(totalSentMB, 2)
    metrics["totalRecievedMB"] = round(totalRecievedMB, 2)
    
    metrics["load"] = round((totalSpeed)/(TOTAL_BW/100), 2)
    metrics["totalUsedGB"] = round(totalUsedGB, 2)

    jsonResponse["devices"] = devicesArr 
    jsonResponse["metrics"] = metrics
    return jsonResponse



