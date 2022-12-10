# 功能清單
# 1. 新增科目與成績
# 2. 刪除某個科目的成績
# 3. 關閉系統
# 每回合都要顯示目前的成績以及功能清單
d = {}
while True:
    for key, value in d.items():
        print(f'{key}={value}')
    print("1. 新增科目與成績 ")
    print("2. 刪除某個科目的成績")
    print("3. 關閉系統")
    s = input("請輸入功能選項:")
    print("==========================")
    if s == "3":
        break
    elif s == "1":
        key = input('科目:')
        value = input('分數:')
        d[key] = value
    elif s == "2":
        c = input('想刪的科目分數:')
        a = d.pop(c, '呵呵沒有喔')
        print(f'移除:{a}')
    else:
        print("error")