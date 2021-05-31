import os

def clearScreen():
    os.system("cls")

def pauseScreen():
    os.system("pause")

def humanSpeedUnits(kbps):
    if(kbps > 1000):
        return f"{round(kbps/1000, 2)} MBps"
    else:
        return f"{kbps} KBps"