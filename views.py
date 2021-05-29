import time

from api import getAllStatsJson, getDeviceParamFromIp, getTrafficStatsJson
from utils import clearScreen
from config import TOTAL_BW, MAX_BLOCKS

def showSimpleStats():
    stats = getTrafficStatsJson("goform/updateIptAccount")
    clearScreen()
    for device in stats:
        print(f"IP: {device['ip']} > RECV:{device['recievedMB']} MB")
        print("------------------")
    time.sleep(1)


def showAdvancedStats():
        stats = getAllStatsJson()
        clearScreen()  
        
        # bandwidth bar  
        bu = stats[-1]["metrics"]["totalSpeed"]
        br = round((TOTAL_BW - bu ), 2)

        print(f'BW: {bu} KB|BW Rem: {br} KB')
        load = round(bu/(TOTAL_BW/100), 2)
        print(f"Load: {load}%")
        print('█'*int(bu/(TOTAL_BW/MAX_BLOCKS)))
        
        for device in stats:
            try:
                name = device["name"]
                speed = round(device["downKB"] ,0)
                used = int(device["recievedMB"] )
                unitLoad = int(speed/(TOTAL_BW/MAX_BLOCKS))
                # if(unitLoad>0):
                
                print(f"{name} | {used} MB")
                print('█'*unitLoad,f"{speed}KBps")
            except:
               pass

        time.sleep(1)

