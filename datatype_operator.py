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

print ("計算結果 ＝ " + str(100))
# Python為強型別語言，需要手動進行資料型態轉換

# Python中多個程式敘述，使用;號做區隔
a = 20; b = 30; c = 150
print (a*b/c)

str(), # 轉換成字串
int(), # 轉換成整數
float() # 轉換成浮點小數

a = 1
print(type(a))
b = str(a)
print(type(b))
c = 1.0
print(type(c))


