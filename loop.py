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
# while (i <= 10) { console.writeLiine(i); i++} 

# Python 
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