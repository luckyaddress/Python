#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

import re           #import re 作為引入regex函式庫
pattern = '[abc]'   #設定正規式要搜尋的pattern
string = 'aAbBcC'   #搜尋字串
match_string = re.findall(pattern, string)   #設定match_string為re函式庫下findall方法的回傳字串
# 用法findall(第一字串為搜尋的pattern, 第二個為欲待分析的字串)
x = match_string
print  x     # 輸出 ['a', 'b', 'c']