d = {}
num = int(input('input number:'))
for i in range(num):
    key = input('input key:')
    value = input('input value:')
    d[key] = value
    print(d)

c = input('input del key:')
a = d.pop(c, '呵呵沒有喔')
print(f'移除:{a}')
