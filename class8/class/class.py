# ['蘋果', '香蕉', '葡萄']

# []
# ['蘋果']
# ['a', 'b']
# [1, 2, 3]

# [1, 2] + ['b', 'c']

# [1, 2] * 2

# l = ['a', 'b', 'c']
# l[0]
# l[1]
# l[2]

# l = [0, 1, 2, 3, 4]
# l[0:3]
# l[3:5]

# len([])
# len(['蘋果'])
# len(['a', 'b'])
# len([1, 2, 3])

# l = ['a', 'b', 'c']
# for index in range(len(l)):
#     print(l[index])

# l = ['a', 'b', 'c']
# for element in l:
#     print(element)

# max([])
# max(['蘋果', '香蕉', '橘子'])
# max(['a', 'b'])
# max([1, 2, 3])

# min([])
# min(['蘋果', '香蕉', '橘子'])
# min(['a', 'b'])
# min([1, 2, 3])

# list('abc')
# list([4, 5, 6])
# list(range(3))
# '1,2,3'.split(',')
# '2020/1/1'.split('/')

# img = ['1', '2', '3']
# '-'.join(img)

# l = ['a', 'b', 'c']
# a = l.copy()
# a[0] = 1
# print(a, l)
# 白色的对勾
# 眼睛
# 举起双手
# 回复
# 回复

a = ('1.蘋果汁')
b = ('2.柳橙汁')
c = ('3.葡萄汁')
d = ('系統關閉')
j = ['蘋果汁', '柳橙汁', '葡萄汁', '可樂', '系統關閉']
while True:
    for i in range(len(j)):
        print(f'{i+1}. {j[i]}')
    ans = int(input('請輸入編號:'))
    if ans == len(j):
        print('系統關閉')
        break
    elif ans > len(j) or ans <= 0:
        print('無此果汁')
    else:
        print(f'你點的是{j[ans-1]}')
