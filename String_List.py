#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

str1 = "Test"
for e in str1:
    print(e) # 會變成迭代逐行列印str1中的各字元

# 亦可利用索引運算子[]跟重複運算子*，來列印字元
str1 = "Hello"
print(str1[1]) # 索引從0開始，故1為e
print(str1*2)

# 可以利用in 或者 not in 跟 關係運算子來進行字串比較
str2 = "HelloWakaki"
print("Wa" in str2)
print("wakaki" in str2)  # 這個 in 跟not in 有比較大小寫

"Kitty" >= "Wakaki"
