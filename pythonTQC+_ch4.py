# -*- coding: utf-8 -*-
"""
TQC+ 程式語言Python 401 最小值
請撰寫一程式，由使用者輸入十個數字，然後找出其最小值，最後輸出最小值。

輸入說明
十個數值
輸出說明
十個數值中的最小值
"""
ll=[]
for i in range(10):
    x=eval(input())
    ll.append(x)
print(min(ll))
#%%
"""
TQC+ 程式語言Python 402 不定數迴圈-最小值
請撰寫一程式，讓使用者輸入數字，輸入的動作直到輸入值為9999才結束，
然後找出其最小值，並輸出最小值。

輸入說明
n個數值，直至9999結束輸入
輸出說明
n個數值中的最小值
"""
ll=[]
x=0
while x!=9999:
    x=int(input())
    ll.append(x)
print(min(ll))
#%%
"""
TQC+ 程式語言Python 403 倍數總和計算
請撰寫一程式，讓使用者輸入兩個正整數a、b（a<=b），
輸出從a到b（包含a和b）之間4或9的倍數
（一列輸出十個數字、欄寬為4、靠左對齊）
以及倍數之個數、總和。

輸入說明
兩個正整數a、b（a<=b）
輸出說明
格式化輸出兩個正整數之間4或9之倍數（包含a和b）
倍數個數
倍數總合

範例輸入1
5
55
範例輸出1
8   9   12  16  18  20  24  27  28  32  
36  40  44  45  48  52  54  
17
513

範例輸入2
4
9
範例輸出2
4   8   9   
3
21
"""
a=int(input())
b=int(input())

l=[]
printl=0
for i in range(a,b+1):
    
    if i%4==0:
        if printl%10==0:print()
        l.append(i)
        print('{:<4d}'.format(i),end='')
        printl=printl+1
    elif i%9==0:
        if printl%10==0:print()
        l.append(i)
        print('{:<4d}'.format(i),end='')
        printl=printl+1
        
print('\n',len(l),sep='')
print(sum(l))



















