item_list = [('暹罗猫',130),
             ('狸花猫',13),
             ('奶牛猫',20),
             ('三花猫',15),
             ('黑猫',100)]

user_list = []

Alipay_balance = input("请输入你的余额：")
if Alipay_balance.isdigit():
    Alipay_balance = int(Alipay_balance)
    while True:
        print("-------♥毛猫列表♥-------")
        for item in item_list:
            print(item_list.index(item), item)
        choice = (input("请输入商品编号："))

        if choice.isdigit():
            choice = int(choice)
            if choice >= 0 and choice < len(item_list):
                if Alipay_balance >= item_list[choice][1]:
                    Alipay_balance = Alipay_balance - item_list[choice][1]
                    print("已获得 %s ，您的余额为 %s "%(item_list[choice][0], Alipay_balance))
                    user_list.append(item_list[choice])

                else:
                    print("购买失败余额不足，请选择其它毛猫或按'q'推出")
            else:
                print("没有这个东西，请选择其它毛猫或按'q'退出")
        elif choice == "q":
            print("------毛猫清单-------")
            for items in user_list:
                print(user_list.count(items), items)
            print("您的余额还有：%s"%(Alipay_balance))
            break
        else:
            print("请输入毛猫编号或按'q'推出")
else:
    print("请输入正确余额")
