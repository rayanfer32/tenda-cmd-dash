import api
import json

resp = api.getAllStatsJson()
print(resp)

with open("getAllStats.json", 'w') as f:
		json.dump(resp, f)