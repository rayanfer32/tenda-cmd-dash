import api
import json

import requests

session = requests.Session() 

url = "http://192.168.0.1/login.asp"
headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
	"Origin": "http://192.168.0.1",
	"Referer" : "http://192.168.0.1/login.asp",
	"Sec-GPC" : '1',
	"Connection": "keep-alive",
	"Content-Length" :"34",
	"Cache-Control": "max-age=0",
	"Content-Type": "application/x-www-form-urlencoded",
	"Upgrade-Insecure-Requests": "1",
	"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}

headers = {"content-type":"text/plain",
"pragma":"no-cache"}

payload = {'Username':'admin', "Password": "YWRtaW4="}
r = requests.post(url, data = payload)

# print(r.content)
print(r.cookies.items())
with open("index.asp", "wb") as f:
    f.write(r.content)



# resp = api.getAllStatsJson()
# print(resp)

# with open("./reference/getAllStats.json", 'w') as f:
# 		json.dump(resp, f)