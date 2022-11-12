# for i in range(2, 6):
#     print(i)
# else:
#     print("迴圈正常結束")

# i = 2
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("迴圈正常結束")

# i = 1
# while i < 6:
#     if i == 3:
#         break
#     print(i)
#     i += 1

# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# i = 1
# while i < 6:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     i += 1
# a = ('1.蘋果汁')
# b = ('2.柳橙汁')
# c = ('3.葡萄汁')
# d = ('系統關閉')

# while True:
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     ans = input('請輸入編號:')
#     if ans == '1':
#         print('您點的是' + a)
#     elif ans == '2':
#         print('您點的是' + b)
#     elif ans == '3':
#         print('您點的是' + c)
#     elif ans == '4':
#         print(d)
#         break
#     else:
#         print('無此果汁')
import random as r

a = r.randint(1, 100)
while True:
    x = int(input('請輸入1-100的整數:'))
    if x < a:
        print('在大一點')
    elif x > a:
        print('在小一點')
    elif x == a:
        print('中')
