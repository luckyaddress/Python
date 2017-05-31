#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼
python_file = open("Python_test.txt", "a")
# 同一個資料夾下的路徑，不用加上\
# a 是新增資料，w是清除檔案內容，新增資料
python_file.write("測試加入第一行\n")
python_file.write("測試加入第二行\n")


# python_file.close()

