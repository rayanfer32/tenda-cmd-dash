import time

from api import getAllStatsJson, getDeviceParamFromIp, getTrafficStatsJson
from utils import clearScreen
from config import TOTAL_BW, MAX_BLOCKS, WAIT_BEFORE_UPDATE

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
        load = stats[-1]["metrics"]["load"]
        totalUsedGB = stats[-1]["metrics"]["totalUsedGB"]
        print(f'Speed: {bu} KBps|Total: {totalUsedGB} GB|Load: {load}%')
        
        print('█'*int(bu/(TOTAL_BW/MAX_BLOCKS)))
        
        count = 0
        for device in stats:
            try:
                name = device["name"]
                speed = round(device["downKB"] ,0)
                used = int(device["recievedMB"] )
                unitLoad = int(speed/(TOTAL_BW/MAX_BLOCKS))                
                count +=1
                print(f"{count}: {name} | {used} MB")
                print('█'*unitLoad,f"{speed}KBps")
            except:
               pass

        time.sleep(WAIT_BEFORE_UPDATE)