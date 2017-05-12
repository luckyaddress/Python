#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

d1 = {"name":"Rei", "sex":"male",  "weight":75}  # 宣告一個dict
print (d1["name"]) # dict使用key當作index

d1["CATEGORIES"]="圖資處"  # 新增一筆key:value 紀錄
# 如果要列印 串列或 Dict類別的 中文，請參考下列用法
print (str(d1).decode('string_escape'))

d2 = {1:"a", 2:"b"}
print (d2[1])

# key值 限定為 字串 或 數字，value則沒有限制

# 串列 List
List1 = ["name:Rei", "性別:男", "weight:175"]
print (List1[0])
a = "rei@yahoo.com"
b = "test@google.com"
List1.insert(3,"群組:"+ a + " " + b)
# 如果要列印 串列或 Dict類別的 中文，請參考下列用法
print (str(List1).decode('string_escape'))