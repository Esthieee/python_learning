# format1

#name = input("名字：")
#classes = input("课程名称：")
#day = input("星期几：")
#time = input("第几节：")
#info = '''------info ''' + name + ''' -------
#Name:'''+name+'''
#classes:'''+classes+'''
#day:'''+day+'''
#time:'''+time+'''
#'''
#print(info)



#format 2

#name = input("名字：")
#classes = input("课程：")
#day = input("星期几：")
#time = input("第几节：")# info = '''------info ''' + name + ''' -------
# Name:'''+name+'''
# Age:'''+age+'''
# Job:'''+job+'''
# Salary'''+salary+'''
# '''

# print(info)

#info2 =  '''-------INFO OF {0} -------
#Name:{0}
#classes:{1}
#day:{2}
#time:{3}
#'''.format(name,
           #classes,
           #day,
           #time)
#print(info2)


#占位符

name = input("名字：")
classes = input("课程名称：")
day = input("星期几：")
time = input("第几节：")

info_03 = '''------info %s-------
名字:%s
课程名称:%s
星期几:%s
第几节:%s
''' % (name,name,classes,day,time)

print(info_03)