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

#靜態方法: 沒有預設參數，要呼叫類別中，靜態方法外的參數，像是下例中的var1
#前面要使用該類別名稱，像是new一個物件出來，進而使用他的var1屬性一樣。

class dog:
    var1 = "Try staticmethod"
    @staticmethod
    def wow(x,y):
        print('wow '* x * y)
        print(dog.var1) #  要在類別方法中 直接new一個物件dog出來，使用他的var1屬性
        # 不能夠 print(var1)


a = dog() #相當於new一個物件，將其實體化
a.wow(2,3)
# 因為 a已經是類別dog的 實體物件，所以執行wow方法，會連裡面的print(dog.var1)一起執行


#類別方法 
# 第一個參數為預設可自訂參數，例如pig_self，可以透過第一個參數來使用 類別中但是為方法外的參數var1
# 使用方式為pig_self.var1
# 不需要宣告一個物件，宣告類別，建立方法後即可使用 --> pig.Print3！
# classmethod方法中的第二個參數開始，即為函數方法的自帶參數
# 方法宣告了幾個參數，方法中即要有對應的參數數量 像是pig_self, x, y

class pig:
    var1 = "Try classmethod"
    @classmethod      
    def Print3(pig_self, x, y):  
        print "print 3: "+ pig_self.var1 + x + y  # 因為有自訂參數pig_self 所以使用var1 就比較容易

pig.Print3(" 測試", " Python的方法") # 可以不用像上面的靜態方法，仍要去new一個物件a出來

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