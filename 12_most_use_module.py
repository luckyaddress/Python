#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

# os模組 可以 刪除檔案 建立目錄 更名和刪除目錄
import os
path = os.getcwd() # 取得現在工作目錄
print(path)  

print(os.listdir(path))  # 取得路徑下的檔案 和 目錄清單

# os.mkdir("os_module_test") # 建立新目錄 如果目錄已存在，會出現目錄同名無法建立的錯誤

# os.rename("os_module_test", "omt") # 更名現有目錄

# os.rmdir("omt") # 刪除目錄

# 建立檔案 刪除檔案 因為建立後刪除 同時只能完成一個動作，否則刪除會通知找不到檔案

#file = open("aa.txt", "w")
#file.close()
#print("建立檔案:", os.listdir(path))

# 先建立，方能測試刪除
# os.remove("aa.txt")
# print("測試檔案", os.listdir(path))

# os.path模組:檢查檔案或目錄是否存在

files = (os.getcwd(), "loop_2.py")
for f in files:
    print("該項目為 = " + str(f))
    if os.path.exists(f):
        print("檔案或目錄存在")
    if os.path.isdir(f):
        print("該檔案是目錄")
    if os.path.isfile(f):
        print("該檔案是檔案")

# 數學函數與亂數 import math 或者 random
import random
r1 = random.randint(1,20)
print(str(r1))

list1 = ["apple", "orange", "strawberry", "juice", "roasted-beef"]
r2 = random.choice(list1) # choice 在清單的資料型態中任意抽選一個
print(r2)

# Python時間模組 time模組顯示時間與日期 calendar模組顯示月曆資料

import time
time_1 = time.time()
print(time_1)

localtime = time.localtime(time_1)
print("Year", localtime[0], "Month", localtime[1])
# 年月日時分秒 分別為: localtime[0]-[5]

# calendar模組 顯示指定年份和月份資料(以月曆形式顯示)
import calendar
cal = calendar.month(2017,4)
print(cal)

# 精確表示浮點數 decimal模組
import decimal
decimal.getcontext().prec = 7 # 指定小數點精確度
print(decimal.Decimal(7.6) + decimal.Decimal(8.7))

# 正規運算式 re模組 
import re
source_data = "my name is kao and email is ykk@gmail.com"
match_string = re.search(r"([\w.-]+)@([A-Za-z0-9_.-]+)", source_data)
# + 表示前面的字元可以被比較1次或多次
# + 要包在r後的""字串範圍內，否則連群組抓取都會無法正常使用
print(match_string.group())

# 群組抓取，上述的字串已經分割成群組
print(match_string.group(1))
print(match_string.group(2))

# re正規表達式的 findall()方法 --seacrh()只能找到一次，要找出所有符合的，要用findall()
source_data2 = "my name is kao and email is ykk@gmail.com, your name is wakaki and email is wakaki@gmail.com"
match_string2 = re.findall(r"([\w.-]+)@([A-Za-z0-9_.-]+)", source_data2)
print(match_string2)   # 會變成一個二維的list
print(match_string2[0][0])
print(match_string2[0][1])
print(match_string2[1][0])
print(match_string2[1][1])

