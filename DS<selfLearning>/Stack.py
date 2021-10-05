class Stack :
    def __init__(self):
        self.sack =[]
        self.size = -1

    def Max(self):
        try:
            return max(self.stack)
        except :
            return 'out of index'  
        
    def push(self,x):
        self.size += 1
        self.stack.append(x)
        
    def pop(self):
        if not self.stack :
            raise  Empty(' Stack is empty ')
        ## reurn self.arr.pop()
        val = self.stack[-1]
        self.stack = self.stack[:-1]
        return val
    
    def __len__(self):
        return self.size
    
    def isempty(self):
        return self.size == -1
    
    def top(self):
        if not self.stack:
            raise Empty( 'Stack is empty ')
        return self.stack[-1]
    
    def Reversing_Data_Using_a_Stack(self , data = self.stack): 
        reversing_df = []
        while data:
            reversing_df.append(data.pop())
        
        return reversing_df
        
    def build_max(self,val):
        if len(self.stack) == 0:
            self.stack.append(val)
        else:
            currMax = slef.stack[-1]
            self.stack.append(val if val > currMax else currMax)
            
df = [9,8,3,2,4,5,6]
stack = []
for i in df:
    if len(stack) == 0:
        stack.append(val)
    else:
        currMax = stack[-1]
        tack.append(val if val > currMax else currMax)









##### problem link>>>>>>>>  https://www.hackerrank.com/challenges/equal-stacks/problem
#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    l1, l2, l3 = 0, 0, 0
    for each in h1:
        l1 = l1 + each
    for each in h2:
        l2 = l2 + each
    for each in h3:
        l3 = l3 + each
    while l1 !=0 and l2 != 0 and l3 != 0 and (l1!=l2 or l2!=l3):
        if max(l1, l2, l3) == l1:
            l1 = l1 - h1[0]
            h1.pop(0)
        elif max(l1, l2, l3) == l2:
            l2 = l2 - h2[0]
            h2.pop(0)
        else:
            l3 = l3 - h3[0]
            h3.pop(0)
    else:
        if l1==l2 and l2==l3:
            return l1
        else:
            return 0    #
    # Write your code here.
    #






############## https://www.hackerrank.com/challenges/simple-text-editor/submissions/code/145089430

n = int(input())
stack = []
stri = ''
for i in range(n):
    l = list(input().split())
    if(int(l[0]) == 1):
        stri += str(l[1])
        stack.append(len(str(l[1])))
    if(int(l[0]) == 2):
        stack.append(stri[-int(l[1]):])
        stri = stri[:-int(l[1])]
    if(int(l[0]) == 3):
        print(stri[int(l[1]) - 1])                    
    if(int(l[0]) == 4):
        x = stack.pop()
        if(type(x) is int):
            stri = stri[:-x]
        else:
            stri+=x
