from ile3helper import ints, primes, is_prime, hide, nth, nth_for_m, Memoize
from collections import defaultdict
from goody import irange


def tail(*iterables):
    l=[]
    d={}
    c=1
    for x in iterables:
        itit=iter(x)
        l.append(itit)
    while True:
        for y in l:
            try:
                d[y]=next(y)
            except StopIteration:
                l.remove(y)
                del d[y]
        if len(d)==1 and c==1:
            c=0
        elif len(d)==1 and c==0:
            yield list(d.values())[0]
        if len(d)==0:
            break



    
# Returns whether every character in s occurs an odd number
#  of times. Hint: s.count('a') returns the number of times
#  that 'a' occurs in s. Write this and get some credit.

def all_odd(s : str) -> bool:
    for x in s:
        if s.count(x)%2!=1:
            return False
    return True
    

        


# Memoize min_cuts_odd to speed-up its execution.
@Memoize
def  min_cuts_odd(s : str) -> str:
    poss=[]
    part=''
    if all_odd(s):
        part=part+s
        return part
    elif not all_odd(s):
        for x in range(len(s)):
            if all_odd(s[:x]) and all_odd(s[x:]):
                part=s[:x]+'|'+s[x:]
                poss.append(part)
            else:
                if all_odd(s[:x]):
                    part=s[:x]+'|'+min_cuts_odd(s[x+1:])
                    poss.append(part)
                elif all_odd(s[x:]):
                    part=min_cuts_odd(s[1:x])+'|'+s[x:]
                    poss.append(part)
                else:
                    part=min_cuts_odd(s[1:x])+'|'+min_cuts_odd(s[x+1:])
                    poss.append(part)
                
        return min(poss)
        

     



class transformkey_dict(dict):
    kl=[]
    def __init__(self,f):
        dict.__init__(self)
        self._f=f
        
    def __setitem__(self, k,v):
        k=self._f(k)
        transformkey_dict.kl.append(k)
        dict.__setitem__(self, k,v)
        
    def __getitem__(self, k):
        k=self._f(k)
        transformkey_dict.kl.append(k)
        return dict.__getitem__(self, k)
    
    def __call__(self, k):
        for x in transformkey_dict.kl:
            if k==self._f(x):
                return x

                    

        
  




if __name__ == '__main__': 
    print("min_cuts_odd('ababa')      =", repr(min_cuts_odd('ababa')), '        ... minimal is 2 |s')
    
    '''
    print('\n\nTesting tail')
    print("for tail('abc', 'abcdef', 'ab')... should produce d e f")
    for i in tail('abc', 'abcdef', 'ab'):
        print(' ',i)
        
    print("\nfor tail(hide('abc'), hide('abcdef'), hide([1,2]))... should produce d e f")
    for i in tail(hide('abc'), hide('abcdef'), hide([1,2])):
        print(' ',i)
        
    print("\nfor nth_for_m(tail(hide('abcdef'),ints(),hide('abc')),n=1,m=10)... should produce 7 through 16")
    for i in nth_for_m(tail(hide('abcdef'),ints(),hide('abc')),n=1,m=10):
        print(' ',i)
        
    print("\nfor nth_for_m(tail(hide('abcdef'),ints(),hide('abc')),n=100,m=10)... should produce 106 through 115")
    for i in nth_for_m(tail(hide('abcdef'),ints(),hide('abc')),n=100,m=10):
        print(' ',i)
        
    print("\nfor nth_for_m(tail(hide('abcdef'),ints(),hide('abc')),n=100,m=10)... should produce [106 through 115]")
    print(' ',list(nth_for_m(tail(hide('abcdef'),ints(),hide('abc')),n=100,m=10)))
    

    
    print('\n\nTesting all_odd: the helper function for min_cuts_odd. Feel free to test other cases')
    print("all_odd('')           =", all_odd(''), ' ...no characters, so no violation of all characters odd')
    print("all_odd('a')          =", all_odd('a'))
    print("all_odd('aa')         =", all_odd('aa'))
    print("all_odd('abca')       =", all_odd('abca'))
    print("all_odd('cabcaabcb')  =", all_odd('cabcaabcb'), ' ... 3 as, 3 bs, 3 cs')
    print("all_odd('cabcababcb') =", all_odd('cabcababcb'), '... 3 as, 4 bs, 3 cs')

    
    print('\n\nTesting min_cuts_odd. Feel free to test other cases')
    print("min_cuts_odd('')           =", repr(min_cuts_odd('')), '               ... minimal is 0 |s')
    print("min_cuts_odd('a')          =", repr(min_cuts_odd('a')), '              ... minimal is 0 |s')
    print("min_cuts_odd('aaa')        =", repr(min_cuts_odd('aaa')), '            ... minimal is 0 |s')
    print("min_cuts_odd('aa')         =", repr(min_cuts_odd('aa')), '            ... minimal is 1 |')
    print("min_cuts_odd('aba')        =", repr(min_cuts_odd('aba')), '           ... minimal is 1 |')
    print("min_cuts_odd('ababa')      =", repr(min_cuts_odd('ababa')), '        ... minimal is 2 |s')
    print("min_cuts_odd('aaaabb')     =", repr(min_cuts_odd('aaaabb')), '       ... minimal is 2 |s')
    print("min_cuts_odd('bcaabcab')   =", repr(min_cuts_odd('bcaabcab')), '     ... minimal is 2 |s')
    print("min_cuts_odd('bacacababa') =", repr(min_cuts_odd('bacacababa')), '   ... minimal is 2 |s')
    print("min_cuts_odd('aacbbcca')   =", repr(min_cuts_odd('aacbbcca')), '    ... minimal is 3 |s')
    print("min_cuts_odd('bbaabccbba') =", repr(min_cuts_odd('bbaabccbba')), ' ... minimal is 4 |s')
    print("min_cuts_odd('bbccbbaacc') =", repr(min_cuts_odd('bbccbbaacc')), '... minimal is 5 |s')
    
    
    '''
    print('\n\nTesting transformkey_dict: feel free to use different test cases')
    d = transformkey_dict(str.lower)
    d['aLPHa'] = 1
    d['BetA'] = 2
    d['ALPHA'] += 10
    print("d['alPHA'], d['BEta']:", d['alPHA'], d['BEta'])
    print("d('aLpHa'), d('BeTa'):", d('aLpHa'), d('BeTa'))
    '''
    print('\n\nTesting transformkey_dict: extra credit case')
    d = transformkey_dict(str.lower,[('ALPHA', 1), ('BETA',2)], GAmma=3, delTA = 4)
    print("d['alPHA'], d['BEta'],d['gamma'], d['DELTA']:",d['alPHA'], d['BEta'],d['gamma'], d['DELTA'])
    print("d('alPHA'), d('BEta'),d('gamma'), d('DELTA'):", d('alPHA'), d('BEta'),d('gamma'), d('DELTA'))
   '''


    print()
    import driver
    #Uncomment the following lines to see MORE details on exceptions
    driver.default_file_name = 'bscile3W22.txt'
    #But better to debug putting testing code above
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
    driver.driver()
