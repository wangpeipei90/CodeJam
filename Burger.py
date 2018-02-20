'''
Created on Feb 16, 2018

@author: peipei
'''
import itertools
from itertools import permutations
import unittest
class BugerTest(unittest.TestCase):
    def runTest (self):
        """ Test addition and succeed. """
        self.failUnlessEqual(getMinErr1(5,[0,2,1,1,2]),2,"fail case 1")
        self.failUnlessEqual(getMinErr1(1,[0]),0,"fail case 2")
        self.failUnlessEqual(getMinErr1(6,[2,2,2,2,2,2]),10,"fail case 3")
        
        self.failUnlessEqual(getMinErr2(5,[0,2,1,1,2]),2,"fail case 1")
        self.failUnlessEqual(getMinErr2(1,[0]),0,"fail case 2")
        self.failUnlessEqual(getMinErr2(6,[2,2,2,2,2,2]),10,"fail case 3")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(BugerTest())
    return suite

def getDistance(n):
    mid=int(n/2) ## n=6, mid=3 n=7, mid=3
    distance=[x for x in range(mid)]
    if n%2==0: ##[0,1,2,2,1,0]
        distance=distance+distance[::-1]
    else:
        distance=distance+[mid]+distance[::-1]
    
    return distance
    
def getMinErr1(n,optimal):
    ''' complexity: O(nlog(n))
    rearrangement inequality) if x1<x2, y1<y2 then x1y1+x2y2>x1y2+x2y1
    min_error=(x1-y1)^2 +(x2-y2)^2 
    = x1^2+x2^2+y1^2+y2^2 -2x1y1-2x2y2 <(x1-y2)^2+(x2-y1)^2
    '''
    dis=getDistance(n) ##O(n)
    dis.sort()##O(nlog(n))
    optimal.sort()##O(nlog(n))
    
    sq_error=[(dis[i]-optimal[i])**2 for i in range(n)] ##O(n)
    return sum(sq_error) ##O(n)
    
def getMinErr2(n,optimal):  
    ''' complexity O(n! × n) '''
    
    dis=getDistance(n)
    
    min_error=4127283647
    for permutation in itertools.permutations(range(n)):  ###O(n!)
        e=0
        for pos,opt in enumerate(permutation): ##O(n)
            e+=(dis[pos]-optimal[opt])**2        
        min_error=e if e<min_error else min_error
        
    return min_error
            
def getInputs():
    tests=int(input())
    for i in range(tests):
        n=int(input())
        optimal=[int(x) for x in input().split(" ")]
        
        res=getMinErr1(n, optimal)
#         res=getMinErr2(n, optimal)

        print("Case #"+str(i+1)+": "+str(res))
if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     test_suite = suite()
#     runner.run(test_suite)
    getInputs()
