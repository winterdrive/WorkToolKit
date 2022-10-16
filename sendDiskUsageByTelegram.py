import requests
import shutil

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)
  
total, used, free = shutil.disk_usage("/")
text="【Alert!】"+"\n"+("Disk usage: ")+str(round((used/total)*100,2))+"%"+"\n"+("Total size: %d GiB" % (total // (2**30)))+"\n"+("Used: %d GiB" % (used // (2**30)))+"\n"+("Free size: %d GiB" % (free // (2**30)))
TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
CHATID="YYYYYYYYYYYYYY"

url = f"https://api.telegram.org/bot{TOKEN}"
params = {"chat_id": CHATID, "text": text}

req = requests.get(url + "/sendMessage", params=params)