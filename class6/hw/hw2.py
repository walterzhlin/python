"""
請輸入要印出的箭頭大小
​
hint:
可利用字串乘法
val="*" * 3
print(val)
***
​
EX:
請輸入要印出的箭頭大小:3
  *  
 *** 
*****
  *  
  *  
  * 
"""

x = int(input('請輸入要印出的箭頭大小:'))

for i in range(x):
    # print(f'{x-i-1},{i*2+1}')
    print(' ' * (x - i - 1) + '*' * (i * 2 + 1))
for i in range(x):
    print(' ' * (x - 1) + '*' * (1) + ' ' * (x - 1))
