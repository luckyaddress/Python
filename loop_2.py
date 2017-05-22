#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

# 99乘法迴圈

for i in range(1,10,1):
    for j in range(1,10,1):
        print (str(i)+ "*" + str(j) + "=" + str(i*j))
        
# 第一層 i 每跑1次，j要跑9次，i總共要跑9次，所以可產生出99乘法表