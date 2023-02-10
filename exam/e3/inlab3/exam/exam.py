from ile3helper import ints, primes, is_prime, hide, nth, nth_for_m, Memoize
from collections import defaultdict


def prev_n(iterable, n : int, pred : callable):
    l=[]
    for x in iterable:
        l.append(x)
        if pred(x) and len(l)==1:
                yield l
        elif pred(x) and len(l)<=n:
            yield l
            l=l[1:]
        elif len(l)>=n:
            l=l[1:]
    
    
  





     

def deepest(nl : "int or nested list of int"):
    if type(nl)==int:
        return 0
    elif type(nl)==list:
        d=1
        l=[]
        for x in nl:
            c=d+deepest(x)
            l.append(c)
        d=max(l)
        return d




class check_dict(dict):
    auxiliary_dictionary={}
    def __init__(self,lam1,lam2): 
        dict.__init__(self)
        self.lam1=lam1
        self.lam2=lam2
        
    def __setitem__(self, key,value):
        if self.lam1(key) and self.lam2(value):
            dict.__setitem__(self, key, value)
        else:
            if key in check_dict.auxiliary_dictionary.keys():
                check_dict.auxiliary_dictionary[key].append(value)
            elif key not in check_dict.auxiliary_dictionary.keys():
                dict.__setitem__(check_dict.auxiliary_dictionary,key,[value])

    def __call__(self,key):
        if key in self.keys():
            return self.__getitem__(key)
        elif key in check_dict.auxiliary_dictionary.keys():
            return check_dict.auxiliary_dictionary[key][-1]
        else:
            raise KeyError
        
        
    def  iter_errors(self):
        for x in sorted(check_dict.auxiliary_dictionary.items(),key= lambda x:len(x[1]), reverse=True):
            yield x
            
        

        
        

  

if __name__ == '__main__': 
    '''
    print('Testing prev_n: note that 10th prime 29, and the 200th prime is 1,223,')
    print('  and the 10th prime ending in 13 is 2213. Feel free to test other cases')
    '''
    for i in prev_n(hide([1,2,3,4,5,6,7,8,9]),3,lambda x : x%2==1):
        print(i)
    
    print("list( prev_n(hide([1,2,3,4,5,6,7,8,9]),3,lambda x : x%2==1) )\n  =", list(prev_n([1,2,3,4,5,6,7,8,9],3,lambda x : x%2==1)))
    '''
    print("list( prev_n('a.bcde.f.g.hijk',3,lambda x:x=='.') )\n  =", list(prev_n('a.bcde.f.g.hijk',3,lambda x:x=='.')))
    print("list( prev_n(hide('ab.defghi.klmn.pqrst.vwz.z'),5,lambda x : x=='.') )\n  =", list(prev_n(hide('ab.defghi.klmn.pqrst.vwz.z'),5,lambda x : x=='.')))
    
    print("nth(prev_n(ints(),5,is_prime),10)\n  =", nth(prev_n(ints(),5,is_prime),10))
    print("nth_for_m(prev_n(ints(),5,is_prime),200,3)\n  =", nth_for_m(prev_n(ints(),5,is_prime),200,3))
    print("nth_for_m(prev_n(ints(),5,lambda x : is_prime(x) and x%100==13),10,3)\n  =", nth_for_m(prev_n(ints(),5,lambda x : is_prime(x) and x%100==13),10,3))
    


    print('\n\nTesting deepest: feel free to test other cases')
    print("For deepest([1])                              :",deepest([1]),': should be 1')
    print("For deepest([[1]])                            :",deepest([[1]]),': should be 2')
    print("For deepest([[[1,2,[9,8],[1,3,2]],[1,1]])     :",deepest([[1,2,[9,8],[1,3,2]],[1,1]]),': should be 3')
    print("For deepest([[1,2,[9,[7],8],[1,3,2]],[1,1]])  :",deepest([[1,2,[9,[7],8],[1,3,2]],[1,1]]),': should be 4')
    print("For deepest([[1,2,[9,8],[1,[[7]],3,2]],[1,1]]):",deepest([[1,2,[9,8],[1,[[7]],3,2]],[1,1]]),': should be 5')
    
    
    
    print('\n\nTesting transformkey_dict. Feel free to test other cases')
    d = check_dict(lambda x : type(x) is str,\
                   lambda x : type(x) is int and x >= 0)
    d['a'] = 1       # legal key and value
    d[2] = 2         # illegal key
    d['z'] = -1      # illegal value
    d[2] = 2.5       # illegal key and value
    print(d)
    
    print('d:',d)
    print("d['a']:",d['a'])
    try:
        print("d[2]:",d[2])
        print('should have raised exception')
    except:
        print('correctly raised exception')
    print()
    print("d('a'):",d('a'))
    print("d(2):",d(2))
    print("d('z'):",d('z'))
    try:
        print("d(5):",d(5))
        print('should have raised exception')
    except:
        print('correctly raised exception')
    print()
    print('Iterator over key/value errors')
    for k,v in d.iter_errors():    # __iterator__ shows all keys,values for errors
        print('  error :',repr(k),'->',repr(v))
    
    print()
    print('check_dict with initialization')  
    d2 = check_dict(lambda x : type(x) is str, lambda x : type(x) is int and x >= 0, [('a',1),(2,2)],b=2,c=-3)
    print(d2)
    for k,v in d2.iter_errors():    # __iterator__ shows all keys,values for errors
        print('  error :',repr(k),'->',repr(v))
    '''
    print()
    import driver
    #Uncomment the following lines to see MORE details on exceptions
    driver.default_file_name = 'bscile3F21.txt'
    #But better to debug putting testing code above
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
    driver.driver()
