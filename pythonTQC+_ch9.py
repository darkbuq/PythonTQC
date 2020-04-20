#%%
"""
TQC+ 程式語言Python 901 成績資料
請撰寫一程式，要求使用者讀入read.dat（以UTF-8編碼格式讀取）
第一列為欄位名稱，第二列之後是個人記錄。
請輸出檔案內容並顯示男生人數和女生人數
（根據"性別"欄位，0為女性、1為男性）。

輸入說明
讀取read.dat
輸出說明
讀取檔案內容，並格式化輸出男生人數和女生人數

輸入輸出範例
範例輸入
無

範例輸出
學號 姓名 性別 科系

101 陳小華 0 餐旅管理

202 李小安 1 廣告

303 張小威 1 英文

404 羅小美 0 法文

505 陳小凱 1 日文
Number of males: 3
Number of females: 2
"""

# =============================================================================
# fp=open(r"C:\Users\ASUS\Desktop\read.dat", "w",encoding='UTF-8')
# for i in range(5):
#   fp.write(input())
#   fp.write('\n')
# fp.close()
# =============================================================================
#%%
"""
TQC+ 程式語言Python 902 資料加總
請撰寫一程式，讀取read.txt的內容（內容為數字，以空白分隔）
並將這些數字加總後輸出。檔案讀取完成後要關閉。

輸入說明
讀取read.txt的內容（內容為數字，以空白分隔）
輸出說明
總和

輸入輸出範例
範例輸入
無
範例輸出
660
"""
ff=open('read.txt','r',encoding='UTF-8')
dt=ff.read()
ff.close()

summ=0
for i in dt.split():
    summ=summ+int(i)
print(summ)
#%%
"""
TQC+ 程式語言Python 903 成績資料
請撰寫一程式，要求使用者輸入五個人的名字並加入到data.txt的尾端。
之後再顯示此檔案的內容。


輸入說明
輸入五個人的名字
輸出說明
讀取及寫入檔案後，輸出此檔案內容

輸入輸出範例
範例輸入
Daisy
Kelvin
Tom
Joyce
Sarah
範例輸出
Append completed!
Content of "data.txt":
Ben
Cathy
Tony
Daisy
Kelvin
Tom
Joyce
Sarah
"""
fa=open('data.txt','a',encoding='UTF-8')
for i in range(5):
    fa.write("\n"+input())
print('Append completed!')
print('Content of "data.txt":')
fa.close()

fr=open('data.txt',encoding='UTF-8')
for i in fr:
    print(i,end="")
fr.close()
#%%
"""
TQC+ 程式語言Python 904 資料計算
請撰寫一程式，讀取read.txt
（每一列的格式為名字和身高、體重，以空白分隔）
並顯示檔案內容、所有人的平均身高、平均體重以及最高者、最重者。

提示：輸出浮點數到小數點後第二位。

輸入說明
讀取read.txt（每一行的格式為名字和身高、體重，以空白分隔）
輸出說明
輸出檔案中的內容
平均身高
平均體重
最高者
最重者

輸入輸出範例
範例輸入
無
範例輸出
Ben 175 65

Cathy 155 55

Tony 172 75
Average height: 167.33
Average weight: 65.00
The tallest is Ben with 175.00cm
The heaviest is Tony with 75.00kg
"""
import numpy as np
fr=open('read.txt',encoding='UTF-8')
hl=[]
wl=[]
nl=[]
for i in fr:
    nl.append(str(i.split()[0]))
    hl.append(int(i.split()[1]))
    wl.append(int(i.split()[2]))
    print(i)
fr.close()

print('Average height: {:.2f}'.format(np.mean(hl)))
print('Average weight: {:.2f}'.format(np.mean(wl)))

print('The tallest is {:s} with {:.2f}cm'
      .format(nl[hl.index(max(hl))],max(hl)))
print('The heaviest is {:s} with {:.2f}kg'
      .format(nl[wl.index(max(wl))],max(wl)))













