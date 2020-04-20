#%%
"""
TQC+ 程式語言Python 801 字串索引
請撰寫一程式，首先要求使用者輸入正整數k（1 <= k <= 100），
代表有k筆測試資料。每一筆測試資料是一串數字，
每個數字之間以一空白區隔，請找出此串列數字中最大值和最小值之間的差。

提示：差值輸出到小數點後第二位。

輸入說明
先輸入測試資料的筆數，再輸入每一筆測試資料
（一串數字，每個數字之間以空白區隔）
輸出說明
每個串列數字中，最大值和最小值之間的差

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
4
94 52.9 3.14 77 46
90.86
-2 0 1000.34 -14.4 89 50
1014.74
87.78 33333 29.3
33303.70
9998 9996 9999
3.00
"""
k=0
while(k<1 or k>100):
    k=int(input())

for j in range(k):
    str=input()
    ll=str.split(' ')
    lll=[]
    for i in ll:
        lll.append(eval(i))
    print('{:.2f}'.format(max(lll)-min(lll)))
#%%
"""
TQC+ 程式語言Python 802 字元對應
請撰寫一程式，要求使用者輸入一字串，
顯示該字串每個字元的對應ASCII碼及其總和。

輸入說明
一個字串
輸出說明
依序輸出字串中每個字元對應的ASCII碼
每個字元ASCII碼的總和

範例輸入
Kingdom
範例輸出
ASCII code for 'K' is 75
ASCII code for 'i' is 105
ASCII code for 'n' is 110
ASCII code for 'g' is 103
ASCII code for 'd' is 100
ASCII code for 'o' is 111
ASCII code for 'm' is 109
713
"""
str=input()
summ=0
for i in str:
    print("ASCII code for '{:s}' is {:d}".format(i,ord(i)))
    summ=summ+ord(i)
print(summ)
#%%
"""
TQC+ 程式語言Python 803 倒數三個詞
請撰寫一程式，讓使用者輸入一個句子（至少有五個詞，以空白隔開），
並輸出該句子倒數三個詞。

輸入說明
一個句子（至少五個詞，以空白隔開）
輸出說明
該句子倒數三個詞

輸入輸出範例
範例輸入
Many foreign students study in FJU
範例輸出
study in FJU
"""
ll=input().split()
print(ll[-3],ll[-2],ll[-1])
#%%
"""
TQC+ 程式語言Python 804 大寫轉換
請撰寫一程式，讓使用者輸入一字串，
分別將該字串轉換成全部大寫以及每個字的第一個字母大寫。

輸入說明
一個字串
輸出說明
全部大寫
每個字的第一個字母大寫

範例輸入
learning python is funny
範例輸出
LEARNING PYTHON IS FUNNY
Learning Python Is Funny
"""
ll=input()
print(ll.upper())
print(ll.title())


















