import os
import api

def clearScreen():
    os.system("cls")

def pauseScreen():
    os.system("pause")

def humanSpeedUnits(kbps):
    if(kbps > 1000):
        return f"{round(kbps/1000, 2)} MBps"
    else:
        return f"{kbps} KBps"

import socket
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def get_suffix_for_ip(ip):
    sub_ip = int(ip[-3:])%100
    suffixes = ["1qw","ded","ert","fcv","vgf","nrg","xcb","jku","cvd","wdv","2dw","njk","ftb","efv","azx","tuo","cvb","bcx","eee","mfw",
    "qdr","bhu","il0","3g7","xnh","7ht","23f","cmj","njf","3t8","ad9","zxq","tgb","nyj","ilo","tfh","cnd","wrx","421","vmy",
    "bhy","dfj","rmx","skh","3yz","xwa","etf","cxn","mji","gkt","fva","qpn","xdw","oir","lkf","bde","tew","mnb","dex","ves",
    "yjd","nmk","xcv","9hd","5gk","2fs","78v","03h","1mz","tcs","ula","rns","xow","alb","89v","344","7dw","bbf","ttt","opp"]

    return suffixes[sub_ip*16 % (len(suffixes) - 1 )]