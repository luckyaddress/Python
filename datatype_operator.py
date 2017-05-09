#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

#判斷是否為整數
print(2.00.is_integer())
print(0.025.is_integer())

# 跳脫字元\t --tab鍵
print('Hello\tJack!')
# 列印單引號或者雙引號 使用\'或\"
print('\'單引號\'')
print('\"雙引號\"')

# 設定變數為布林值
a = True
b = False
print(a,b)

# 資料陣列
a = []
b = [1, 2, "3",[4],(5)]
print(b[3])

# 運算子
a = True
b = False
c = a and b
print(c)
x = a or b
print(x)

d = not b
print(d)

# 算術運算子
a = 5
b = a + 3
print(b)

b = a * 3
print(b)

b = a/5
print(b)

b = a - 2
print(b)

b = a % 2 
print(b)

b = a ** 2
print(b)