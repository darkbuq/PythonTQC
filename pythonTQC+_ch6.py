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
"""
TQC+ 程式語言Python 605 成績計算
請撰寫一程式，讓使用者輸入十個成績，
接下來將十個成績中最小和最大值（最小、最大值不重複）
以外的成績作加總及平均，並輸出結果。

提示：平均值輸出到小數點後第二位。

輸入說明
十個數字
輸出說明
總和
平均

範例輸入
89
78
67
80
75
98
77
89
76
60
範例輸出
631
78.88
"""
#ll=[89,78,67,80,75,98,77,89,76,60]
ll=[]
for i in range(10):
    x=int(input())
    ll.append(x)

maxx=max(ll)
minn=min(ll)
ll.remove(maxx)
ll.remove(minn)
print(sum(ll))
print('{:.2f}'.format(sum(ll)/len(ll)))
#%%
"""
TQC+ 程式語言Python 606 二維串列行列數
請撰寫一程式，讓使用者輸入兩個正整數rows、cols，
分別表示二維串列lst 的「第一個維度大小」與「第二個維度大小」。
串列元素[row][col]所儲存的數字，其規則為：
row、col 的交點值 = 第二個維度的索引col – 第一個維度的索引row。
接著以該串列作為參數呼叫函式compute()輸出串列。

提示：欄寬為4。

輸入說明
兩個正整數（rows、cols）
輸出說明
格式化輸出row、col的交點值

範例輸入
5
10
範例輸出
   0   1   2   3   4   5   6   7   8   9
  -1   0   1   2   3   4   5   6   7   8
  -2  -1   0   1   2   3   4   5   6   7
  -3  -2  -1   0   1   2   3   4   5   6
  -4  -3  -2  -1   0   1   2   3   4   5
"""
roww=int(input())
coll=int(input())

def compute(row,col):
    for i in range(1,roww+1):
        for j in range(1,col+1):
            print('{:>4d}'.format(j-i),sep='',end='')
        print()

compute(roww,coll)
#%%
"""
TQC+ 程式語言Python 607 成績計算
請撰寫一程式，讓使用者輸入三位學生各五筆成績，
接著再計算並輸出每位學生的總分及平均分數。

提示：平均分數輸出到小數點後第二位。

輸入說明
三位學生各五筆成績
輸出說明
格式化輸出每位學生的總分及平均分數

輸入與輸出會交雜如下，輸出的部份以粗體字表示
The 1st student:
78
89
88
70
60
The 2nd student:
90
78
66
68
78
The 3rd student:
69
97
70
89
90
Student 1
#Sum 385
#Average 77.00
Student 2
#Sum 380
#Average 76.00
Student 3
#Sum 415
#Average 83.00
"""
print('The 1st student:')
l1=[]
for i in range(5):
    l1.append(int(input()))

print('The 2nd student:')
l2=[]
for i in range(5):
    l2.append(int(input()))

print('The 3rd student:')
l3=[]
for i in range(5):
    l3.append(int(input()))

import numpy as np

print('Student 1')
print('#Sum {:d}'.format(sum(l1)))
print('#Average {:.2f}'.format(np.mean(l1)))

print('Student 2')
print('#Sum {:d}'.format(sum(l2)))
print('#Average {:.2f}'.format(np.mean(l2)))

print('Student 3')
print('#Sum {:d}'.format(sum(l3)))
print('#Average {:.2f}'.format(np.mean(l3)))
#%%
"""
TQC+ 程式語言Python 608 最大最小值索引
請撰寫一程式，讓使用者建立一個3*3的矩陣，
其內容為從鍵盤輸入的整數（不重複），
接著輸出矩陣最大值與最小值的索引。

輸入說明
九個整數
輸出說明
矩陣最大值及其索引
矩陣最小值及其索引

範例輸入
6
4
8
39
12
3
-3
49
33
範例輸出
Index of the largest number 49 is: (2, 1)
Index of the smallest number -3 is: (2, 0)
"""
ll=[]
for i in range(9): ll.append(int(input()))
print('Index of the largest number {:d} is: ({:d}, {:d})'
      .format(max(ll), ll.index(max(ll))//3, ll.index(max(ll))%3))

print('Index of the smallest number {:d} is: ({:d}, {:d})'
      .format(min(ll), ll.index(min(ll))//3, ll.index(min(ll))%3))
#%%
"""
TQC+ 程式語言Python 609 矩陣相加
請撰寫一程式，讓使用者建立兩個2*2的矩陣，
其內容為從鍵盤輸入的整數，
接著輸出這兩個矩陣的內容以及它們相加的結果。

輸入說明
兩個2*2矩陣，皆輸入整數
輸出說明
矩陣1的內容
矩陣2的內容
矩陣1及矩陣2相加的結果

輸入與輸出會交雜如下
Enter matrix 1:
[1, 1]: 3
[1, 2]: 5
[2, 1]: 7
[2, 2]: 5
Enter matrix 2:
[1, 1]: 6
[1, 2]: 9
[2, 1]: 8
[2, 2]: 3

Matrix 1:
**3 5 **
**7 5 **
Matrix 2:
**6 9 **
**8 3 **
Sum of 2 matrices:
**9 14 **
**15 8 **
"""
la=[]
print('Enter matrix 1:')
for i in range(4): 
    la.append(int(input('[{:d}, {:d}]: '
                        .format((i//2)+1, (i%2)+1))))

lb=[]
print('Enter matrix 2:')
for i in range(4): 
    lb.append(int(input('[{:d}, {:d}]: '
                        .format((i//2)+1, (i%2)+1))))

lc=[]
for i in range(4): lc.append(la[i] + lb[i])

print('Matrix 1:\n{} {} \n{} {} '
      .format(la[0], la[1], la[2], la[3]))
print('Matrix 2:\n{} {} \n{} {} '
      .format(lb[0], lb[1], lb[2], lb[3]))
print('Sum of 2 matrices:\n{} {} \n{} {} '
      .format(lc[0], lc[1], lc[2], lc[3]))
#%%
"""
TQC+ 程式語言Python 610 平均溫度
請撰寫一程式，讓使用者輸入四週各三天的溫度，
接著計算並輸出這四週的平均溫度及最高、最低溫度。

提示1：平均溫度輸出到小數點後第二位。
提示2：最高溫度及最低溫度的輸出，如為31時，
       則輸出31，如為31.1時，則輸出31.1。

輸入說明
四週各三天的溫度
輸出說明
平均溫度
最高溫度
最低溫度

輸入輸出範例
Week 1:
Day 1:23.1
Day 2:24
Day 3:23.5
Week 2:
Day 1:23.1
Day 2:24
Day 3:23.5
Week 3:
Day 1:23.1
Day 2:24
Day 3:23.5
Week 4:
Day 1:23.1
Day 2:24
Day 3:23.5
Average: 28.11
Highest: 35.3
Lowest: 23.1
"""
import numpy as np
ll=[]
for i in range(12):
    if i%3==0:
        print('Week {:d}:'.format((i//3)+1))
    ll.append(eval(input('Day {:d}:'.format((i%3)+1))))

print('Average: {:.2f}'.format(np.mean(ll)))
print('Highest:',max(ll))
print('Lowest:',min(ll))

