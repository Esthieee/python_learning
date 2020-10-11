names = ["野比大雄","哆啦a梦","冈田武"]
print(names)

names.append("骨川小夫")
print(names)

names.insert(1,"源静香")
print(names)

pop_names = names.pop(2)
print(pop_names)
print(names)

names.remove("骨川小夫")
print(names)

names[0] = "出木杉英才"
print(names)

_name = "野比大雄"
if _name in names:
    print(names.index(_name))
else:
    print("%s 不在列表中"%(_name))

print(names)