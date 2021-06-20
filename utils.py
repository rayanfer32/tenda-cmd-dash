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
