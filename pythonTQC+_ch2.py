#%%
"""
Python 201 偶數判斷
請使用選擇敘述撰寫一程式，
讓使用者輸入一個正整數，然後判斷它是否為偶數（even）。

範例輸出
56 is an even number.
21 is not an even number.
"""
x=int(input())
if x%2==0:
    print('{:d} is an even number.'.format(x))
else:
    print('{:d} is not an even number.'.format(x))
#%%
"""
Python 202 倍數判斷
請使用選擇敘述撰寫一程式，讓使用者輸入一個正整數，
然後判斷它是3或5的倍數，顯示【x is a multiple of 3.】
或【x is a multiple of 5.】；若此數值同時為3與5的倍數，
顯示【x is a multiple of 3 and 5.】；
如此數值皆不屬於3或5的倍數，
顯示【x is not a multiple of 3 or 5.】，將使用者輸入的數值代入x。
範例輸出
55 is a multiple of 5.
36 is a multiple of 3.
92 is not a multiple of 3 or 5.
15 is a multiple of 3 and 5.
"""
x=int(input())
if x%3==0 and x%5==0:
    print('{} is a multiple of 3 and 5.'.format(x))
elif x%3==0 and x%5!=0:
    print('{} is a multiple of 3.'.format(x))
elif x%3!=0 and x%5==0:
    print('{} is a multiple of 5.'.format(x))
else:
    print('{} is not a multiple of 3 or 5.'.format(x))
#%%
"""
Python 203 閏年判斷
請使用選擇敘述撰寫一程式，讓使用者輸入一個西元年份，
然後判斷它是否為閏年（leap year）或平年。
其判斷規則為：每四年一閏，每百年不閏，但每四百年也一閏。

範例輸出
1992 is a leap year.
2010 is not a leap year.
"""
x=int(input())
if x%400==0:
    print('{} is a leap year.'.format(x))
elif x%4==0 and x%100!=0:
    print('{} is a leap year.'.format(x))
else:
    print('{} is not a leap year.'.format(x))
#%%
"""
Python 204 算術運算
請使用選擇敘述撰寫一程式，讓使用者輸入兩個整數a、b，
然後再輸入一算術運算子 (+、-、*、/、//、%） ，輸出經過運算後的結果。
範例輸入
30
20
*
範例輸出
600
"""
a=int(input())
b=int(input())
c=input()
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    print(a/b)
elif c=='//':
    print(a//b)
elif c=='%':
    print(a%b)
#%%
"""
Python 205 字元判斷
請使用選擇敘述撰寫一程式，讓使用者輸入一個字元，
判斷它是包括大、小寫的英文字母（alphabet）、數字（number）、
或者其它字元（symbol）。例如：a為英文字母、9為數字、$為其它字元。
範例輸入
P is an alphabet.
@ is a symbol.
7 is a number.
"""
a=input()
if str.isalpha(a):
    print('%s is an alphabet.'%(a))
elif str.isdigit(a):
    print('%s is a number.'%(a))
else:
    print('%s is a symbol.'%(a))
#%%
"""
Python 206 等級判斷
請使用選擇敘述撰寫一程式，
根據使用者輸入的分數顯示對應的等級。
標準如下表所示：

分　數	等級
80 ~ 100	A
70 ~ 79	B
60 ~ 69	C
<= 59	F
"""
x=int(input())
if x>=80:
    print('A')
elif x<80 and x>=70:
    print('B')
elif x<70 and x>=60:
    print('C')
else:
    print('F')
#%%
"""
Python 207 折扣方案
請使用選擇敘述撰寫一程式，要求使用者輸入購物金額，
購物金額需大於8,000（含）以上，並顯示折扣優惠後的實付金額。
購物金額折扣方案如下表所示：

金　　額	折　扣
8,000（含）以上	9.5折
18,000（含）以上	9折
28,000（含）以上	8折
38,000（含）以上	7折

輸入說明
一個數值，需大於8,000（含）以上
輸出說明
顯示折扣優惠後的實付金額（輸出不需指定小數點位數）

範例輸入
12000
範例輸出
11400.0
"""
x=int(input())
if x>=38000:
    print(x*0.7)
elif x>=28000:
    print(x*0.8)
elif x>=18000:
    print(x*0.9)
elif x>=8000:
    print(x*0.95)
#%%
"""
Python 208 十進位換算
請使用選擇敘述撰寫一程式，
讓使用者輸入一個十進位整數num(0 ≤ num ≤ 15)，
將num轉換成十六進位值。

提示：
轉換規則 = 十進位0~9的十六進位值為其本身，
十進位10~15的十六進位值為A~F。
"""
x=int(input())
print('%X'%(x))
#%%
"""
Python 209 距離判斷
請使用選擇敘述撰寫一程式，讓使用者輸入一個點的平面座標x和y值，
判斷此點是否與點(5, 6)的距離小於或等於15，
如距離小於或等於15顯示【Inside】，反之顯示【Outside】。

輸入說明
兩個數值x、y

輸出說明
小於或等於15輸出Inside；大於15輸出Outside

範例輸出
Inside
Outside
"""
x=eval(input())
y=eval(input())
dd=(((x-5)**2)+((y-6)**2))**(1/2)
if dd<=15:
    print('Inside')
else:
    print('Outside')
#%%
"""
Python 210 三角形判斷
請使用選擇敘述撰寫一程式，讓使用者輸入三個邊長，
檢查這三個邊長是否可以組成一個三角形。
若可以，則輸出該三角形之周長；
否則顯示【Invalid】。

提示：檢查方法 = 任意兩個邊長之總和大於第三邊長。

範例輸出
Invalid
3
"""
a=eval(input())
b=eval(input())
c=eval(input())
if a+b>c and b+c>a and c+a>b:
    print(a+b+c)
else:
    print('Invalid')







  