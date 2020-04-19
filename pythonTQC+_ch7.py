#%%
"""
TQC+ 程式語言Python 701 串列數組轉換
請撰寫一程式，輸入數個整數並儲存至串列中，
以輸入-9999為結束點（串列中不包含-9999），
再將此串列轉換成數組，最後顯示該數組以及其長度（Length）
、最大值（Max）、最小值（Min）、總和（Sum）。

輸入說明
n個整數，直至-9999結束輸入

輸出說明
數組
數組的長度
數組中的最大值
數組中的最小值
數組內的整數總和

範例輸入
-4
0
37
19
26
-43
9
-9999
範例輸出
(-4, 0, 37, 19, 26, -43, 9)
Length: 7
Max: 37
Min: -43
Sum: 44
"""
ll=[]
x=int(input())
while (x!=(-9999)):
    ll.append(x)
    x=int(input())
    
tt=tuple(ll)
print(tt)
print('Length:', len(tt))
print('Max:', max(tt))
print('Min:', min(tt))
print('Sum:', sum(tt))
#%%
"""
TQC+ 程式語言Python 702 數組合併排序
請撰寫一程式，輸入並建立兩組數組，
各以-9999為結束點（數組中不包含-9999）。
將此兩數組合併並從小到大排序之，顯示排序前的數組和排序後的串列。

輸入說明
兩個數組，直至-9999結束輸入
輸出說明
排序前的數組
排序後的串列

輸入與輸出會交雜如下，輸出的部份以粗體字表示
Create tuple1:
9
0
-1
3
8
-9999
Create tuple2:
28
16
39
56
78
88
-9999
Combined tuple before sorting: (9, 0, -1, 3, 8, 28, 16, 39, 56, 78, 88)
Combined list after sorting: [-1, 0, 3, 8, 9, 16, 28, 39, 56, 78, 88]
"""
la=[]
print("Create tuple1:")
x=int(input())
while (x!=(-9999)):
    la.append(x)
    x=int(input())

lb=[]
print("Create tuple2:")
x=int(input())
while (x!=(-9999)):
    lb.append(x)
    x=int(input())

lc=la+lb
tt=tuple(lc)
print('Combined tuple before sorting:', tt)
print('Combined list after sorting:', sorted(lc))
#%%
"""
TQC+ 程式語言Python 703 數組條件判斷
請撰寫一程式，輸入一些字串至數組（至少輸入五個字串）
以字串"end"為結束點（數組中不包含字串"end"）。
接著輸出該數組，
再分別顯示該數組的第一個元素到第三個元素和倒數三個元素。

輸入說明
至少輸入五個字串至數組，直至end結束輸入
輸出說明
數組
該數組的前三個元素
該數組最後三個元素

範例輸入
president
dean
chair
staff
teacher
student
end
範例輸出
('president', 'dean', 'chair', 'staff', 'teacher', 'student')
('president', 'dean', 'chair')
('staff', 'teacher', 'student')
"""
ll=[]
while True:
    x=input()
    if x=='end':
        break
    ll.append(x)
tt=tuple(ll)
print(tt)
print(tt[0:3])
print(tt[(-3):])
#%%
"""
TQC+ 程式語言Python 704 集合條件判斷
請撰寫一程式，輸入數個整數並儲存至集合，
以輸入-9999為結束點（集合中不包含-9999），
最後顯示該集合的長度（Length）、最大值（Max）
最小值（Min）、總和（Sum）。

輸入說明
輸入n個整數至集合，直至-9999結束輸入
輸出說明
集合的長度
集合中的最大值
集合中的最小值
集合內的整數總和

範例輸入
34
-23
29
7
0
-1
-9999
範例輸出
Length: 6
Max: 34
Min: -23
Sum: 46
"""
ss=set()
while True:
    x=int(input())
    if x==(-9999):
        break
    ss.add(x)
print('Length:',len(ss))
print('Max:',max(ss))
print('Min:',min(ss))
print('Sum:',sum(ss))
#%%
"""
TQC+ 程式語言Python 705 子集合與超集合
請撰寫一程式，依序輸入五個、三個、九個整數，
並各自儲存到集合set1、set2、set3中。
接著回答：set2是否為set1的子集合（subset）？
set3是否為set1的超集合（superset）？

輸入說明
依序分別輸入五個、三個、九個整數
輸出說明
顯示回覆：
set2是否為set1的子集合（subset）？
set3是否為set1的超集合（superset）？

輸入與輸出會交雜如下，輸出的部份以粗體字表示
Input to set1:
3
28
-2
7
39
Input to set2:
2
77
0
Input to set3:
3
28
12
99
39
7
-1
-2
65
set2 is subset of set1: False
set3 is superset of set1: True
"""
# =============================================================================
# 聯集： A B 集合的所有項目
# 交集： A B 集合的共有項目
# 差集： A 集合扣掉 A B 集合的共有項目
# 對稱差集： A B 集合的獨有項目
# 
# 子集合 (sebset) ： 
# 若 A 集合的所有項目是 B 集合的部分集合, 則稱 A 為 B 的子集合
# 超集合 (superset) ： 
# 若 A 集合的所有項目是 B 集合的部分集合, 則稱 B 為 A 的超集合
# =============================================================================

# s1={3,28,-2,7,39}
s1=set()
print('Input to set1:')
for i in range(5):
    s1.add(int(input()))

# s2={2,77,0}
s2=set()
print('Input to set2:')
for i in range(3):
    s2.add(int(input()))

# s3={3,28,12,99,39,7,-1,-2,65}
s3=set()
print('Input to set3:')
for i in range(9):
    s3.add(int(input()))

print('set2 is subset of set1:',s2.issubset(s1))
print('set3 is superset of set1:',s3.issuperset(s1))
#%%
"""
TQC+ 程式語言Python 706 全字母句
全字母句（Pangram）是英文字母表所有的字母都出現至少一次
（最好只出現一次）的句子。
請撰寫一程式，要求使用者輸入一正整數k（代表有k筆測試資料），
每一筆測試資料為一句子，程式判斷該句子是否為Pangram，
並印出對應結果True（若是）或False（若不是）。

提示：不區分大小寫字母

輸入說明
先輸入一個正整數表示測試資料筆數，再輸入測試資料
輸出說明
輸入的資料是否為全字母句

輸入與輸出會交雜如下，輸出的部份以粗體字表示 第1組
3
The quick brown fox jumps over the lazy dog
True
Learning Python is funny
False
Pack my box with five dozen liquor jugs
True

輸入與輸出會交雜如下，輸出的部份以粗體字表示 第2組
2
Quick fox jumps nightly above wizard
True
These can be weapons of terror
False
"""
# =============================================================================
# s1=set('The quick brown fox jumps over the lazy dog')
# s11={'The quick brown fox jumps over the lazy dog'}
# #上面是兩種set 差很多 要注意
# s2=set('The quick brown fox jumps over the lazy do55555')
# 
# len(s1.upper()) #會報錯
# len(s2.upper()) #會報錯
# #  'set' object has no attribute 'upper'
# # 所以要在設成set之前就要處理大小寫
# =============================================================================
x=int(input())

for i in range(x):
    ss=set(input().upper()) #如果有數字 這行是無法判斷的 考試沒差
    print(len(ss)==27)
#%%
"""
TQC+ 程式語言Python 707 共同科目
請撰寫一程式，輸入X組和Y組各自的科目至集合中，
以字串"end"作為結束點（集合中不包含字串"end"）。
請依序分行顯示(1) X組和Y組的所有科目、
(2)X組和Y組的共同科目、(3)Y組有但X組沒有的科目，
以及(4) X組和Y組彼此沒有的科目（不包含相同科目）。

提示：科目須參考範例輸出樣本，依字母由小至大進行排序。

輸入說明
輸入X組和Y組各自的科目至集合，直至end結束輸入
輸出說明
X組和Y組的所有科目
X組和Y組的共同科目
Y組有但X組沒有的科目
X組和Y組彼此沒有的科目（不包含相同科目）

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
Enter group X's subjects:
Math
Literature
English
History
Geography
end
Enter group Y's subjects:
Math
Literature
Chinese
Physical
Chemistry
end
['Chemistry', 'Chinese', 'English', 'Geography', 'History', 'Literature', 'Math', 'Physical']
['Literature', 'Math']
['Chemistry', 'Chinese', 'Physical']
['Chemistry', 'Chinese', 'English', 'Geography', 'History', 'Physical']
"""
a=set()
print("Enter group X's subjects:")
while True:
    x=input()
    if x=='end':
        break
    a.add(x)

b=set()
print("Enter group Y's subjects:")
while True:
    x=input()
    if x=='end':
        break
    b.add(x)

print(sorted(a|b))
print(sorted(a&b))
print(sorted(a-b))
print(sorted(a^b))




