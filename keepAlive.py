import time
import requests

url= "https://www.google.com/"

req = requests.get(url)
status=req.status_code        
while(True):
    if(status==200):
        print("%s connected"%time.asctime())
        time.sleep(60)
        req = requests.get(url)
        status=req.status_code
    else:
        print("failed")

# & c:/python/.venv/Scripts/python.exe c:/python/webscrapper/keepAlive.py