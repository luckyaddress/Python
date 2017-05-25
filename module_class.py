#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

# 如果有多個模組要匯入，使用,號隔開
import module_example  # 匯入模組後，下方即可使用該模組的方法或變數

x = module_example.bmi_cal(1.79, 0.95)

print(x)

# Python亦可匯入內建模組,並使用別名來呼叫模組
import random
random_n = random.randint(1, 100)
import random as R
rn_2 = R.randint(20, 60)
print(random_n, rn_2)

# 僅匯入模組的部份
from module_example_2 import print_name
# import module_example_2 上面為限制模組的部份，僅使用print_name的功能
# print(module_example_2.gender)
module_example.print_name("Wakaki")
