#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

# 例外處理: try / except區塊
try:
    try_open = open("Exception.txt", "r")
    print(try_open.read())
    try_open.close()
except:
    print("錯誤，檔案不存在！")

# else 跟 Finally區塊
try:
    n1 = input("輸入第一個整數值 =>")
    n2 = float(input("輸入第二個整數值 =>"))  # 要用int / float才能呈現小數點
    r = n1 / n2
    print("變數r的值 = {0:2f} ".format(r))
except:
    print("錯誤:輸入的資料與運算有錯誤")
else:
    print("ELSE:輸入的資料沒有錯誤")
finally:
    print("Finally:您有輸入資料")
