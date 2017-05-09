#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

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
