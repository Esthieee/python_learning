vowels = ['a','e','i','o','u']
word = input("请输入一个英文单词：")

found = {} #建立一个空字典
#
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

#found['e'] = found['e'] + 1 #递增e的频度记数
#fouond['e'] += 1 #+=同样能递增e的频度记数，相较上面更为简洁

for letter in word: #利用迭代计算单词中元音字母出现次数
    if letter in vowels:
        found[letter] += 1 #若某个字母在条件内则增加记数

for k, v in sorted(found.items()): #利用循环迭代访问数据
    print(k,'出现了',v,'次')