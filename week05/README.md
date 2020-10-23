### 复制列表  
**.copy()** - 对列表进行浅复制   
```python  
# 例  
a = [1,2,3]  
b = a.copy()  
print(b)
>>>>>
b = [1,2,3]
```  
这样看上去使用copy和用b=a的直接赋值方法差不多，但实际上不同的。  
- #### 复制与赋值的区别
```python   
# 赋值  
a = [1,2,3]  
b = a  
print(a,b)  
>>>>>>  
a = [1,2,3]  
b = [1,2,3]  
a.remove(3)  # 这时如果对列表a进行修改  
print(a,b)  
>>>>>>  
a = [1,2]  
b = [1,2]  # 会看到列表b也同时与a一样改变了  
# 复制  
a = [1,2,3]  
b = a.copy()  
print(a,b)  
>>>>>>  
a = [1,2,3]  
b = [1,2,3]    
a.remove(3)  # 同样再对列表a进行修改  
print(a,b)  
>>>>>>  
a = [1,2]  
b = [1,2,3]  # 这时列表b不再像上面一样也跟着被修改了。
```  
- #### 浅复制与深复制  
| 复制 | 代码 | 介绍 |
| :-----: | :----: | :---: |
| 浅复制 | copy | 拷贝父对象，不会拷贝对象的内部的子对象 |
| 深复制 | deepcopy | 完全拷贝了父对象及其子对象 |  
  + 浅复制  
  ![浅复制](https://www.runoob.com/wp-content/uploads/2017/03/1489720930-6827-Vtk4m.png)  
  + 深复制  
  ![深复制](https://www.runoob.com/wp-content/uploads/2017/03/1489720930-5882-BO4qO.png)  
  
### 列表嵌套  
就是列表中包含列表，有点复杂，以后补充。  

### 列表的切片处理与方法处理的区别  
使用列表方法将一个字符串转换为另一个字符串时，这些列表方法是**破坏性的**，因为这个代码会修改列表的原始状态。  
而列表切片是**非破坏性**的，因为从一个现有列表中抽取对象不会改变原来的列表，元数据仍保持不变。  

 - 列表切片  
 ```python   
 phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase +   ''.join([plist[5],plist[4],plist[7],plist[6]])  
print(plist)
print(new_phrase)  
>>>>>>
plist = ['D', 'o', 'n', "'", 't', ' ', 'p', 'a', 'n', 'i', 'c', '!']  
new_phrase = "on tap"  
```  

- 方法处理  
```python 
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(),plist.pop()])
plist.insert(2, plist.pop(3))
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)  
>>>>>>
plist = ['o', 'n', ' ', 't', 'a', 'p']
new_phrase = "on tap"  
```  

### join  
将序列中的元素以指定的字符连接生成一个新的字符串  
```python   
# 例  
str = "-"  
seq = ("a", "b", "c")  # 字符串序列  
print str.join( seq )   
>>>>>>  
a-b-c
```  

### while  
- while和for循环的区别  

### 元组的基本创建和使用  

### 本周练习  
```python   
item_list = [('暹罗猫',130),  
             ('狸花猫',13),  
             ('奶牛猫',20),  
             ('三花猫',15),  
             ('黑猫',100)]  
  
user_list = [] #首先创建一个物品列表和一个空列表  
  
Alipay_balance = input("请输入你的余额：") #用Input让用户自由输入金额  
if Alipay_balance.isdigit():  
    Alipay_balance = int(Alipay_balance) #将用户输入的数字整数化  
    while True: # 建立一个大的循环  
        print("-------♥毛猫列表♥-------")  
        for item in item_list: #再建立一个for循环开始进入正题  
            print(item_list.index(item), item) #首先打印出商品列表供用户挑选  
        choice = (input("请输入商品编号："))  
        if choice.isdigit():  
            choice = int(choice) #将用户输入的编号数字整数化    
            if choice >= 0 and choice < len(item_list):
                if Alipay_balance >= item_list[choice][1]:
                    Alipay_balance = Alipay_balance - item_list[choice][1]
                    print("已获得 %s ，您的余额为 %s "%(item_list[choice][0], Alipay_balance))
                    user_list.append(item_list[choice])

                else:
                    print("购买失败余额不足，请选择其它毛猫或按'q'推出")
            else:
                print("没有这个东西，请选择其它毛猫或按'q'退出")
        elif choice == "q": #建立如果用户选择退出后的条件语句  
            print("------毛猫清单-------")
            for items in user_list:
                print(user_list.count(items), items) #利用count()来获取物品购入数量  
            print("您的余额还有：%s"%(Alipay_balance)) #将用户购买的物品清单与余额打印出来  
            break #循环结束  
        else:
            print("请输入毛猫编号或按'q'推出")
else:
    print("请输入正确余额") #最外层循环若输入的不是数字则重来  
```  