import requests
import sys
import requests
import shutil

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)
  
if __name__ == '__main__':
    text=sys.argv[1]+" just pushed a commit and finished the build job ! \nCheck it on："+sys.argv[2]
    total, used, free = shutil.disk_usage("/")
    if (used/total)>0.4:
        text=text+"\n"+"-----------------------"+"\n"+"【Alert!】"+"\n"+("Disk usage: ")+str(round((used/total)*100,2))+"%"+"\n"+("Total size: %d GiB" % (total // (2**30)))+"\n"+("Used: %d GiB" % (used // (2**30)))+"\n"+("Free size: %d GiB" % (free // (2**30)))
    print(text)

    TOKEN="XXXXXXXXXXXXXXXXXXXXXXXXXX"
    headers = { "Authorization": "Bearer " + TOKEN }
    data = { 'message': text }
    requests.post("https://notify-api.line.me/api/notify",
        headers = headers, data = data)

