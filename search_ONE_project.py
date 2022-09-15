from os import walk
from os.path import join
import os

# 如果要裝套件，先在terminal下這幾行命令
# py -3 -m venv .venv
# .venv\scripts\activate
# python3 -m pip install matplotlib
# python3 -m pip install pandas

# 指定要列出所有檔案的目錄
view ="你的檔案路徑"

viewFileList=[]
# 遞迴列出 view 所有子目錄與檔案
for root, dirs, files in walk(view):
  for f in files:
    fullpath = join(root, f)
    # fullpath.replace("\\","/")
    viewFileList.append(fullpath)
    # print(fullpath)
# print (viewFileList)

# 搜尋內容，包含內文及純unicode轉碼比對
input_text="你的搜尋文字(支援unicode)"
input_text_in_utf8=input_text.encode('unicode_escape').decode('utf-8').upper().replace(r'\U',r'\u')
# \u4F7F\u7528\u7D05\u5229\u5931\u6557
# print(input_text_in_utf8)
errorFilePath=[]
totalFileNumber=0
for filePath in viewFileList:
  try:
    # 大型檔案不看(2Mb)
    if(os.path.getsize(filePath)>2000000):
      # errorFilePath.append(filePath)
      pass
    else:
      text=""
      with open(filePath,"r",encoding="UTF-8")as file:
          lines = file.readlines()
          for i in lines:
              text+=i  
      # if ((input_text in text)or(input_text_in_utf8 in text))and(".gsp" in filePath):
      if ((input_text in text)or(input_text_in_utf8 in text)):
          print (filePath)
          totalFileNumber+=1
          # pass
  except:
      # errorFilePath.append(filePath)
      pass
# print("errorFilePath: ",errorFilePath)
print(totalFileNumber)