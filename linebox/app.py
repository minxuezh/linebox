# print("Hello")

# result=0
# n=1
# while n<=10:
#     result+=n
#     n+=1
# print(result)
# for迴圈
# for變數in列表
# result=0
# for n in [5,7,2]:
#     result+=n
# print(result)
# function函式
# def test(n1,n2):
#     return n1+n2
# result=test(3,4)
# print(result)
# read the file
# file=open("data.txt", mode="r")
# data=file.read()
# file.close()
# print(data)



import json
file = open("data.txt", mode ="r", encoding ="utf-8")
data =json.load(file)
file.close()
#flask
from flask import * #載入 flask 模組
app=Flask("My Website") # 建立一個網站應用程式物件
#網站的網址:http://主機名稱/路徑?參數名稱=資料&參數名稱=資料&...
#例如:http://127.0.0.1:5000/
@app.route("/")# 指定對應的網址路徑
def home(): # 對應的處理函式
    return "<h3>Hello Flask</h3><div>This is line 1</div><script>alert('Hello');</script>"  # 回應給前端的訊息

#例如:http://127.0.0.1:5000/test.php?keyword=關鍵字
@app.route("/test.php")# 指定對應的網址路徑
def test(): # 對應的處理函式
    # 取得網址列上的參數:request.args.get(參數名稱, 預設值)
    keyword=request.args.get("keyword", None)
    if keyword==None:
        return redirect("/") #導向到路徑 /
    else:
        if keyword in data:
            return "中文 "+data[keyword]
        else:
            return "沒有翻譯"

app.run() # 啟動伺服器
