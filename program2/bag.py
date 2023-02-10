
from collections import defaultdict
from goody import type_as_str
import prompt

class Bag:
    def __init__(self,inp=[]):
        self.content={}
        self.content=dict((x,inp.count(x)) for x in inp if x not in self.content)
    def __repr__(self):
        pr_str=[x for x in ''.join(list((str(x[0]))*x[1] for x in self.content.items()))]
        return 'Bag('+str(pr_str)+')'
    def __str__(self):
        s=''.join(list((str(x[0])+'['+ str(x[1])+']') for x in self.content.items() if len(self.content.items())!=0))
        return 'Bag('+s+')'
    def __len__(self):
        return sum(x for x in self.content.values())
    def unique(self):
        return len(self.content.keys())
    def count(self,right):
        if right not in self.content.keys():
            num = 0
        else:
            num = self.content[right]
        return num
    def add(self,right):
        if right in self.content.keys():
            self.content[right]+=1
        else:
            self.content[right]=1
    def remove(self,right):
        #seems work correctly but did not pass the bsc test in line 80
        #fixed
        if right in self.content.keys() and self.content[right]>0:
            self.content[right]-=1
            if self.content[right]<=0:
                del self.content[right]
        else:
            raise ValueError(f'{right} is not a valid item to be removed')
    def __contains__(self,candd):
        '''FIXED: Correct, Before did not return a True or False only printed a value'''
        if candd in self.content.keys():
            return True
        else:
            return False
    def __add__(self, right):
        '''FIXED: Correct, Before was missing the else part of the conditional'''
        if type(right)!=Bag:
            raise TypeError ('invalid object type ')
        else:
            list1=[items for items in ''.join(list((key)*value for key, value in self.content.items()))]
            list2=[items for items in ''.join(list((key)*value for key, value in right.content.items()))]
            newlist=list1+list2
            return Bag(newlist)
    def __eq__(self,right):
        print(self.content)
        '''FIXED: Correct, Before was missing the False conditional for if the type was not equal to a bag'''
        if type(right)==Bag:
            return self.content==right.content
        else:
            return False
    def __ne__(self,right):
        '''FIXED: Correct, Before certain test cases returned the wrong boolean'''
        if type(right)!=Bag:
            return True
        else:
            return self.content!=right.content
    def __iter__(self):
        #fixed
        pr_str=[x for x in ''.join(list((str(x[0]))*x[1] for x in self.content.items()))]
        return (x for x in pr_str)
    
        





if __name__ == '__main__':
    
    #Simple tests before running driver
    #Put your own test code here to test Bag before doing the bsc tests
    #Debugging problems with these tests is simpler

    
    b = Bag(['d','a','d','b','c','b','d'])
    print(repr(b))
    print(all((repr(b).count('\''+v+'\'')==c for v,c in dict(a=1,b=2,c=1,d=3).items())))
    for i in b:
        print(i)
    #b2 = Bag(['a','a','b','x','d'])
    #print(repr(b2+b2))
    #print(str(b2+b2))
    #print([repr(b2+b2).count('\''+v+'\'') for v in 'abdx'])
    #b = Bag(['a','b','a'])
    #print(repr(b))
    #print()
    

        
    import driver
    driver.default_file_name = 'bscp21W22.txt'
#     driver.default_show_exception = prompt.for_bool('Show exceptions when testing',True)
#     driver.default_show_exception_message = prompt.for_bool('Show exception messages when testing',True)
#     driver.default_show_traceback = prompt.for_bool('Show traceback when testing',True)
    driver.driver()
