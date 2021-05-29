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
```
[
  {
    "ip":"192.168.0.100",
    "upKB":1.0,
    "downKB":0.5,
    "sentMsg":674604.0,
    "sentMB":69.3,
    "recievedMsg":2624653.0,
    "recievedMB":2967.6,
    "name":"M2003J15SC-RedmiNote",
    "mac":"2A:52:73:F1:FE:53",
    "jank":"0",
    "leaseTime":86320.0
  },
  {
    "ip":"192.168.0.104",
    "upKB":0.0,
    "downKB":0.0,
    "sentMsg":147101.0,
    "sentMB":103.4,
    "recievedMsg":218875.0,
    "recievedMB":246.5,
    "name":"POCOM2Pro-POCOM2Pro",
    "mac":"E0:1F:88:23:C4:92",
    "jank":"0",
    "leaseTime":78473.0
  },
  {
    "ip":"192.168.0.105",
    "upKB":0.0,
    "downKB":0.0,
    "sentMsg":574971.0,
    "sentMB":41.3,
    "recievedMsg":1349381.0,
    "recievedMB":1347.9,
    "name":"lg",
    "mac":"90:00:4E:91:54:5D",
    "jank":"0",
    "leaseTime":74266.0
  },
  {
    "metrics":{
      "totalDownKB":1.4,
      "totalUpKB":1.0,
      "totalSpeed":2.4,
      "totalSentMB":4186.0,
      "totalRecievedMB":14137.2,
      "load":0.02,
      "totalUsedGB":17.89
    }
  }
]
```
