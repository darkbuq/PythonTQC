#%%
"""
TQC+ 程式語言Python 501 訊息顯示
請撰寫一程式，呼叫函式compute()，
該函式功能為讓使用者輸入系別（Department）、學號（Student ID）
和姓名（Name）並顯示這些訊息。

輸入說明
三個字串
輸出說明
系別（Department）
學號（Student ID）
姓名（Name）

範例輸入
Information Management
123456789
Tina Chen
範例輸出
Department: Information Management
Student ID: 123456789
Name: Tina Chen
"""
def compute(dept,sid,name):
    print("Department:",dept)
    print("Student ID:",sid)
    print("Name:",name)
d=input()
s=input()
n=input()
compute(d,s,n)
#%%
"""
TQC+ 程式語言Python 502 乘積
請撰寫一程式，將使用者輸入的兩個整數作為參數
傳遞給一個名為compute(x, y)的函式，
此函式將回傳x和y的乘積。

輸入說明
兩個整數
輸出說明
兩個整數相乘之乘積

範例輸入
56
11
範例輸出
616
"""
a=int(input())
b=int(input())
def compute(x,y):
    return x*y
print(compute(a,b))
#%%
"""
TQC+ 程式語言Python 503 連加計算
請撰寫一程式，讓使用者輸入兩個整數，接著呼叫函式compute()，
此函式接收兩個參數a、b，並回傳從a連加到b的和。

輸入說明
兩個整數
輸出說明
從a連加到b的和

範例輸入
33
66
範例輸出
1683
"""
x=int(input())
y=int(input())
def compute(a,b):
    return sum(range(a,b+1))
print(compute(x,y))
#%%
"""
TQC+ 程式語言Python 504 次方計算
請撰寫一程式，讓使用者輸入兩個整數，
接著呼叫函式compute()，此函式接收兩個參數a、b，並回傳 a^b 的值。

範例輸入
14
3
範例輸出
2744
"""
x=int(input())
y=int(input())
def compute(a,b):
    return a**b
print(compute(x,y))
#%%
"""
TQC+ 程式語言Python 505 依參數格式化輸出
請撰寫一程式，將使用者輸入的三個參數，
變數名稱分別為a（代表字元character）、x（代表個數）、y（代表列數），
作為參數傳遞給一個名為compute()的函式，
該函式功能為：一列印出x個a字元，總共印出y列。

提示：輸出的每一個字元後方有一空格。

輸入說明
三個參數，分別為a（代表字元character）、x（代表個數）、y（代表列數）
輸出說明
一列印出x個a字元，總共印出y列

範例輸入
e
5
4
範例輸出
e e e e e 
e e e e e 
e e e e e 
e e e e e 
"""
s=input()
n1=int(input())
n2=int(input())
def compute(a,x,y):
    for i in range(n2):
        for j in range(n1):
            print('{} '.format(s),end='')
        if i!=n2+1:
            print()
compute(s,n1,n2)
#%%
"""
TQC+ 程式語言Python 506 一元二次方程式
請撰寫一程式，將使用者輸入的三個整數
（代表一元二次方程式  ax^2+bx+c=0 的三個係數a、b、c）
作為參數傳遞給一個名為compute()的函式，
該函式回傳方程式的解，
如無解則輸出【Your equation has no root.】
提示：輸出有順序性

輸入說明
三個整數，分別為a、b、c
輸出說明
代入一元二次方程式，回傳方程式解；
如無解則輸出【Your equation has no root.】

範例輸入1
2
-3
1
範例輸出1
1.0, 0.5
範例輸入2
9
9
8
範例輸出2
Your equation has no root.
"""
a=int(input())
b=int(input())
c=int(input())
def compute(a,b,c):
    
    if (b**2)<(4*a*c):
        print('Your equation has no root.')
    else:
        anss=(b**2)-(4*a*c)
        anss=anss**(1/2)
        anss1=((-b)+anss)/(2*a)
        anss2=((-b)-anss)/(2*a)
        print(anss1,anss2,sep=', ')
compute(a,b,c)    
#%%
"""
TQC+ 程式語言Python 507 質數
請撰寫一程式，讓使用者輸入一個整數x，
並將x傳遞給名為compute()的函式，
此函式將回傳x是否為質數（Prime number）的布林值，
接著再將判斷結果輸出。
如輸入值為質數顯示【Prime】，否則顯示【Not Prime】。      

輸入說明
一個整數
輸出說明
判斷是否為質數，若為質數顯示【Prime】，否則顯示【Not Prime】

範例輸入1
3
範例輸出1
Prime

範例輸入2
6
範例輸出2
Not Prime
"""
a=int(input())
def compute(x):
    anss=0
    for i in range(2,x):
        if x%i==0:
            anss=anss+1 
    return bool(anss)
booll=compute(a)        
if booll!=True:
    print('Prime')
else:
    print('Not Prime')

















