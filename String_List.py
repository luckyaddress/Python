#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

str1 = "Test"
for e in str1:
    print(e) # 會變成迭代逐行列印str1中的各字元

# 亦可利用索引運算子[]跟重複運算子*，來列印字元
str1 = "Hello"
print(str1[1]) # 索引從0開始，故1為e
print(str1*2)

# 索引運算子 可用於切割字串
print(str1[1:3])  # end端點不包含

# 可以利用in 或者 not in 跟 關係運算子來進行字串比較
str2 = "HelloWakaki"
print("Wa" in str2)
print("wakaki" in str2)  # 這個 in 跟not in 有比較大小寫

print("Kitty" <= "Wakaki")

# 字串函數 字串方法 轉換字串方法 

print(len("Hello")) # 傳回字串長度
print(max("HELLOWAKAKI")) # 如果有小寫字母，以小寫字母為主排序
print("HELLO".isupper()) # 檢測字串是否均為大寫的方法
print("banana".count("a")) # 搜尋子字串的方法
print("bxnxnx".replace("x" ,"a")) # 將x取代為a的方法，並輸出

# List 清單的物件型態，可新增 刪除 插入 更改內部項目
# 用[]括起來，用,號分開，並且可容納不同資料型態

list1 = [1, "2", [3, 4 , 5]] # list具有巢狀之功能
print(list1)

# 使用巢狀清單中之資料
print(list1[2][2]) # 會列印出5
list1[1] = "wakaki" # 重新指派修改
print(list1)

# 新增 刪除 list資料
list2 = [1, 2, [3, 4, 5], 6, 7, 8]
list2.append(9) # 在最後一個位置加入一個
list2.extend([10, 11, 12]) # 在最後的位置一次加入多個
list2.insert(0, "x") # 第一個引數為索引值，第二個引數為插入內容 
print(list2)
# 刪除可用 del pop() remove()
del list2[10] # 測試刪除最後一個
print(list2) 
list2.pop(0) # pop() 如果之中沒有引數，預設會刪除最後一個並回傳，如果有引數，則刪除引數所給予的索引位置
print(list2) # 到此處，list2已刪除 x 跟 12
list2.remove(9) # 刪除引數所代表的項目，此處的index = 9 實際上是原本的7，但已經刪除2個，所以index有變動
print(list2)

# 清單運算子 包含 + * 以及 in not in 判斷，另外，同樣地可使用切割運算子
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(list1[3:7])

# 清單函數 len(), list(), sorted()
list3 = [7, 3, 8, 5, 9, 0, 1]
print(len(list3), sorted(list3))
str1 = str(123456)
print(list(str1)) #將字串 集合 元組等轉換回list

# 切割字串成為清單
str1 = "This is a book that I like"
list1 = str1.split()
print(list1)
str2 = "Email:xxx@kmu.edu.tw \nName:高煜凱"
list2 = str(str2.splitlines()).decode('string_escape')
print(list2)
