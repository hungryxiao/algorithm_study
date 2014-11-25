# -*- coding: cp936 -*-
#选择排序

testNum = [1,5,3,4,2,9,8,6,7,10]
print testNum

def selectionSort(testNum):
    i = 0
    while i < len(testNum):
        index = i
        j = i+1
        while j < len(testNum):
            if (testNum[j] < testNum[index]):
                index = j
            j += 1
        if (index != i):
            temp = testNum[i]
            testNum[i] = testNum[index]
            testNum[index] = temp
        i += 1
    return testNum

print selectionSort(testNum)