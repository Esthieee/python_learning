## 列表  
### 列表方法  
|序号|方法|作用|
|:---:|:---:|:---:|
|1|list.append(obj)|在列表末尾添加新的对象|
|2|list.count(obj)|统计某个元素在列表中出现的次数|
|3|list.extend(seq)|在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）|
|4|list.index(obj)|从列表中找出某个值第一个匹配项的索引位置|
|5|list.insert(index, obj)|将对象插入列表|
|6|list.pop([index=-1])|移除列表中的一个元素（默认最后一个元素），并且返回该元素的值|
|7 |list.remove(obj)|移除列表中某个值的第一个匹配项|
|8|list.reverse()|反向列表中元素|
|9|list.sort( key=None, reverse=False)|对原列表进行排序|
|10|ist.clear() |清空列表|
|11|list.copy() |复制列表|  

## 字典  
### 字典方法  
|序号|方法|作用|
|:---:|:---:|:---:|
|1|dict.clear()|删除字典内所有元素
|2|dict.copy()|返回一个字典的浅复制|
|3|dict.fromkeys()|创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值|
|4|dict.get(key, default=None)|返回指定键的值，如果键不在字典中返回 default 设置的默认值|
|5|key in dict|如果键在字典dict里返回true，否则返回false|
|6|dict.items()|以列表返回可遍历的(键, 值) 元组数组|
|7|dict.keys()|返回一个迭代器，可以使用 list() 来转换为列表|
|8|dict.setdefault(key, default=None)|和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default|
|9|dict.update(dict2)|把字典dict2的键/值对更新到dict里|
|10|dict.values()|返回一个迭代器，可以使用 list() 来转换为列表|
|11|pop(key[,default])|删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。|
|12|popitem()|随机返回并删除字典中的最后一对键和值。|  
---  

### 猜数字练习  
```python  
import getpass #先导入getpass
card = int(getpass.getpass("请输入数字：")) #设置答案
print(type(card))
count = 0 #count起始为0

while True: #设置while循环
    if count <3: #设置循环次数
        user_guess = int(input("请猜一猜：")) #用户输入数字
        print(type(user_guess))
        if card == user_guess: #如果用户输入数字等于答案
            print("恭喜你答对了！")
            break #结束循环
        elif card > user_guess: #如果用户输入数字小于答案
            print("小了小了")
        else: #如果用户输入数字大于答案
            print("大了大了")
    else: #次数用完
        print("猜不中，没机会了")
        break #结束循环
    count = count + 1 #每次循环count数加一
```  
---  
### 课本练习  
#### 1.
```python
found = {} #建立一个空字典
#初始化键 必须初始化！！
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
```  
#### 2.  
```python
vowels = ['a','e','i','o','u']
word = input("请输入一个英文单词：")

found = {} #建立一个空字典

for letter in word: #利用迭代计算单词中元音字母出现次数
    if letter in vowels:
        found.setdefault(letter, 0) #利用.setdefault来设置初始值避免出现keyerror
        found[letter] += 1 #若某个字母在条件内则增加记数

for k, v in sorted(found.items()): #利用循环迭代访问数据
    print(k,'出现了',v,'次')
```  
#### 3.  
```python
vowels = set('aeiou') #用set函数创建集合
word = input("请输入单词：") #为word变量赋值

u = vowels.union(set(word)) #将word中的值转换为一个字母对象集合（在转换中会删除所有重复对象）

u_list = sorted(list(u)) #用sorted和list函数将集合转换为有序列表

d = vowels.difference(set(word)) #用difference函数将vowels与set(word)中的对象进行比较，再将两者不重复的对象加入到d集合中

i = vowels.intersection(set(word)) #intersection将两者中相同的对象加入到i集合中

found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)
```
#### 4. 
```python
# 在jupyter notebook中已经运行得到的数据
results =[{'faceId': '360fc287-bc83-439c-b5ca-da9a0a9c226c',
  'faceRectangle': {'top': 92, 'left': 207, 'width': 54, 'height': 54},
  'faceAttributes': {'smile': 0.831,
   'gender': 'male',
   'age': 42.0,
   'glasses': 'ReadingGlasses',
   'hair': {'bald': 0.03,
    'invisible': False,
    'hairColor': [{'color': 'black', 'confidence': 1.0},
     {'color': 'brown', 'confidence': 0.94},
     {'color': 'gray', 'confidence': 0.87},
     {'color': 'other', 'confidence': 0.22},
     {'color': 'blond', 'confidence': 0.01},
     {'color': 'red', 'confidence': 0.01},
     {'color': 'white', 'confidence': 0.0}]}}},
 {'faceId': '64eb7f8f-7961-4dd5-8dc4-aed1716e4e0a',
  'faceRectangle': {'top': 136, 'left': 414, 'width': 45, 'height': 45},
  'faceAttributes': {'smile': 1.0,
   'gender': 'female',
   'age': 15.0,
   'glasses': 'NoGlasses',
   'hair': {'bald': 0.15,
    'invisible': False,
    'hairColor': [{'color': 'black', 'confidence': 1.0},
     {'color': 'brown', 'confidence': 0.85},
     {'color': 'gray', 'confidence': 0.42},
     {'color': 'other', 'confidence': 0.26},
     {'color': 'blond', 'confidence': 0.15},
     {'color': 'red', 'confidence': 0.02},
     {'color': 'white', 'confidence': 0.0}]}}},
 {'faceId': '8f925af7-320b-4331-8f5f-2c579069c24b',
  'faceRectangle': {'top': 132, 'left': 336, 'width': 45, 'height': 45},
  'faceAttributes': {'smile': 1.0,
   'gender': 'female',
   'age': 35.0,
   'glasses': 'NoGlasses',
   'hair': {'bald': 0.03,
    'invisible': False,
    'hairColor': [{'color': 'black', 'confidence': 1.0},
     {'color': 'brown', 'confidence': 0.84},
     {'color': 'other', 'confidence': 0.46},
     {'color': 'gray', 'confidence': 0.28},
     {'color': 'red', 'confidence': 0.04},
     {'color': 'blond', 'confidence': 0.02},
     {'color': 'white', 'confidence': 0.0}]}}},
          ]

face = {
    'person1' : {
    '性别' : results[0]['faceAttributes']['gender'],
    '年龄' : results[0]['faceAttributes']['age'],
    '是否戴眼镜' : results[0]['faceAttributes']['glasses'],
    '头发颜色' : results[0]['faceAttributes']['hair']['hairColor'][0]['color'],
    '微笑指数' : results[0]['faceAttributes']['smile'],
    },
    'person2' : {
    '性别' : results[1]['faceAttributes']['gender'],
    '年龄' : results[1]['faceAttributes']['age'],
    '是否戴眼镜' : results[1]['faceAttributes']['glasses'],
    '头发颜色' : results[1]['faceAttributes']['hair']['hairColor'][0]['color'],
    '微笑指数' : results[1]['faceAttributes']['smile'],   
    },
    'person3' : {
    '性别' : results[2]['faceAttributes']['gender'],
    '年龄' : results[2]['faceAttributes']['age'],
    '是否戴眼镜' : results[2]['faceAttributes']['glasses'],
    '头发颜色' : results[2]['faceAttributes']['hair']['hairColor'][0]['color'],
    '微笑指数' : results[2]['faceAttributes']['smile'],
    },
}

print(face)
```