#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

def Test1():
    print('Earn Money')
    print('Buy iMac')
Test1()

def Test2(x):
    print('Hi '+ x) 
    print('Hi '+ x + ' Good')
Test2('Rei')

class Cat:
    def meow(self):
        # self指向當這個類別被new起來時的那個物件
        # 只是這樣使用，每次new一個Cat物件，呼叫一次方法，就會重複創建這個方法
        print('測試類別') 
a = Cat()
a.meow()

#靜態方法，跟@classmethod方法類似，但需要new一個物件才能使用，詳如下：，
#方法內有多少參數，new出來的物件，就有多少參數。
#跟classmethod的差別在於：因為staticmethod沒有在方法中自帶自己的類別，
#所以如果在@staticmethod下，要直接使用類別中的其他屬性(變數)是無法的，等於是要在
#new一個類別物件，才能使用該類別中不屬於靜態方法中的類別屬性或方法
class dog:
    var1 = "Try staticmethod"
    @staticmethod
    def wow(x,y):
        print('wow '* x * y)
        print(dog.var1) # new一個dog出來，使用他的var1屬性
        # static靜態方法，跟C#宣告物件後使用的方法較為雷同

a = dog() #相當於new一個物件，將其實體化
a.wow(2,3)

#類別方法 
#不需要宣告一個物件，宣告類別，建立方法後即可使用！
#在classmethod的方法中，第一個參數表示類別本身，所以可以命名第一個參數為paraTest
#即是呼叫了該類別(pig)，即可使用該類別下的屬性var1
#classmethod方法中的第二個參數開始，即為函數方法的自帶參數

class pig:
    
    var1 = "Try classmethod"
    @classmethod      
    def Print3(paraTest, x, y):  
        print "print 3: "+ paraTest.var1 + x + y 

pig.Print3(" 測試", " Python的方法")

# 函數使用return

def test1(a,b):
    if a > b:
        return "好"
    else:
        return "不好"

print(test1(5,8)) # 列印函數的回傳值！

# 類別
class Cat:
    def voice(self, a, b): #self表示這個類別本身
        self.num1 = a
        self.num2 = b
        # voice方法先把 a跟b 指定給這個類別的本身self
    def meow(self):
        return self.num1 + self.num2

d = Cat()  # new一個Cat物件
d.voice(22,33)  # Cat物件下的voice方法，會將Cat.num1跟Cat.num2這兩個屬性 設定為a跟b兩個參數
print(d.meow()) # 之後meow()方法用到時，num1跟num2即會是a跟b的值 