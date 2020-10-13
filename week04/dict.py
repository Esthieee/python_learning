timetable = {}

while True:
    time = input("请输入星期几第几节课：例：星期一第1-2节")
    course = input("课程：")
    # 用户输入内容加入到字典中

    timetable[time] = course
    repeat = input("是否继续输入？(yes/no)")
    # 询问用户是否要再输入其它信息
    if repeat == 'no':
        break
        # 结束循环

keyinput = input("请输入星期几第几节课：")
if keyinput in timetable:
    print("{key}上{value}".format(key=keyinput, value=timetable[keyinput]))
else:
    print("没课。")

# 我尽力了，我真的不知道怎么还可以输入值返回键


