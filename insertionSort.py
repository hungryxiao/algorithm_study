# -*- coding: cp936 -*-
#插入排序
l = [5,4,2,3,1,8,8,6,9,10]
print len(l)
print l

def insert_sort(l):
    for i in range(1,len(l)):
        print i
        value = l[i]
        while i >= 1 and value < l[i-1]:
            l[i] = l[i-1]
            i -= 1
        l[i] = value
    return l

print insert_sort(l)
