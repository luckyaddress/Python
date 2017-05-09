#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

def Test1():
    print('Earn Money')
    print('Buy Stock')
Test1()

def Test2(x):
    print('Hi '+ x) 
    print('Hi '+ x + ' Good')
Test2('Rei')

class Cat:
    def meow(self):
        # self指向當這個類別被new起來時的那個物件
        # 只是這樣使用，每次new一個Cat物件，呼叫一次方法，就會重複創建這個方法
        print('Fuck!') 
a = Cat()
a.meow()

class dog:
    @staticmethod
    def wow(x,y):
        print('wow'* x * y)
        # static靜態方法，跟C#宣告物件後使用的方法較為雷同

a = dog()
a.wow(2,3)

#類別方法 
#不需要宣告一個物件，宣告類別，建立方法後即可使用！
class pig:
    @classmethod
    def hoho(clz,x, y):
        print('success', x ,y)

pig.hoho(10,20)

# 函數使用return
def test1(a,b):
    if a > b:
        return "好"
    else:
        return "不好"

print(test1(5,8)) # 列印函數的回傳值！

# 類別
class Cat:
    def voice(self, a, b):
        self.a = a
        self.b = b
        # voice方法先把 a跟b指定給這個類別的本身self
    def meow(self):
        return self.a + self.b
d = Cat()
d.voice(22,33)
print(d.meow())