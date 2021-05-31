## Simple Cmd-line dashboard app for `Tenda n301 V5.07.56.1` Routers.

### Cmd-line Dashboard 
![dash](./reference/dash.gif)

### Run On Windows
`run.bat`

### Make changes in `config.py`
```python
ROUTER_IP = '192.168.0.1'
ROUTER_PASS = "admin"
TOTAL_BW = 100/8 * 1024  # KBps
MAX_BLOCKS = 32
WAIT_BEFORE_UPDATE = 1
```


### `Api`
```python
import api

resp = api.getAllStatsJson()
print(resp)
```
### Response
```json
{
  "devices":[
    {
      "ip":"192.168.0.100",
      "upKB":0.0,
      "downKB":0.0,
      "sentMsg":167908.0,
      "sentMB":26.5,
      "recievedMsg":334057.0,
      "recievedMB":351.7,
      "name":"*.100",
      "mac":"40:B0:76:71:F0:30",
      "jank":"0",
      "leaseTime":65236.0,
      "totalSpeed":0.0,
      "totalUsedMB":378.2
    },
    {
      "ip":"192.168.0.101",
      "upKB":0.0,
      "downKB":0.0,
      "sentMsg":647728.0,
      "sentMB":59.4,
      "recievedMsg":2436138.0,
      "recievedMB":3046.3,
      "name":"M2003J15SC-RedmiNote",
      "mac":"2A:52:73:F1:FE:53",
      "jank":"0",
      "leaseTime":78595.0,
      "totalSpeed":0.0,
      "totalUsedMB":3105.7000000000003
    },
    {
      "ip":"192.168.0.102",
      "upKB":0.0,
      "downKB":0.0,
      "sentMsg":229523.0,
      "sentMB":127.5,
      "recievedMsg":581197.0,
      "recievedMB":289.2,
      "name":"POCOM2Pro-POCOM2Pro",
      "mac":"E0:1F:88:23:C4:92",
      "jank":"0",
      "leaseTime":77951.0,
      "totalSpeed":0.0,
      "totalUsedMB":416.7
    },
    {
      "ip":"192.168.0.103",
      "upKB":0.9,
      "downKB":1.4,
      "sentMsg":785951.0,
      "sentMB":103.8,
      "recievedMsg":1828217.0,
      "recievedMB":619.1,
      "name":"rayanpc",
      "mac":"14:18:77:B2:69:F4",
      "jank":"0",
      "leaseTime":59495.0,
      "totalSpeed":2.3,
      "totalUsedMB":722.9
    },
    {
      "ip":"192.168.0.105",
      "upKB":0.0,
      "downKB":0.0,
      "sentMsg":156394.0,
      "sentMB":15.3,
      "recievedMsg":268227.0,
      "recievedMB":336.7,
      "name":"lg",
      "mac":"90:00:4E:91:54:5D",
      "jank":"0",
      "leaseTime":83834.0,
      "totalSpeed":0.0,
      "totalUsedMB":352.0
    },
    {
      "ip":"192.168.0.109",
      "upKB":0.0,
      "downKB":0.0,
      "sentMsg":25800.0,
      "sentMB":1.4,
      "recievedMsg":187897.0,
      "recievedMB":267.4,
      "name":"osmc",
      "mac":"B8:27:EB:DF:C9:F8",
      "jank":"0",
      "leaseTime":75189.0,
      "totalSpeed":0.0,
      "totalUsedMB":268.79999999999995
    }
  ],
  "metrics":{
    "totalDownKB":1.4,
    "totalUpKB":0.9,
    "totalSpeed":2.3,
    "totalSentMB":333.9,
    "totalRecievedMB":4910.4,
    "load":0.02,
    "totalUsedGB":5.12
  }
}
```