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

#迴圈
def girlprint(name):
    print('Hi '+ name)

girls = ['nancy', 'stacey', 'tracy', 'wakaki']

for name in girls:  #設定變數name的範圍，是在girls陣列中
    girlprint(name)

# for限定次數的迴圈
for i in range(10,0, -1): 
    # 以C#來說，是類似for(int i = 1; i<=10; i--) 
    #   {
    #      console.writeLine(i);
    #     }的用法設定
    print(i)
    
# while迴圈  
# # C#就是 
#   i = 0;
 #while (i <= 10) { console.writeLiine(i); i++} 
    i = 0
    while i <= 10 :
        print(i)
        i += 1
        #上述程式會執行成 10 0~10 9 0~10 8 0~10 直到 0~10        
