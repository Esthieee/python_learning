vowels = set('aeiou') #用set函数创建集合
word = input("请输入单词：") #为word变量赋值

u = vowels.union(set(word)) #将word中的值转换为一个字母对象集合（在转换中会删除所有重复对象）

u_list = sorted(list(u)) #用sorted和list函数将集合转换为有序列表

d = vowels.difference(set(word)) #用difference函数将vowels与set(word)中的对象进行比较，再将两者不重复的对象加入到d集合中

i = vowels.intersection(set(word)) #intersection将两者中相同的对象加入到i集合中

found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)