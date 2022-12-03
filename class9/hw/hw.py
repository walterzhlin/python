# 每回合顯示功能選單：
# 1. 新增餐點：印出菜單，請使用者輸入餐點編號，可以重複輸入一樣的餐點
# 2. 移除餐點：移除使用者輸入名稱的所有餐點
# 3. 提交菜單：顯示每樣餐點的名稱及數量後關閉系統
juices = ["蘋果汁", "柳橙汁", "葡萄汁"]
my_list = []

while True:
    print('目前已點的餐:{}'.format(my_list))
    print("1. 新增餐點")
    print("2. 移除餐點")
    print("3. 提交菜單")
    s = input("請輸入功能選項:")
    print("==========================")
    if s == '1':
        while True:
            for j in range(len(juices)):
                print("{}. {}".format(j + 1, juices[j]))

            try:
                ans = int(input("請輸入餐點編號:"))
            except:
                print("請輸入數字編號")
            else:
                if ans > len(juices):
                    print("輸入錯誤查無此餐點，請重新輸入餐點編號")
                else:
                    print("您點的商品是:{}".format(juices[ans - 1]))
                    my_list.append(juices[ans - 1])
                    break
    elif s == '2':
        ans = input("請輸入想移除的餐點完整名稱:")
        while ans in my_list:
            my_list.remove(ans)
        print('移除完成')
    elif s == '3':
        print('您點的餐點為')
        for j in juices:
            if j in my_list:
                print("{}:{}".format(j, my_list.count(j)))
        print('菜單已提交囉!')
        break
    else:
        print('查無此功能請重新輸入!')
    print("==========================")
