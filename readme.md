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

{
	"devices":[
		{
			"ip":"192.168.0.103",
			"upKB":0.0,
			"downKB":0.1,
			"sentMsg":2241.0,
			"sentMB":0.2,
			"recievedMsg":5238.0,
			"recievedMB":5.7,
			"name":"rayanpc",
			"mac":"14:18:77:B2:69:F4",
			"jank":"0",
			"leaseTime":86125.0
		},
		{
			"ip":"192.168.0.109",
			"upKB":0.0,
			"downKB":0.0,
			"sentMsg":5747.0,
			"sentMB":0.3,
			"recievedMsg":63859.0,
			"recievedMB":90.3,
			"name":"osmc",
			"mac":"B8:27:EB:DF:C9:F8",
			"jank":"0",
			"leaseTime":85421.0
		}
	],
	"metrics":{
		"totalDownKB":29.3,
		"totalUpKB":3.2,
		"totalSpeed":32.5,
		"totalSentMB":25.6,
		"totalRecievedMB":1013.9,
		"load":0.25,
		"totalUsedGB":1.02
	}
}