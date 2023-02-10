from collections import defaultdict
from goody import type_as_str
import prompt

class Bag:
    def __init__(self,values=[]):
        self.counts = defaultdict(int)
        for v in values:
            self.counts[v] += 1

    
    def __str__(self):
        return 'Bag('+', '.join([str(k)+'['+str(v)+']' for k,v in self.counts.items()])+')'


    def __repr__(self):
        param = []
        for k,v in self.counts.items():
            param += v*[k]
        return 'Bag('+str(param)+')'


    def __len__(self):
        return sum(self.counts.values())

        
    def unique(self):
        return len(self.counts)

        
    def __contains__(self,v):
        return v in self.counts

    
    def count(self,v):
        return self.counts[v] if v in self.counts else 0


    def add(self,v):
        self.counts[v] += 1
 
    
    def __add__(self,right):
        if type(right) is not Bag:
            raise TypeError("TypeError: unsupported operand type(s) for +: '"+str(type(self))+"' and'"+str(type(right))+"'")
        return Bag([v for v in self]+[v for v in right])

    
    def remove(self,v):
        if v in self.counts:
            self.counts[v] -= 1
            if self.counts[v] == 0:
                del self.counts[v]
        else:
            raise ValueError('Bag.remove('+str(v)+'): not in Bag')


    def _same(self,right):
        if len(self) != len(right):
            return False
        else:
            for i in self.counts:
                # check not it to avoid creating count of 0 via defaultdict
                if i not in right or self.counts[i] != right.counts[i]:
                    return False
            return True
    
 
    def __eq__(self,right):
        if type(right) != Bag:
            return False
        else:
            return self.counts == right.counts
            #return self._same(right)
        

    def __ne__(self,right):
        return not (self == right)


    def __iter__(self):
        def do_it(counts):
            for k,v in counts.items():
                for _i in range(v):
                    yield k  
        return do_it(dict(self.counts))
    
    
if __name__ == '__main__':
    
    #Simple tests before running driver
    #Put your own test code here to test Bag before doing the bsc tests
    #Debugging problems with these tests is simpler

    b = Bag(['d','a','d','b','c','b','d'])
    print(repr(b))
    print(all((repr(b).count('\''+v+'\'')==c for v,c in dict(a=1,b=2,c=1,d=3).items())))
    for i in b:
        print(i)

    b2 = Bag(['a','a','b','x','d'])
    print(repr(b2+b2))
    print(str(b2+b2))
    print([repr(b2+b2).count('\''+v+'\'') for v in 'abdx'])
    b = Bag(['a','b','a'])
    print(repr(b))
    print()
    
    import driver
    driver.default_file_name = 'bscp21W20.txt'
#     driver.default_show_exception = prompt.for_bool('Show exceptions when testing',True)
#     driver.default_show_exception_message = prompt.for_bool('Show exception messages when testing',True)
#     driver.default_show_traceback = prompt.for_bool('Show traceback when testing',True)
    driver.driver()
