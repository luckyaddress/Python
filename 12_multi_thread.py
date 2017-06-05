#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼
# Threads 又稱為輕量行程 Lightweight Process

# 建立多執行緒的Python程式
import threading, time, random
def display(name, num):
    i = 1
    while True:
        time.sleep(random.randint(1, 3))
        print(name + str(num) + " =", i)
        i +=1
    
thread1 = threading.Thread(target=display, args=("執行緒",1))
thread1.start()
thread2 = threading.Thread(target=display, args=("執行緒",2))
thread2.start()