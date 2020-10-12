### 标准库、开源模块&自定义模块
#### - 标准库
像我们用到的getcwd等的这类指令，它们被称作函数。而这些函数首先会被储存在如os一样的模块里，运用函数我们就需要从模块中调用。就像数以百计的函数组成了数以百计的模块一样，标准库就是各个模块组成的一个合集，它就像是存放着各类书的图书馆一样。
#### - 开源模块
模块是包含定义的函数和变量的文件，后续名是 .py。模块分为三种，开源模块是其中一种，也就是不是出自官方而是出自第三方之手的模块组件。
#### - 自定义模块
自定义模块就是自己定制的模块，diy产品。
### Python是一种怎样的语言
在我看来Python是一种大概可能应该比较容易入门的语言。简洁的代码和其它可以跨平台、方便移植、扩展性很强的属性让Python就像一款“胶水语言”
### 模块查询
- import sys - 导入sys模块
- sys.platform - 查询当前使用平台的名称
- print（sys.version) - 打印输出当前python版本信息
- getcwd - 查询当前代码所在文件夹的名称
- environ - 访问系统的全部环境变量
- date - 日期
- today - 今天
- today().day/month/year - 今天的日月年
- date.isoformat - 将日期转换成字符串
- strftime - 大概是指定时间显示的格式吧
> %H:%M - 24小时制显示  
> %A - 星期几  
> %p - AM还是PM  

![我的查询运行](https://s1.ax1x.com/2020/09/20/wTZBwt.jpg)  

### if、else、elif
- if - 赋予一个条件
- else - 不符合if条件的另一种状况
- elif - 在赋予了if条件后再新增条件，相当于else if
### 代码块
一个模块、一个函数、一个类、一个文件等都是代码块  
### 迭代
相当于for循环
### for循环、range循环
- for循环 - 循环对象集里的内容
- range循环 - 给予运行次数范围，指定循环次数
### random、time模块
- random模块 - 生成随机数
> randint - 生成整数随机数
- time模块
> sleep - 暂停指定秒数时间  
### 对象  
在Python中，一切都是对象，不论是数字、字符串、函数、模块。  
对象可以有*状态*和*行为*  
### 内置数据结构  
1. 列表 - 有序的可变对象集合  
列表是*动态*的，可以根据需要扩展或收缩；列表使*可变*的，可以在任何时间增加、删除或修改对象来修改列表。  
2. 元组 - 有序的不可变对象集合  
一旦向元组赋对象，任何情况下这个元组都不能再改变。  
3. 字典 - 无序的键/值对集合  
在字典中每个唯一键有一个与之关联的值，字典可以包含多个键/值对。与键关联的值可以是任意对象。  
使用字典时要注意不能依赖解释器所用的内部顺序，因为在字典中增加键/值对时可能有一个顺序，但字典不会保存这个顺序。  
4. 集合 - 无序的唯一对象集合  
集合是一种很方便的数据结构，可以用来保存相关对象的一个集合，同时确保其中的任何对象不会重复。  

### 列表  
列表总是用中括号包围  
``` odds = [1, 3, 5] ```这是一个集合  
列表中的内容可以是数字、字符串，也可以是一个列表的列表  

#### 扩展列表  
如果我们想在一个已有的列表中添加对象，这是我们可以通过使用.append()来实现操作  
```  
found = []  
# 一个空列表  
found.append['a']  
# 往列表中添加一个新对象  
len(found)  
# 再使用"len"函数来检查列表  
found = ['a']  
# 这时就会发现原本的空列表中新增了一个对象
```  
#### in  
我们可以通过利用in操作符检查一个对象是否包含在一个集合中，还可以用not in来检查是否不在集合中  
```  
# 一个示例操作
vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milkways"  
found = []  
for letter in word:  
# 循环word  
    if letter in vowels:  
	# 检查word中的字母是否有存在于vowels列表中相同的  
	    if letter not in vowels:  
		# 检查word中的字母是否有不存在于vowels列表中相同的
		    found.append(letter)
			# 如果有不存在的，就往found中添加该对象  
for vowel in found:  
    print(vowel)  
```  
#### 管理列表的4个方法
1. 删除对象 - remove  
remove方法会从列表中删除指定数据值的第一次出现。如果在列表中找到了该值，就会从列表中删除包含这个值的对象；反之报错。  
```  
nums = [1,2,3,4]  
nums.remove(3)  
>>>>>  
nums  
[1,2,4]  
```  
2. 弹出对象 - pop  
使用pop，我们可以从某个特定的索引槽删除一个对象  
```  
nums = [1,2,3,4]  
nums.pop()
# 若括号中不输入值则默认为0，弹出列表中第一位对象  
>>>>>>  
nums  
[2,3,4]  
nums.pop(2)  
>>>>>>  
nums  
[2,3]
```  
3. 扩展列表 - extend  
用extend可以往列表中新增对象，也可以合并两个列表  
```  
nums = [2]  
nums.extend([3,4])  
>>>>>>  
nums  
[2,3,4]
```  
4. 插入对象 - insert  
同pop相似，insert可以将一个对象插入到列表中指定索引值的后面。  
```  
nums = [2,3,4]  
nums.insert(0,1)  
>>>>>>  
nums  
[1,2,3,4]
```  

一个小练习  
```  
phrase = "Don't panic!"  
plist = list(phrase)  
# 将字符串转换为列表  
print(phrase)  
print(plist)  
# 这里要将列表中的Don't panic!转换成on tap  
for i in range(4):  
    plist.pop()  
	# 这里首先利用for循环，将末尾四个对象(nic!)弹出 此时 = Don't pa  
plist.pop(0)  
# 将第一位对象D弹出  此时 = on't pa  
plist.remove("'")  
# 指定删除“'" 此时 = ont pa  
plist.extend([plist.pop(), plist.pop()])
# 因为extend是往列表最后添加对象，所以此时第一个pop弹出的是末尾的a,然后第二个pop弹出变成末尾的p。在弹出完成后，extend再依照顺序将这两个对象重新添加回列表 此时 = ont ap  
plist.insert(2,plist.pop(3))
# 这里先将" "弹出，然后在指定位置将" "插入  此时已经得到on tap  
new_phrase = ''.join(plist)  
# 将plist转换成字符串  
print(plist) # ['o','n',' ','t','a','p']
print(new_phrase) # on tap 
```  
#### copy  
当我们想要复制列表时。可以使用copy  
```  
first = [1,2,3]  
third = first.copy()  
>>>>>>  
third = [1,2,3]
```  
#### 括号记法  
[ start : stop : step ]  
start起始值：允许你控制范围从哪里开始，默认值为0  
stop结束值：允许你控制范围何时结束，不指定则取列表允许最大  
step步长值：允许你控制范围如何生成，默认值为1  
#### 列表切片  
通过利用括号记法，我们可以在**不破坏**列表的前提下对列表进行切片
```  
phrase = "Don't panic!"  
plist = list(phrase)  
print(phrase)  
print(plist)  
new_phrase = ''.join(plist[1:3])  
# 先将列表中的on进行切片再转化成字符串赋值给new_phrase  
new_phrase = new_phrase + ''.join([plist[5],plist[4],plist[7],plist[6]])  
# 利用同样的方法将" tap"也加上  
print(plist) # ['D','o','n',"'",'t',' ','p','a','n','i','c','!']  
print(new_phrase) # on tap  
```  
与上面利用pop、extend、remove、insert相比，列表切片是**非破坏性**的