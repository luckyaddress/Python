#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

import re           #import re 作為引入regex函式庫 (Python的函式庫)
pattern = '[abc]'   #設定正規式要搜尋的pattern
string = 'aAbBcC'   #搜尋字串
match_string = re.findall(pattern, string)   #設定match_string為re函式庫下findall方法的回傳字串
# 用法findall(第一字串為搜尋的pattern, 第二個為欲待分析的字串)
x = match_string
print  x     # 輸出 ['a', 'b', 'c']

pattern_2 = r'ab.'   # r 表示 raw string，不做特殊處理，另外+號表示1個或1個以上的關鍵字，寫在pattern字串內 
string_2 = 'abdabxacb'
match_string_2 = re.search(pattern_2,string_2) 
# search用法跟 findall相同，第一個字串為pattern，第二個字串為比對的string字串
x_2 = match_string_2.group()
# search 要跟 group()搭配，回傳比對結果
print x_2  # search 跟 group()的搭配，只會傳回第一個比對到的值

pattern_3 = r"\.\w+"  # \. 表示 . 因為Regex中 . 表示單一任意字元
string_3 = ".abc 123 abc"
match_string_3 = re.search(pattern_3,string_3)
x_3 = match_string_3.group()
print x_3

# 另一種用法：將Pattern在re中comile，變成一個re的物件，再執行其search或findall方法
p = re.compile('[a-z]')　
m = p.findall("zljlrjuaoducomlreaf") # 執行findall方法 將字串帶入re物件(p)的方法中
print m