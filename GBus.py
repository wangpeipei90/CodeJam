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
        a=orderBuses(4,[15, 25, 30, 35, 45, 50, 10, 20])
        b=orderBuses(10,[10,15,5,12,40,55,1,10, 25, 35, 45, 50, 20, 28, 27, 35, 15, 40, 4, 5])
        self.failUnlessEqual(a,[[10,20],[15,25],[30,35],[45,50]],"fail case -1")
        self.failUnlessEqual(b,[[1,10],[4,5],[5,12],[10,15],[15,40],[20,28],[25,35],[27,35],[40,55],[45,50]],"fail case 0")
        self.failUnlessEqual(getBuses(a,15),2,"fail case 1")
        self.failUnlessEqual(getBuses(a,25),1,"fail case 2")
        self.failUnlessEqual(getBuses(b,5),3,"fail case 3")
        self.failUnlessEqual(getBuses(b,10),3,"fail case 1")
        self.failUnlessEqual(getBuses(b,27),4,"fail case 2")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(BugerTest())
    return suite

def orderBuses(n,paths):
    buses=[[paths[2*i],paths[2*i+1]] for i in range(n)]
    buses.sort(key=lambda x:x[0])
    return buses

def getBuses(buses,city):
    count=0
    for c_bus in buses:
        c_from,c_end=c_bus[0],c_bus[1]
        if c_from<=city and city<=c_end:
            count+=1
        elif city<c_from:
            break
    return count
def getInputs():
    tests=int(input())
    for i in range(tests):
        n=int(input())
        paths=[int(x) for x in input().strip().split(" ")]
        buses=orderBuses(n, paths)
        
        q=int(input())
        citiesQ=[int(input()) for x in range(q)]
        res=[getBuses(buses,city) for city in citiesQ]
        input()
        s=" ".join([str(count) for count in res])
        print("Case #"+str(i+1)+":",s)
if __name__ == '__main__':  
#     runner = unittest.TextTestRunner()
#     test_suite = suite()
#     runner.run(test_suite)
    getInputs()