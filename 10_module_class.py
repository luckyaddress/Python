#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

# 如果有多個模組要匯入，使用,號隔開
import import_10_module_example  # 匯入模組後，下方即可使用該模組的方法或變數

x = import_10_module_example.bmi_cal(1.79, 0.95)

print(x)

# Python亦可匯入內建模組,並使用別名來呼叫模組
import random
random_n = random.randint(1, 100) #randint(a,b) 從a跟b之間隨機取一整數
import random as R
rn_2 = R.randint(20, 60)
print(random_n, rn_2)

# 僅匯入模組的部份
from import_10_module_example_2 import print_name
# import module_example_2 上面為限制模組的部份，僅使用print_name的功能
# print(module_example_2.gender)
import_10_module_example.print_name("Wakaki")

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

# 類別繼承 要調整

# 父類別
class papa(object):  # 父類別要先繼承object的類別，才能給予他人繼承
    def __init__(self, name):
        self.name = name
        print(name)
    def setName(self, new_name):
        self.name = new_name
        print(new_name)

p1 = papa("爸爸")
p1.setName("乾爹")
    
# 子類別
class  child(papa): # 繼承自papa
    def __init__(self, name, color): # 繼承而來的變數只有一個name, 到子類別自己多一個變數color
        super(child, self).__init__(name) # super()內部是子類別，呼叫父類別的屬性並初始化
        self.color = color  # 初始化子類別的屬性及相關方法
        print(color)
    
    def setColor(self, name, new_color):  # 設定一個新方法，繼承父類別，並且可更改子類別的屬性
        super(child, self).__init__(name)
        self.color = new_color
        print(new_color) 

    def setName(self, name, color, height):
        self.name = name
        self.color = color
        self.height = height
        print(name, color, height)

c1 = child("小孩", "黃皮膚")
c1.setName("MaMa", "White", "188") 
# 繼承自父類別的方法，原先只能有一個引數，但可以用成同名方法，此時
# 呼叫的會是子類別自己的方法，而非父類別的一個引數的方法

c1.setColor("孫孫子", "黑人") #繼承父類別的方法，並且使用子類別的方法


# 檢查物件所屬類別 使用isinstance()來檢查物件所屬類別

b = isinstance(c1,child)
c = isinstance(c1,papa) # 因為有繼承關係 所以子是由父類別生
d = isinstance(p1,child) # 子不可能生出父類別
e = isinstance(p1,papa)
print(b, c, d, e)
