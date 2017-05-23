#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

# 討論元組 字典 集合
# 元組(turple)，使用()建立，各項目使用,隔開，各項目無法像list一樣變更
turple1 = () # 空turple
turple2 = (1, "2", 3, "test", 4.1782)
print(turple2)

# turple 一樣可以用索引跟迴圈走訪

for i in turple2:
    print(str(i))

print(turple2[3])

# turple 一樣可使用 + * in not in等運算子 包含切割
turple3 = turple2[2:4]
print(turple3)

# 元組函數 元組方法 len() sum() sorted() 方法: count()，跟list相同
print(sorted(turple2)) # 因為2是字串

t3 = (1, 1, "a", "a", "n", "c", 3, 5,)
print(t3.count("a"))

#Dict 字典檔案型態類型
