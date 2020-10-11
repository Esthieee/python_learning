# 别练了头都大了

import os
import sys

#1
s = input('请输入内容：')
dic = {'letter': 0, 'number': 0, 'space': 0, 'other': 0}
for i in s:
    if i > 'a' and i < 'z' or i > 'A' and i < 'Z':
        dic['letter'] += 1
    elif i in '0123456789':
        dic['number'] += 1
    elif i == ' ':
        dic['space'] += 1
    else:
        dic['other'] += 1

print('统计：', s)
print(dic)
for key, value in dic.items():
    print('%s=' % key, value)

#2
vote = {}

