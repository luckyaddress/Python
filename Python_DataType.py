#-*- coding: utf-8 -*- 
#判斷是否為整數
print(2.00.is_integer())
print(0.025.is_integer())

# 跳脫字元\t --tab鍵
print('Hello\tJack!')
# 列印單引號或者雙引號 使用\'或\"
print('\'Hello Jack\'')
print('\"測試\"')

# 設定變數為布林值
a = True
b = False
print(a,b)

# 資料陣列
a = []
b = [1, 2, "3",[4],(5)]
print(b[3])

# 運算子
a = True
b = False
c = a and b
print(c)
x = a or b
print(x)
d = not b
print(d)

# 算術運算子
a = 5
b = a + 3
print(b)
b = a * 3
print(b)
b = a/5
print(b)
b = a - 2
print(b)
b = a % 2 
print(b)
b = a ** 2
print(b)

# 函數使用return
def test1(a,b):
    if a > b:
        return "好"
    else:
        return "不好"

print(test1(5,8)) # 列印函數的回傳值！

# 類別
class Cat:
    def voice(self, a, b):
        self.a = a
        self.b = b
        # voice方法先把 a跟b指定給這個類別的本身self
    def meow(self):
        return self.a + self.b
d = Cat()
d.voice(22,33)
print(d.meow())