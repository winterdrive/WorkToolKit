from os import walk
from os.path import join

# 如果要裝套件，先在terminal下這幾行命令
# py -3 -m venv .venv
# .venv\scripts\activate
# python3 -m pip install matplotlib
# python3 -m pip install pandas

# 指定要列出所有檔案的目錄
viewProjectList = [
    "C:/",
    "D:/"
]

for view in viewProjectList:
    print("--------"+view+"--------------")
    viewFileList = []
    # 遞迴列出 view 所有子目錄與檔案
    for root, dirs, files in walk(view):
        for f in files:
            fullpath = join(root, f)
            # fullpath.replace("\\","/")
            viewFileList.append(fullpath)
            # print(fullpath)
    # print (viewFileList)

    # 搜尋內容，包含內文及純unicode轉碼比對
    input_text = "你的文字"
    input_text_in_utf8 = input_text.encode('unicode_escape').decode(
        'utf-8').upper().replace(r'\U', r'\u')
    # print(input_text_in_utf8)
    errorFilePath = []
    for filePath in viewFileList:
        try:
            text = ""
            with open(filePath, "r", encoding="UTF-8")as file:
                lines = file.readlines()
                for i in lines:
                    text += i
            if (input_text in text) or (input_text_in_utf8 in text):
                print(filePath)
                # pass
        except:
            # errorFilePath.append(filePath)
            pass
    # print("errorFilePath: ",errorFilePath)
