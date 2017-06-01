#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼
python_file = open("Python_test.txt", "r") 
# 同一個資料夾下的路徑，不用加上\
# a 是新增資料，w是清除檔案內容，新增資料 要讀取檔案 後續參數只能使用r
# python_file.write("測試加入第一行\n")
# python_file.write("測試加入第二行\n")

# python_file.close()

str1 = python_file.read()
print("以下列印檔案內容")
print(str1)

fp = open("Python_test.txt", "r") 
line1 =  fp.readlines()  # 將開啟的檔案內容，逐行變成一個list的資料型態
print("以下為逐行列印檔案內容")
for x in line1:
    print(x)


fp2 = open("Python_test.txt", "r")
str2 = fp2.read(9) # read中的參數，可限制讀取多少字元
print(str2)

fp3 = open("Python_test.txt", "r")
for line2 in fp3:
    print(line2)  # 使用for迴圈來讀取每一行

# 二進位檔案讀寫 並非內建，，需要import pickle模組
import pickle
fp_b = open ("note.dat", "wb") # 二進位要加上一個b, 讀取是rb
# 二進位檔案寫入 執行完後資料夾下會產生二進位檔 note.dat
pickle.dump("第一行測試", fp_b)
pickle.dump(2, fp_b)
pickle.dump([4,5,6,7], fp_b)
fp_b.close()

