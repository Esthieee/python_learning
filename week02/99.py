for i in range (1, 10):
    for j in range (1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
        # \t为横向制表符，口诀之间的分隔；end=''作每段的分隔
    print()
    # 换行

# 第二种
for o in range (1,10):
    for p in range (1,o+1):
        print("%dx%d=%d" %(o,p,o*p),end='\t')
    print()

#试下倒过来
for m in range(1,10):
    for n in range(1,m):
        print(end="\t"*2)
    for k in range (10-m,0,-1):
        print("%dx%d=%d"%((10-m),k,(10-m)*k),end='\t')
    print()

#不试了好累啊