from collections import Counter

names = ["野原新之助","野原美伢","野原广志","野原向日葵","小白","野原新之助","风间彻","樱田妮妮","佐藤正南","阿呆","野原新之助"]
renames = []
num = {}

for name in names:
    if names.count(name)>1:
        renames.append(name)
        num[name] = names.count(name)
    else:
        break

print(renames)
print(num)