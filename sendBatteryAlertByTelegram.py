import requests
import psutil
import time
  

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)
  

battery = psutil.sensors_battery()
text="Battery percentage : "+str(battery.percent)+"\n"+"Power plugged in : "+ str(battery.power_plugged)+"\n"+"Battery left : "+ str(convertTime(battery.secsleft))
TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
CHATID="YYYYYYYYYYYYY"

url = f"https://api.telegram.org/bot{TOKEN}"
params = {"chat_id": CHATID, "text": text}

while(True):
    if(battery.percent>50):
        print("battery remain "+str(battery.percent)+"%")
        req = requests.get(url + "/sendMessage", params=params)
        time.sleep(300)
