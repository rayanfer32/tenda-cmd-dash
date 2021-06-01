import api
import json


resp = api.getAllStatsJson()
print(resp)

with open("./reference/getAllStats.json", 'w') as f:
		json.dump(resp, f)