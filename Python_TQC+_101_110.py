# Python TQC+解題101~110
# http://b0212066.pixnet.net/blog/post/214984392-python-tqc%2B-_110_%E6%AD%A3n%E9%82%8A%E5%BD%A2%E9%9D%A2%E7%A9%8D%E8%A8%88%E7%AE%97
#%%
"""
101_整數格式化輸出
題目說明:
請撰寫一程式，輸入四個整數，
然後將這四個整數以欄寬為5、欄與欄間隔一個空白字元，
再以每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，
左右皆以直線 |（Vertical bar）作為邊界。

範例輸出
|   85     4|
|  299   478|
|85    4    |
|299   478  |
"""
x1=int(input())
x2=int(input())
x3=int(input())
x4=int(input())
print('|{:>5d} {:>5d}|\n|{:>5d} {:>5d}|'.format(x1,x2,x3,x4))
print('|{:<5d} {:<5d}|\n|{:<5d} {:<5d}|'.format(x1,x2,x3,x4))
#%%
"""
102_浮點數格式化輸出
題目說明:
請撰寫一程式，輸入四個分別含有小數1到4位的浮點數，
然後將這四個浮點數以欄寬為7、欄與欄間隔一個空白字元、
每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，
左右皆以直線 |（Vertical bar）作為邊界。
提示：輸出浮點數到小數點後第二位

範例輸出
|  23.12  395.30|
| 100.46  564.33|
|23.12   395.30 |
|100.46  564.33 |
"""
x1=float(input())
x2=float(input())
x3=float(input())
x4=float(input())
print('|{:>7.2f} {:>7.2f}|\n|{:>7.2f} {:>7.2f}|'.format(x1,x2,x3,x4))
print('|{:<7.2f} {:<7.2f}|\n|{:<7.2f} {:<7.2f}|'.format(x1,x2,x3,x4))
#%%
"""
103_字串格式化輸出
題目說明:
請撰寫一程式，輸入四個單字，
然後將這四個單字以欄寬為10、欄與欄間隔一個空白字元、
每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，
左右皆以直線 |（Vertical bar）作為邊界。

範例輸出 
|         I      enjoy|
|  learning     Python|
|I          enjoy     |
|learning   Python    |
"""
# x1='I';x2='enjoy';x3='learning';x4='Python'
x1=input()
x2=input()
x3=input()
x4=input()
print('|{:>10s} {:>10s}|\n|{:>10s} {:>10s}|'.format(x1,x2,x3,x4))
print('|{:<10s} {:<10s}|\n|{:<10s} {:<10s}|'.format(x1,x2,x3,x4))
#%%
"""
104_圓形面積計算
題目說明:
請撰寫一程式，輸入一圓的半徑，並加以計算此圓之面積和周長，
最後請印出此圓的半徑（Radius）、周長（Perimeter）和面積（Area）
提示：
->需import math模組，並使用math.pi
->輸出浮點數到小數點後第二位

範例輸出
Radius = 10.00
Perimeter = 62.83
Area = 314.16
"""
import math
Radius=float(input())
Perimeter=2*Radius*math.pi
Area=Radius*Radius*math.pi
print('Radius = {:.2f}\nPerimeter = {:.2f}\nArea = {:.2f}'
      .format(Radius,Perimeter,Area))
#%%
"""
105_矩形面積計算
題目說明:
請撰寫一程式，輸入兩個正數，代表一矩形之寬和高，
計算並輸出此矩形之高（Height）、寬（Width）、周長（Perimeter）及面積（Area）
提示: 輸出浮點數到小數點後第二位

範例輸出
Height = 23.50
Width = 19.00
Perimeter = 85.00
Area = 446.50
"""
h=float(input())
w=float(input())
print('Height = {:.2f}\nWidth = {:.2f}\nPerimeter = {:.2f}\nArea = {:.2f}'
      .format(h,w,2*(h+w),h*w))
#%%
"""
106_公里英哩換算
題目說明:
假設一賽跑選手在x分y秒的時間跑完z公里，
請撰寫一程式，輸入x、y、z數值，
最後顯示此選手每小時的平均英哩速度（1英哩等於1.6公里）
提示: 輸出浮點數到小數點後第一位

範例輸入
10
25
3
範例輸出
Speed = 10.8
"""
x=float(input())
y=float(input())
z=float(input())
print('Speed = {:.1f}'.format((z/1.6)/((x+y/60)/60)))
#%%
"""
107_數值計算
題目說明:
請撰寫一程式，讓使用者輸入五個數字，
計算並輸出這五個數字之數值、總和及平均數
提示： 輸出浮點數到小數點後第1位

範例輸出
20 40 60 80 100
Sum = 300.0
Average = 60.0
"""
x=[]
strr=''
for i in range(5):
    kk=float(input())
    x.append(kk)
    strr=strr+' '+str(kk)
print(strr[1:])
print('Sum = {:.1f}'.format(sum(x)))
print('Average = {:.1f}'.format(sum(x)/5))
#%%
"""
108_座標距離計算
題目說明:
請撰寫一程式，讓使用者輸入四個數字x1、y1、x2、y2，
分別代表兩個點的座標(x1, y1)、(x2, y2)。
計算並輸出這兩點的座標與其歐式距離
提示：
->歐式距離 = sqrt((x1 - x2)^2+(y1 - y2)^2)就是=>  
-> 兩座標的歐式距離，輸出到小數點後第4位     

範例輸出
( 2 , 1 )
( 5.5 , 8 )
Distance = 7.8262
"""
import math
x1=eval(input())
y1=eval(input())
x2=eval(input())
y2=eval(input())
print('( {} , {} )'.format(x1,y1))
print('( {} , {} )'.format(x2,y2))
print('Distance = {:.4f}'.format(math.sqrt((x1 - x2)**2+(y1 - y2)**2)))
#%%
"""
109_正五邊形面積計算
題目說明:
請撰寫一程式，讓使用者輸入一個正數s，代表正五邊形之邊長，
計算並輸出此正五邊形之面積（Area）
提示：
-> 建議使用import math模組的math.pow及math.tan
-> 正五邊形面積的公式：Area=(5*(s**2))/(4*tan(pi/5))
-> 輸出浮點數到小數點後第四位

範例輸出
Area = 43.0119
"""
import math
s=eval(input())
Area=(5*(s**2))/(4*math.tan(math.pi/5))
print('Area = {:.4f}'.format(Area))
#%%
"""
110_正n邊形面積計算
題目說明:
題目敘述有錯
提示：
-> 建議使用import math模組的math.pow及math.tan
-> 正五邊形面積的公式：
-> 輸出浮點數到小數點後第四位

範例輸出
Area = 173.8234
"""
import math
n = eval(input())
s = eval(input())
area = (n*math.pow(s,2))/(4*math.tan(math.pi/n))
print('Area = {:.4f}'.format(area))









