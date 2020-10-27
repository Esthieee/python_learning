import getpass
card = int(getpass.getpass("请输入数字："))
print(type(card))
count = 0

while True:
    if count <3:
        user_guess = int(input("请猜一猜："))
        print(type(user_guess))
        if card == user_guess:
            print("恭喜你答对了！")
            break
        elif card > user_guess:
            print("小了小了")
        else:
            print("大了大了")
    else:
        print("猜不中，没机会了")
        break
    count = count + 1