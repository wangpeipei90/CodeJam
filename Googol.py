'''
Created on Feb 24, 2018

@author: peipei
'''
import itertools
from itertools import permutations
import unittest
class BugerTest(unittest.TestCase):
    def runTest (self):
        """ Test addition and succeed. """
        s=getK(10)
        ks=[1,2,3,10]
        self.failUnlessEqual(s[ks[0]-1],'0',"fail case 1")
        self.failUnlessEqual(s[ks[1]-1],'0',"fail case 2")
        self.failUnlessEqual(s[ks[2]-1],'1',"fail case 3")
        self.failUnlessEqual(s[ks[3]-1],'0',"fail case 4")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(BugerTest())
    return suite

def orderBuses(n,paths):
    buses=[[paths[2*i],paths[2*i+1]] for i in range(n)]
    buses.sort(key=lambda x:x[0])
    return buses

def getNext(s,n):
    mid=int(len(s)/2)
    s2=list(s)
    s2[mid]='1'
    return s+"0"+"".join(s2)

def getK(k):
    s='0'
    n=1
    while len(s)<k+1:
        s=getNext(s, n)
        n+=1
#         print(n,s)
    return s   
def getInputs():
    tests=int(input())
    ks=[]
    for i in range(tests):
        ks.append(int(input()))
    k=max(ks)
    s=getK(k)
    for i in range(tests):
        print("Case #"+str(i+1)+":",s[ks[i]-1])
if __name__ == '__main__':  
#     runner = unittest.TextTestRunner()
#     test_suite = suite()
#     runner.run(test_suite)
    getInputs()

    