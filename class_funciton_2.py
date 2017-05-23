#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

# 最簡單的函數，沒有引數，沒有回傳值
def function_test():
    print("函數測試")

function_test() # 呼叫函數，並執行

def sum_to_ten():
    s,i = 0,0  # s跟i 起始值皆為0
    for i in range(1,11):
        s += i
    print("1 加到 10 ＝" + str(s))

sum_to_ten()

# 將上述函數，改成帶有相關參數的引數
def sum_to_summary(start, end):
    s, i = 0,0
    for i in range(start, end+1): # 要包含end值，在range函數的話，要加1
        s += i
    print ("從" + str(start) + "加到" + str(end) + "＝" + str(s))

sum_to_summary(1,100)
