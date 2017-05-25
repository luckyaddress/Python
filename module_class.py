#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

# 如果有多個模組要匯入，使用,號隔開
import module_example  # 匯入模組後，下方即可使用該模組的方法或變數

x = module_example.bmi_cal(1.79, 0.95)

print(x)

# Python亦可匯入內建模組,並使用別名來呼叫模組
import random
random_n = random.randint(1, 100)
import random as R
rn_2 = R.randint(20, 60)
print(random_n, rn_2)

# 僅匯入模組的部份
from module_example_2 import print_name
# import module_example_2 上面為限制模組的部份，僅使用print_name的功能
# print(module_example_2.gender)
module_example.print_name("Wakaki")

# 物件導向 物件與類別
# 定義類別
class student:
    def __init__(self, name, grade, gender): # 類別建構子，可用來建立類別中的物件屬性
        self.name = name
        self.grade =  grade
        self.gender = gender
    def displayGrade(self):
        print("學生姓名"+ self.name)
        print("分數成績"+ str(self.grade))
        print("學生性別"+ self.gender)

# 建立一個 student的範例物件
s1 = student("Wakaki", 98, "female")
s1.displayGrade() #直接執行s1物件下的displayGrade方法
print(s1.grade)

# public類別 或 private類別
class student2:
    def __init__(self, name, grade, gender):
        self.name = name
        self.grade = grade
        self.__gender = gender # private 屬性 

    def __getGender(self):
        return self.__gender # 在self.之後加上__屬性或方法名，表示private屬性或方法
 
    def output_Gender(self):
        print("學生性別" + str(self.__getGender()))


s2 = student2("Yukai", 88, "male")
s2.output_Gender()
print(s2.name, s2.grade)  
# 無法直接叫用s2.gender會出現 
# AttributeError: student2 instance has no attribute 'gender'

# 類別繼承

