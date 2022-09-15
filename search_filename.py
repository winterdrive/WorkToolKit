from os import walk
from os.path import join

# linux有實作了
# https://blog.gtwang.org/linux/linux-grep-command-tutorial-examples/
# "grep -r ubuntu /etc/"

# 如果要裝套件，先在terminal下這幾行命令
# py -3 -m venv .venv
# .venv\scripts\activate
# python3 -m pip install matplotlib
# python3 -m pip install pandas

# 指定要列出所有檔案的目錄
view ="C:/"

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
input_text="指定檔名(如:.副檔名)"
input_text_in_utf8=input_text.encode('unicode_escape').decode('utf-8').upper().replace(r'\U',r'\u')
# \u4F7F\u7528\u7D05\u5229\u5931\u6557
# print(input_text_in_utf8)
errorFilePath=[]
for filePath in viewFileList:
  try:
    if (input_text in filePath)or(input_text_in_utf8 in filePath):
        print (filePath)
        # pass
  except:
      # errorFilePath.append(filePath)
      pass
# print("errorFilePath: ",errorFilePath)