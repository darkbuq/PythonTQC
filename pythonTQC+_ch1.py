#%%
"""
TQC+ 程式語言Python 101 整數格式化輸出
請撰寫一程式，輸入四個整數，
然後將這四個整數以欄寬為5、欄與欄間隔一個空白字元，
再以每列印兩個的方式，先列印向右靠齊，
再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。


輸入說明
四個整數
輸出說明
格式化輸出

範例輸入
85
4
299
478
範例輸出
|   85     4|
|  299   478|
|85    4    |
|299   478  |
"""
a=int(input())
b=int(input())
c=int(input())
d=int(input())

print("|{:>5d} {:>5d}|".format(a,b))
print("|{:>5d} {:>5d}|".format(c,d))

print("|{:<5d} {:<5d}|".format(a,b))
print("|{:<5d} {:<5d}|".format(c,d))
#%%
"""
TQC+ 程式語言Python 102 浮點數格式化輸出
請撰寫一程式，輸入四個分別含有小數1到4位的浮點數，
然後將這四個浮點數以欄寬為7、欄與欄間隔一個空白字元、每列印兩個的方式，
先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。

提示：輸出浮點數到小數點後第二位。

輸入說明
四個浮點數
輸出說明
格式化輸出

範例輸入
23.12
395.3
100.4617
564.329
範例輸出
|  23.12  395.30|
| 100.46  564.33|
|23.12   395.30 |
|100.46  564.33 |
"""
a=eval(input())
b=eval(input())
c=eval(input())
d=eval(input())

print("|{:>7.2f} {:>7.2f}|".format(a,b))
print("|{:>7.2f} {:>7.2f}|".format(c,d))

print("|{:<7.2f} {:<7.2f}|".format(a,b))
print("|{:<7.2f} {:<7.2f}|".format(c,d))
#%%
"""
TQC+ 程式語言Python 103 字串格式化輸出
請撰寫一程式，輸入四個單字，然後將這四個單字以欄寬為10、
欄與欄間隔一個空白字元、每列印兩個的方式，先列印向右靠齊，
再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。

輸入說明
四個單字
輸出說明
格式化輸出

範例輸入
I
enjoy
learning
Python
範例輸出
|         I      enjoy|
|  learning     Python|
|I          enjoy     |
|learning   Python    |
"""
a=input()
b=input()
c=input()
d=input()

print("|{:>10s} {:>10s}|".format(a,b))
print("|{:>10s} {:>10s}|".format(c,d))

print("|{:<10s} {:<10s}|".format(a,b))
print("|{:<10s} {:<10s}|".format(c,d))
#%%
"""
TQC+ 程式語言Python 104 圓形面積計算
請撰寫一程式，輸入一圓的半徑，並加以計算此圓之面積和周長，
最後請印出此圓的半徑（Radius）、周長（Perimeter）和面積（Area）。

提示1：需import math模組，並使用math.pi。
提示2：輸出浮點數到小數點後第二位。

輸入說明
半徑
輸出說明
半徑
周長
面積

輸入輸出範例
範例輸入1
10
範例輸出1
Radius = 10.00
Perimeter = 62.83
Area = 314.16
"""
import math
r=eval(input())
print("Radius = {:.2f}".format(r))
print("Perimeter = {:.2f}".format(2*r*math.pi))
print("Area = {:.2f}".format(r*r*math.pi))
#%%





















