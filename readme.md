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
      "sentMsg":371596.0,
      "sentMB":26.8,
      "recievedMsg":675509.0,
      "recievedMB":978.4,
      "name":"M2003J15SC-RedmiNote",
      "mac":"2A:52:73:F1:FE:53",
      "jank":"0",
      "leaseTime":76994.0,
      "totalSpeed":0.0
    },
    {
      "ip":"192.168.0.101",
      "upKB":0.0,
      "downKB":0.0,
      "sentMsg":8464.0,
      "sentMB":1.8,
      "recievedMsg":33052.0,
      "recievedMB":41.2,
      "name":"M2006C3MI-POCOC3",
      "mac":"9C:28:F7:C6:47:AA",
      "jank":"0",
      "leaseTime":80405.0,
      "totalSpeed":0.0
    },
    {
      "ip":"192.168.0.102",
      "upKB":0.0,
      "downKB":0.0,
      "sentMsg":6002.0,
      "sentMB":1.1,
      "recievedMsg":19956.0,
      "recievedMB":24.6,
      "name":"192.168.0.102",
      "mac":"40:B0:76:71:F0:30",
      "jank":"0",
      "leaseTime":85073.0,
      "totalSpeed":0.0
    },
    {
      "ip":"192.168.0.103",
      "upKB":1.0,
      "downKB":4.2,
      "sentMsg":668554.0,
      "sentMB":763.7,
      "recievedMsg":697003.0,
      "recievedMB":660.6,
      "name":"rayanpc",
      "mac":"14:18:77:B2:69:F4",
      "jank":"0",
      "leaseTime":83596.0,
      "totalSpeed":5.2
    },
    {
      "ip":"192.168.0.105",
      "upKB":2.6,
      "downKB":130.5,
      "sentMsg":39783.0,
      "sentMB":2.1,
      "recievedMsg":72828.0,
      "recievedMB":104.1,
      "name":"lg",
      "mac":"90:00:4E:91:54:5D",
      "jank":"0",
      "leaseTime":85208.0,
      "totalSpeed":133.1
    },
    {
      "ip":"192.168.0.109",
      "upKB":0.0,
      "downKB":0.0,
      "sentMsg":5839.0,
      "sentMB":0.3,
      "recievedMsg":64048.0,
      "recievedMB":90.3,
      "name":"osmc",
      "mac":"B8:27:EB:DF:C9:F8",
      "jank":"0",
      "leaseTime":82892.0,
      "totalSpeed":0.0
    }
  ],
  "metrics":{
    "totalDownKB":134.7,
    "totalUpKB":3.6,
    "totalSpeed":138.3,
    "totalSentMB":795.8,
    "totalRecievedMB":1899.2,
    "load":1.08,
    "totalUsedGB":2.63
  }
}
```