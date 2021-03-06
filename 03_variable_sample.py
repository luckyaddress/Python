# -*- coding: utf-8 -*-
# 使用中文註解，要加上上面那一行的編碼

x,y = 22,55
print (x)
# Python 可用上述方式進行變數之多重指定

a = 77; b = 88
print (b)
# 寫在同一行，則是用;號區隔

x,y = 33,66
x,y = y,x   # 重新指定後，x,y的值會互換
print (y)

j = 5; a = 4 + 3*j; b = 5 + 2j
print(a,b)
print(str(type(a)), str(type(b)))
# Python支援複數(complex)資料型態
# 利用type()來取得資料型態
