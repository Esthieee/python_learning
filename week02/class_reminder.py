from datetime import datetime
today = datetime.today().strftime("%A")

if today == 'Monday':
    print("今天有课噢，14：30上界面设计，18：45上毛概实践")
elif today == 'Tuesday':
    print("今天也有课💔，9：45上听说，16：10上广告心理学。")
elif today == 'Wednesday':
    print("怎么今天还有课，8：00上毛概，接着10：35上公选课，晚上18：45还要上python！！")
elif today == 'Thursday':
    print("今天满课886，从8：00开始上五节英语课，14：30上体育之后又上通识，晚上还上api💔")
else:
    print("哈哈！没课！开开心心过大年！")

