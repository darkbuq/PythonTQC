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
































