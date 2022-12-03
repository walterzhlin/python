# l = ['a', 'b', 'c']
# l
# l[0] = 'A'
# l

# a = [1, 2, 3]
# b = a
# b[0] = 2
# print(a)

# l = [1, 2, 3]
# l.append(4)
# print(l)

# l = [9, 1, -4, 3, 7, 11, 3]
# print(l.count(3))

# l = ['a', 'b', 'c', 'a']
# l.remove('a')
# print(l)

# l = [1, 2, 3]
# l.insert(0, 'A')
# print(l)

# l = [1, 2, 3]
# l.pop()
# print(l)

# l = [1, 2, 3]
# l.pop(0)
# print(l)

# l = [3, 1, 5, 4, 2]
# l.sort()
# print(l)

# l = [3, 1, 5, 4, 2]
# l.sort(reverse=True)
# print(l)

# l = [3, 1, 5, 4, 2]
# l.reverse()
# print(l)

# l = ['a', 'b', 'c', 'a']
# index = l.index('a')
# print(index)
# l=[1,2,5,3,6,4,1,1,2,2,3,5]
# print(not(1 in l))
# while 1 in l:
#     l.remove(1)

# print(l)
a = []

while True:
    x = input('輸入e就離開程式,請輸入想新增的資料:')
    if x == 'e':
        break
    else:
        a.append(x)
        print(a)

while True:
    x = input('輸入e就離開程式,請輸入想x的資料:')
    if x == 'e':
        break
    else:
        while x in a:
            a.remove(x)

        print(a)
k = []
for i in a:
    if i in k:
        continue
    else:
        k.append(i)
for i in k:
    print(f'{i}有{l.count(i)}個')
