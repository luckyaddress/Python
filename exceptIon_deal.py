#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

# 例外處理: try / except區塊
try:
    try_open = open("Exception.txt", "r")
    print(try_open.read())
    try_open.close()
except:
    print("錯誤，檔案不存在！")

# 同時處理多種例外
