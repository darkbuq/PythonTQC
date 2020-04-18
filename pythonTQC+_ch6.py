#%%
"""
TQC+ 程式語言Python 601 偶數索引值加總
請撰寫一程式，利用一維串列存放使用者輸入的12個正整數（範圍1~99）。
顯示這些數字，接著將串列索引為偶數的數字相加並輸出結果。

提示：輸出每一個數字欄寬設定為3，每3個一列，靠右對齊。

輸入說明
12個正整數（範圍1~99）
輸出說明
格式化輸出12個正整數
12個數字中，索引為偶數的數字相加總合

範例輸入
56
45
43
22
3
1
39
20
93
18
44
83
範例輸出
 56 45 43
 22  3  1
 39 20 93
 18 44 83
278
"""
# x=int(input())
ll=[]
summ=0
for i in range(12):
    x=int(input())
    ll.append(x)
    if i%2==0:
        summ=summ+x
for j in range(0,12,3):
    print('{:>3d}{:>3d}{:>3d}'.format(ll[j],ll[j+1],ll[j+2]))
print(summ)
#%%
"""
TQC+ 程式語言Python 602 撲克牌總和
請撰寫一程式，讓使用者輸入52張牌中的5張，計算並輸出其總和。
提示：J、Q、K以及A分別代表11、12、13以及1。

輸入說明
5張牌數
輸出說明
5張牌的數值總和

範例輸入
5
10
K
3
A
範例輸出
32
"""
ll=[]
for i in range(5):
    x=input()
    if x=='A':
        ll.append(1)
    elif x=='K':
        ll.append(13)
    elif x=='Q':
        ll.append(12)
    elif x=='J':
        ll.append(11)
    else:
        ll.append(int(x))
print(sum(ll))
#%%
"""
TQC+ 程式語言Python 603 數字排序
請撰寫一程式，要求使用者輸入十個數字並存放在串列中。
接著由大到小的順序顯示最大的3個數字。

輸入說明
十個數字
輸出說明
由大到小排序，顯示最大的3個數字

範例輸入1
40
32
12
29
20
19
38
48
57
44
範例輸出1
57 48 44
"""
ll=[]
for i in range(10):
    x=int(input())
    ll.append(x)
print(sorted(ll)[-1],sorted(ll)[-2],sorted(ll)[-3])
#%%
"""
TQC+ 程式語言Python 604 眾數
請撰寫一程式，讓使用者輸入十個整數作為樣本數，
輸出眾數（樣本中出現最多次的數字）及其出現的次數。
提示：假設樣本中只有一個眾數。

輸入說明
十個整數
輸出說明
眾數
眾數出現的次數

範例輸入
34
18
22
32
18
29
30
38
42
18
範例輸出
18
3
"""
import numpy as np
# ll=[34,18,22,32,18,29,30,38,42,18]
ll=[]
for i in range(10):
    x=int(input())
    ll.append(x)

ll2=list(np.unique(ll))
ll3=[]
for j in range(len(ll2)):
    ll3.append(ll.count(ll2[j]))

print(ll2[ll3.index(max(ll3))])
print(max(ll3))
#%%























