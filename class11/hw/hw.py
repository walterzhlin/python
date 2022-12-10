d = {}


def add_score():
    global d
    key = input('科目:')
    value = input('分數:')
    d[key] = value


def remove_score():
    global d
    c = input('想刪的科目分數:')
    a = d.pop(c, '呵呵沒有喔')
    print(f'移除:{a}')


while True:
    for key, value in d.items():
        print(f'{key}={value}')
    print("1. 新增科目與成績 ")
    print("2. 刪除某個科目的成績")
    print("3. 關閉系統")
    s = input("請輸入功能選項:")
    print("==========================")
    if s == "1":
        add_score()
    elif s == "2":
        remove_score()
    elif s == "3":
        break

    else:
        print("error")
