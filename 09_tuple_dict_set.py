#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

# 討論元組 字典 集合
# 元組(turple)，使用()建立，各項目使用,隔開，各項目無法像list一樣變更
turple1 = () # 空turple
turple2 = (1, "2", 3, "test", 4.1782)
print(turple2)

# turple 一樣可以用索引跟迴圈走訪

for i in turple2:
    print(str(i))

print(turple2[3])

# turple 一樣可使用 + * in not in等運算子 包含切割
turple3 = turple2[2:4]
print(turple3)

# 元組函數 元組方法 len() sum() sorted() 方法: count()，跟list相同
print(sorted(turple2)) # 因為2是字串

t3 = (1, 1, "a", "a", "n", "c", 3, 5,)
print(t3.count("a"))

# Dict 字典檔案型態類型 屬於Key Value的資料型態
# 字典的檔案型態 為用{}組成，內部項目用,號隔開 另外Key Value值中間用:號區隔
d1 = {1:"apple", 2:"banana", 3:"orange"}
print(type(d1), d1)

# 字典檔的 新增 取出 修改 與取用
# 取用
print(d1[2])
# 修改
d1[2] = "pineapple"
print(d1)
# 指定敘述可用於新增
d1[4] = "banana"
print(d1)

# 迴圈取用
for key in d1:
    print(d1[key])

# 刪除Dict字典檔案型態中的項目
del d1[2]
print(d1)
d1.pop(4) # 刪除並回傳值
print(d1)

# 一次清除全部Dict檔案的所有項目: clear()
d1.clear()
print(d1) # 會顯示{} 表示所有項目已清空，為空集合

d2 = {"Tom":1, "John":2, "Arthur":3, "Lexus":4}
d3 = {"Maggie":1, "May":2, "Betty":3, "Wakaki":4}
print("John" in d2) # 比對Key值
print("Maggie" not in d3)

print(d2 != d3)

# 字典函數跟字典方法 函數:len() dict() sorted() 方法: pop() clear() get() keys() value()
print(d2.keys()) # 傳回所有的Key值,並協助排序
print(d2.values()) # 傳回所有的Value值,並協助排序
print(d2.get("John")) # 用法有點像是 d2["John"]


# Set集合: 無順序的元素集合，每個元素為唯一，使用{}來建立，每個項目使用,號區隔
s1 = {1,"Hello", 3.45}
print(s1)

for i in s1:
    print(i) # 走訪集合中每一個項目

# 新增(add) 更改(update) 刪除(discard, remove, pop, clear) 集合內的元素 
s1.add("Kitty")
print(s1)
s1.update([8, 7, 6])
print(s1)

s1.discard(6) # discard() 參數要帶入集合中要刪除的那一個值，而非索引值
print(s1)
s1.remove(7) #  remove() 參數要帶入集合中要刪除的那一個值，而非索引值，若找不到該值，會回報錯誤
print(s1) 


# 集合的 交互運算
A = {1, 3, 5, 7, 9}
B = {1, 2, 5, 6, 8}
C = A.intersection(B) # A交集B 或者 A & B
D = A.union(B) # A聯集B 或者 A | B
print(C,D) 

E = A.difference(B) # A差集B 或者 A-B (單看A的部份)
F = A.symmetric_difference(B) # A對稱差集B 或者 A ^ B (A跟B一起看)

print(E,F)

# 快速建立清單跟字典檔案格式的  清單包含與字典包含

list1 = [x for x in range(1,10,2) if x % 3 == 0] # 清單包含
print(list1)

dict1 = {x:x**3 for x in range(1,5)}
print(dict1)  # 字典包含 **+數字 表示幾次方

# 格式化字串 使用format() 跟 \逸出字元
# format() 是使用範本字串來建立輸出字串內容，並且使用{}建立格式碼
x,y,z = 10,15,25
s = "Y={a} X={b} Z={c}".format(a=z, b=x, c=y)
print(s) # a b c 一般預設為索引值

# {} 格式碼 - 引數:[寬度.精準度][型態字元]
print("整數: {0:5d}".format(123) ) 
# 引數0 表示第一個位置 5d是指寬度為5位數(不足預設補空白)，d為整數,f為浮點數 s為字串
# b,o,x 為 二進位 八進位 十六進位
print("整數: {0:05d}".format(123)) # 05d表示為5位數，但不足要左側補0

#以下為浮點數範例
print("浮點數:{0:3d} 跟 {1:2.3f}".format(123, 12.31))