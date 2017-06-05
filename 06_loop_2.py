#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

# 99乘法迴圈

for i in range(1,10,1):
    for j in range(1,10,1):
        print (str(i)+ "*" + str(j) + "=" + str(i*j))

# 第一層 i 每跑1次，j要跑9次，i總共要跑9次，所以可產生出99乘法表

# 終止跟繼續迴圈 一樣使用break跟continue
a = 0
while True:
    print(str(a))
    a += 1
    if a > 5:
        break
# continue介紹
for i in range(1,7):
    if (i%2) == 1:
        continue   # 要繼續以下程式，要整除於2
    print(str(i))

# 迴圈當中，亦可使用if/else 條件判斷，進而組成一個猜數字遊戲
 
target = 41; guess = 1
while True:
    guess = int(input("請輸入猜測的數字=>"))
    if guess == target:
        break
    elif guess > target:
        print("數字太大，請重新輸入")
    else:
        print("數字太小，請重新輸入")
print("恭喜你，猜中了")