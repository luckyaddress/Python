#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

a = 2; b = 3
c = a**b
print(c)
# ** 為指數運算子

x = 2; y = 7
z = y / float(x)
p = y // float(x)
print(z,p)
# /顯示除數，不顯示餘數，而python中整數除以整數，只會顯示整數。(此例會顯示3)
# 所以先將其中一個改成浮點數
# //顯示整數形式的除數  

a = 6.0 + 8
b = 5 + 3.79
print(a, b)

# 算術運算子建立數學公式
f = int(input("請輸入華式溫度=>"))
c = (5.0 / 9.0) * (f - 32.0)
print("攝氏溫度為:" + str(c))

