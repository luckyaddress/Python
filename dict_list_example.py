#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

d1 = {"name":"Rei", "sex":"male",  "weight":75}  # 宣告一個dict
print (d1["name"]) # dict使用key當作index

d1["CATEGORIES"]="OLIS"  # 新增一筆key:value 紀錄
print (d1)

d2 = {1:"a", 2:"b"}
print (d2[1])

# key值 限定為 字串 或 數字，value則沒有限制
