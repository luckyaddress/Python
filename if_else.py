#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼
if 2 <= 5:
    print('True')
else:
    print('False')

if 2 < 5:
    print('Get')
elif 2 > 5:
    print('Shit')
else:
    print('False')


t = float(input("請輸入今天氣溫=>"))
if t > 20 and t < 22:
    print("請加件薄外套吧")
elif t < 20:
    print("請加件厚重的外套")

score = int(input("請輸入成績分數=>"))
if score > 60:
    print("恭喜通過考試")
else:
    print("未通過")

# 多選一條件敘述

a = 40

if a > 30:
    print("產率達成")
elif a >25:
    print("產率有待加強")
else:
    print("產率不足")