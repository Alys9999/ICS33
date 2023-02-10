import prompt
from helpers import primes, hide, nth, mini_Backwardable_test, Backwardable_test



def running_count(iterable,p):
    dig=0
    for x in iterable:
        if p(x):
            dig+=1
        yield dig

        
            
def stop_when(iterable,p):
    for x in iterable:
        if p(x):
            continue
        else:
            yield x

        

def yield_and_skip(iterable):
    count=0
    for x in iterable:
        if count!=0:
            count-=1
            continue
        if type(x)==int:
            yield x
            count+=x
        elif type(x)==str:
            yield x
        

def windows(iterable,n,m=1):
    part_list=[]
    m_list=[]
    for x in iterable:
        if len(part_list)<m:
            part_list.append(x)
        elif len(m_list)<(n-m):
            m_list.append(x)
        if len(part_list)+len(m_list)==n:
            yield part_list+m_list
            part_list=m_list
            m_list=[]
    
        
        

def alternate(*iterables):
    iterables=[iter(x) for x in iterables]
    while True:
        try:
            for x in iterables:
                yield next(x)
        except StopIteration:
            break
    
def myzip(*iterables):
    while True:
        tu=()
        for x in iterables:
            try:
                tu=tu+(next(x),)
            except StopIteration:
                tu=tu+(None,)
        if tu==(None,None,None):
            break
        yield tu
        
        



class Backwardable:
    def __init__(self,iterable):
        self._iterable = iterable
            
    def __iter__(self):
        class B_iter:
            def __init__(self,iterable):
                self._all      = []
                self._iterator = iter(iterable)
                self._index    = -1 # index of value just returned from __next__ or __prev__
        
            def __str__(self):
                return '_all={}, _index={}'.format(self._all,self._index)
        

            def __next__(self):
                self._index+=1
                try:
                    return self._all[self._index]
                except IndexError:
                    try:
                        obj=next(self._iterator)
                        self._all.append(obj)
                        return obj
                    except StopIteration:
                        self._index-=1
                        raise StopIteration
                

                
            def __prev__(self):
                self._index-=1
                if self._index<0:
                    self._index+=1
                    raise AssertionError
                else:
                    return self._all[self._index]


            
            def __clear__(self):
                if self._all!=[]:
                    self._all=[self._all[self._index]]
                    self._index=0
                else:
                    self._all=[]


            
        return B_iter(self._iterable)

def prev (x): return x.__prev__()
def clear(x): x.__clear__()




if __name__ == '__main__':
    # Test Backwardable; add your own test cases
    '''
    print('\nTesting Backwardable')

    i = iter(Backwardable(primes()))
    print(i)
    print(next(i),i) #a
    print(next(i),i) #b
    print(next(i),i) #c
    print(prev(i),i) #b
    print(prev(i),i) #a
    try:
        print(prev(i),i)
    except AssertionError:
        print('Tried to prev before first value')
    print(next(i),i) #b
    print(next(i),i) #c
    print(clear(i),i)#None: a, b gone]
    print(next(i),i) #d
    print(next(i),i) #e
    print(next(i),i)
    print(prev(i),i) #d
    print(prev(i),i) #c
    try:
        print(prev(i),i)
    except AssertionError:
        print('Tried to prev before first value (after clear)')
    try:
        print(prev(i),i)
    except AssertionError:
        print('Tried to prev before first value (after clear)')
    try:
        print(prev(i),i)
    except AssertionError:
        print('Tried to prev before first value (after clear)')
    print(next(i),i) #d
    print(next(i),i) #e
    try:
        print(next(i),i)
    except StopIteration:
        print('Correctly raised StopIteration')
    print(prev(i),i)
    print(prev(i),i)
    print(next(i),i)
    print(prev(i),i)
    print(prev(i),i)
    print(next(i),i)
    print(clear(i),i)
    print(next(i),i) #a
    print(next(i),i)
    print(prev(i),i)
    print(prev(i),i)
    print(prev(i),i)
    '''
    '''
    # Test running_count; you can add your own test cases
    print('\nTesting running_count')
    for i in running_count('bananastand',lambda x : x in 'aeiou'): # is vowel
        print(i,end=' ')
    print()
    
    for i in running_count(hide('bananastand'),lambda x : x in 'aeiou'): # is vowel
        print(i,end=' ')
    print()
    
    print(nth(running_count(primes(),lambda x : x%10 == 3),1000))
    
    
    # Test stop_when; you can add your own test cases
    print('\nTesting stop_when')
    for c in stop_when('abcdefghijk', lambda x : x >='d'):
        print(c,end='')
    print()

    for c in stop_when(hide('abcdefghijk'), lambda x : x >='d'):
        print(c,end='')
    print('\n')

    print(nth(stop_when(primes(),lambda x : x > 100000),100))
    
    
    # Test group_when; you can add your own test cases
    print('\nTesting yield_and_skip')
    for i in yield_and_skip([1, 2, 1, 3, 'a', 'b', 2, 5, 'c', 1, 2, 3, 8, 'x', 'y', 'z', 2]):
        print(i,end=' ')
    print()
    
    for i in yield_and_skip(hide([1, 2, 1, 3, 'a', 'b', 2, 5, 'c', 1, 2, 3, 8, 'x', 'y', 'z', 2])):
        print(i,end=' ')
    print()

    print(nth(yield_and_skip(primes()),5))
    
    # Test windows; you can add your own test cases
    print(windows('abcdefghijk',4,2))
    print('\nTesting windows')
    for i in windows('abcdefghijk',4,2):
        print(i,end=' ')
    print()
    
    print('\nTesting windows on hidden')
    for i in windows(hide('abcdefghijk'),4,2):
        print(i,end=' ')
    print()
    
    print(nth(windows(primes(),10,5),20))
    
    
    Test alternate; add your own test cases
    print('\nTesting alternate')
    for i in alternate('abcde','fg','hijk'):
        print(i,end='')
    print()
    
    for i in alternate(hide('abcde'), hide('fg'),hide('hijk')):
        print(i,end='')
    print()
       
    for i in alternate(primes(20), hide('fghi'),hide('jk')):
        print(i,end='')
    print()

    print(nth(alternate(primes(),primes()),50))
    
    
    # Test myzip; add your own test cases
    print('\nTesting myzip')
    for i in myzip('abcde','fg','hijk'):
        print(i,end='')
    print()
       
    for i in myzip(hide('abcde'), hide('fg'),hide('hijk')):
        print(i,end='')
    print()
       
    for i in myzip(primes(20), hide('fghi'),hide('jk')):
        print(i,end='')
    print('\n')
       
    print(nth(myzip(primes(),primes()),50))
       
    
    
    # Test Backwardable; add your own test cases
    print('\nTesting Backwardable')
    s = 'abcde'
    i = iter(Backwardable(s))
    print(i)
    print(next(i),i) #a
    print(next(i),i) #b
    print(next(i),i) #c
    print(prev(i),i) #b
    print(prev(i),i) #a
    try:
        print(prev(i),i)
    except AssertionError:
        print('Tried to prev before first value')
    print(next(i),i) #b
    print(next(i),i) #c
    print(clear(i),i)#None: a, b gone]
    print(next(i),i) #d
    print(next(i),i) #e
    print(prev(i),i) #d
    print(prev(i),i) #c
    try:
        print(prev(i),i)
    except AssertionError:
        print('Tried to prev before first value (after clear)')
    print(next(i),i) #d
    print(next(i),i) #e
    try:
        print(next(i),i)
    except StopIteration:
        print('Correctly raised StopIteration')
    
    # See the mini_Backwardable_test code, which allows you to call
    #  interleaved sequences of next and prev, or quit
    mini_Backwardable_test(iter(Backwardable('abc')))
    mini_Backwardable_test(iter(Backwardable([0,1,2,3,4])))
    mini_Backwardable_test(iter(Backwardable(primes())))
    '''
    
    import driver
    driver.default_file_name = 'bscq4W22.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
    
    
