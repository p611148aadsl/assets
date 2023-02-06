import os
import requests


a="10.10.10.10 hr.geelib.qihoo.net"
with open("/etc/hosts", "a+") as f:
  f.write(a+"\n")
  
url = "https://hr.geelib.qihoo.net"
headers ={"Token": "asdfasDSAFaasdf!@#sadf"}
username = "hr-admin"
password = "testMima"
res = requests.post(url, headers = headers, verify = False, json = {"username": username, "password": password})
if res.status_code == 301:
  print("success")
else:
  print("failed")
