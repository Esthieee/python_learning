vowels = ['a','e','i','o','u']
word = input("请输入一个英文单词：")

found = {} #建立一个空字典

for letter in word: #利用迭代计算单词中元音字母出现次数
    if letter in vowels:
        found.setdefault(letter, 0) #利用.setdefault来设置初始值避免出现keyerror
        found[letter] += 1 #若某个字母在条件内则增加记数

for k, v in sorted(found.items()): #利用循环迭代访问数据
    print(k,'出现了',v,'次')