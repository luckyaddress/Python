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



