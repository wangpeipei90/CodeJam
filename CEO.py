'''
Created on Feb 16, 2018

@author: peipei
'''
import itertools
from itertools import permutations
# def run(m,n,inputs):
#     ''' inputs: List[[row,col]]'''
#     for i in range(m) 
def getInputs():
    tests=int(input())
    
    for i in range(tests):
        levels=int(input())
        level_emp=dict()
        max_level=levels-1
        for row in range(levels):
            n_emp,level=[int(x) for x in input().split(" ")]
            level_emp[level]=n_emp
            max_level=level if max_level<level else max_level
#         print("max_level:",max_level)
        for level in range(max_level,-1,-1):
            if level in level_emp:
                n_emp=level_emp[level]
                sub_emps=level*n_emp
                sublevel=level-1
#                 print("level: ",level," sub_emps:",sub_emps)
                while sub_emps>0 and sublevel>=0:
                    if sublevel in level_emp:
#                         print("sublevel: ",sublevel, "sub_emp:",level_emp[sublevel])
                        if level_emp[sublevel]>=sub_emps:
                            level_emp[sublevel]-=sub_emps
                            sub_emps=0
#                             continue
                        else:
                            sub_emps-=level_emp[sublevel]
                            level_emp[sublevel]=0
                            
#                             continue
#                         print("sublevel: ",sublevel, "sub_emp:",level_emp[sublevel],"sub_emps:",sub_emps)
                    sublevel-=1
        c_emp=0
        for n_emp in level_emp.values():
            c_emp+=n_emp
                    
        res=max(max_level+1,c_emp)
        print("Case #"+str(i+1)+": "+str(res))
if __name__ == '__main__':
    getInputs()
