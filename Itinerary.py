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

def newArray(arr,n): 
    newArr=[]
    for i in range(n):
        for j in range(i+1,n+1):
            newArr.append(sum(arr[i:j]))
    newArr.sort()
    return newArr
            
def getSums(ffrom,fto,newArr):  
    return sum(arr[ffrom-1:fto])      
            
def getInputs():
    tests=int(input())
    for i in range(tests):
        a=[int(x) for x in input().strip().split(" ")]
        n,q=a[0],a[1]
        arr=[int(x) for x in input().strip().split(" ")]
        newArr=newArray(arr, n)
        
        print("Case #"+str(i+1)+": ")
        for j in range(q):
            a=[int(x) for x in input().strip().plit(" ")]
            ffrom,fto=a[0],a[1]
            res=getSums(ffrom,fto,newArr)
            print(res)

if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     test_suite = suite()
#     runner.run(test_suite)
    getInputs()
