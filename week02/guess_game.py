import random
import time

name = input("你想祝福谁")
today = time.strftime("%A")

m = ["新的一周，新的苦难，祝您快乐！", "周一快乐，搬砖加油！", "早安，周一。美好祝福送给您。"]
md = random.choice(m)
t = ["祝您周二快乐。", "再次祝您周二快乐。", "周二唔准唔开心。"]
td = random.choice(t)
w = ["一周已过去一半，你还好吗？", "还有两天周五，加油！"]
wd = random.choice(w)
ts = ["周四了周四了，祝你周四快乐！", "还有一天！一天！！加油！", "周四，为您送上简单祝福。"]
tsd = random.choice(ts)
f = ["周五，祝您五福临门。", "今晚约定你！", "今天周五，开开心心过大年。"]
fd = random.choice(f)
s = ["美好的周六，为您送上美好祝福。", "周六，还可以睡一天的懒觉♥"]
sd = random.choice(s)
su = ["周日，再次送上简单的祝福。", "收拾收拾心情准备搬砖。"]
sud = random.choice(su)

if today == 'Monday':
    print(name,"，",md)
elif today == 'Tuesday':
    print(name,"，",td)
elif today == 'Wednesday':
    print(name,"，",wd)
elif today == "Thursday":
    print(name,"，",tsd)
elif today == 'Friday':
    print(name,"，",fd)
elif today == 'Saturday':
    print(name,"，",sd)
else:
    print(name,"，",sud)

#好累啊我祝我自己可以写个python帮我写python