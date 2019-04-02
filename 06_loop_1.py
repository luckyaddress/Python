#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

#迴圈
# for限定次數的迴圈
for i in range(5, 0, -1): 
    # 以C#來說，是類似for(int i = 1; i<=10; i--) 
    #   {
    #      console.writeLine(i);
    #     }的用法設定
    print(i)
    
# while迴圈  
# # C#就是 
#   i = 0;
# while (i <= 10) { console.writeLine(i); i++} 

# Python 要注意程式段落跟縮排問題，否則會造成執行效果差異！
i = 0
while i <= 4 :
        print(i)
        i += 1

#定義迴圈的函數

def girlprint(name):
    
    print('Hi '+ name)

girls = ['Nancy', 'Stacey', 'Tracy', 'Wakaki']

for name in girls:  #設定變數name的範圍，是在girls陣列中

    girlprint(name) #執行girlprint方法，參數是name，name範圍為girls

# 定義一個表現寵物的方法

def PetShow(x):

    print('Good ' + x)

Petname = ['Snoopy', 'Kitty', 'Doraemon', '孫悟空']

for nameforPet in Petname:
    PetShow(nameforPet)

var1 = int(input("請輸入最大值=>"))
s = 0
for i in range(1,var1+1):
    print("i = " + str(i))
    s += i
print("總和 = " + str(s))

# 條件迴圈 = while 要在條件運算中，自行處理計數器i
n = 1; r = 1
while n <= 4:
    r = n * r  
    #(n=1，r=1,跑下一行 n=1+1=2，新的r= 2*1 ＝2，新的n=2+1=3，新的r=3*2=6，n=3+1=4，而r=6，新的r= 4*6=24 故為數學階層!)
    n = n + 1
print("數學階層！ ＝ " + str(r))