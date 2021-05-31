import time

from api import getAllStatsJson, getTrafficStatsJson
from utils import clearScreen, humanSpeedUnits
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
        bu = stats["metrics"]["totalSpeed"]
        hspeed = humanSpeedUnits(bu)
        load = stats["metrics"]["load"]
        totalUsedGB = stats["metrics"]["totalUsedGB"]
        print(f'Speed: {hspeed} |Total: {totalUsedGB} GB|Load: {load}%')
        
        print('█'*int(bu/(TOTAL_BW/MAX_BLOCKS)))
        
        # device info
        count = 0
        for device in stats["devices"]:
            name = device["name"]
            ip = device["ip"]
            speed = round(device["totalSpeed"] ,0)
            used = int(device["totalUsedMB"] )
            unitLoad = int(speed/(TOTAL_BW/MAX_BLOCKS))                
            count +=1
            hspeed = humanSpeedUnits(speed)
            print(f"{count} | {name} @{ip[-4:]} | {used} MB")
            print('█'*unitLoad,f"{hspeed}")

        time.sleep(WAIT_BEFORE_UPDATE)