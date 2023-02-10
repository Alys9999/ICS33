from ile3helper import ints, primes, is_prime, hide, nth, nth_for_m, Memoize
from collections import defaultdict
from goody import irange


def tail(*iterables):
    iters = [iter(i) for i in iterables]
    while len(iters) > 1:
        for _ in range(len(iters)):
            it = iters.pop(0)
            try:
                last = next(it)    # skip append if next raises exception
                iters.append(it)
            except:
                pass
    yield last
    for i in iters[0]:
        yield i

#     iters = [iter(i) for i in iterables]
#     while len(iters) > 1:
#         new_iters = []
#         for it in iters:
#             try:
#                 last  = next(it)      # skip append if next raises exception
#                 new_iters.append(it)
#             except:
#                 pass
#         iters = new_iters
#     yield last
#     for i in iters[0]:
#         yield i
    
     



# Returns whether every character in s occurs an odd number
#  of times. Hint: s.count('a') returns the number of times
#  that 'a' occurs in s. Write this and get some credit.

def all_odd(s : str) -> bool:
    return all(s.count(a)%2 == 1 for a in set(s))

# Memoize min_cuts_odd to speed-up its execution.
@Memoize
def  min_cuts_odd(s : str) -> str:
    if all_odd(s):
        return s
    else:
        return min(
                   [min_cuts_odd(s[0:i])+'|'+ min_cuts_odd(s[i:]) for i in range(1,len(s))], 
                   key = lambda x : x.count('|')) # could just use len(x) since min #| == min length




class transformkey_dict(dict):
    def __init__(self,transform,initial_dict=[],**kargs):
        dict.__init__(self,                      # call to initialize base-class
                      [(transform(k),v) for k,v in initial_dict],
                      **{transform(k): v for k,v in kargs.items()})
        self._transform = transform              # used in overridden methods
        self._original_keys = {transform(k):k for k,_ in initial_dict}  # used in overridden methods
        self._original_keys.update({transform(k):k for k in kargs.keys()})
          
    # define __str__ any way that will help you debugging
    def __str__(self):
        return dict.__str__(self) +' + ' + str(self._original_keys)   
         
    def __getitem__(self,key):
        return dict.__getitem__(self,self._transform(key))

    def __setitem__(self,key,value):
        if self._transform(key) not in self:
            self._original_keys[self._transform(key)] = key
        dict.__setitem__(self,self._transform(key),value)

    def __call__(self,key):
        return self._original_keys[self._transform(key)]
  

  


if __name__ == '__main__': 
    print('\n\nTesting tail')
    print("for tail('abc', 'abcdef', 'ab')... should produce d e f")
    for i in tail('abc', 'abcdef', 'ab'):
        print(' ',i)
        
    print("\nfor tail(hide('abc'), hide('abcdef'), hide([1,2]))... should produce d e f")
    for i in tail(hide('abc'), hide('abcdef'), hide([1,2])):
        print(' ',i)
        
    print("\nfor nth_for_m(tail(hide('abcdef'),ints(),hide('abc')),1,10)... should produce 7 through 16")
    for i in nth_for_m(tail(hide('abcdef'),ints(),hide('abc')),n=1,m=10):
        print(' ',i)
        
    print("\nfor nth_for_m(tail(hide('abcdef'),ints(),hide('abc')),100,10)... should produce 106 through 115")
    for i in nth_for_m(tail(hide('abcdef'),ints(),hide('abc')),n=100,m=10):
        print(' ',i)
        
    print("\nfor nth_for_m(tail(hide('abcdef'),ints(),hide('abc')),100,10)... should produce [106 through 115]")
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
    
    
    print('\n\nTesting transformkey_dict: feel free to use different test cases')
    d = transformkey_dict(str.lower)
    d['aLPHa'] = 1
    d['BetA'] = 2
    d['ALPHA'] += 10
    print("d['alPHA'], d['BEta']:", d['alPHA'], d['BEta'])
    print("d('aLpHa'), d('BeTa'):", d('aLpHa'), d('BeTa'))
    
    print('\n\nTesting transformkey_dict: extra credit case')
    d = transformkey_dict(str.lower,[('ALPHA', 1), ('BETA',2)], GAmma=3, delTA = 4)
    print("d['alPHA'], d['BEta'],d['gamma'], d['DELTA']:",d['alPHA'], d['BEta'],d['gamma'], d['DELTA'])
    print("d('alPHA'), d('BEta'),d('gamma'), d('DELTA'):", d('alPHA'), d('BEta'),d('gamma'), d('DELTA'))
   


    print()
    import driver
    #Uncomment the following lines to see MORE details on exceptions
    driver.default_file_name = 'bscile3W22.txt'
    #But better to debug putting testing code above
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
    driver.driver()
