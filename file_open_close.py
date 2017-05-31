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