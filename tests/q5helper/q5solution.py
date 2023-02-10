def odd(l):
    if len(l)==0:
        return ()
    else:
        if len(l)<3:
            return (l[0],)
        else:
            return (l[0],)+odd(l[2:])



def compare(a,b):
    if len(a)==0 and len(b)==0:
        return '='
    elif len(a)==0 and len(b)!=0:
        return '<'
    elif len(b)==0 and len(a)!=0:
        return '>'
    else:
        if a[0]<b[0]:
            return '<'
        elif a[0]>b[0]:
            return '>'
        elif a[0]==b[0]:
            return compare(a[1:],b[1:])



def get_assoc(assoc : ((object,object),), key : object) -> object:
    if len(assoc)==0:
        raise KeyError
    if key == assoc[0][0]:
        return assoc[0][1]
    else:
        return get_assoc(assoc[1:],key)



def del_assoc(assoc : ((object,object),), key : object) -> ((object,object),):
    if len(assoc)==0:
        raise KeyError
    else:
        if key==assoc[0][0]:
            return assoc[1:]
        else:
            return (assoc[0],)+del_assoc(assoc[1:],key)



def set_assoc(assoc : ((object,object),), key : object, value: object) -> ((object,object),):
    if len(assoc)==0:
        return assoc+((key,value),)
    if key==assoc[0][0]:
        return ((key,value),)+assoc[1:]
    else:
        return (assoc[0],)+set_assoc(assoc[1:],key,value)



def immutify(a : 'an int, str, list, tuple, set, or dict') -> 'an int, str, tuple, or frozenset':
    if type(a) in [int,str,frozenset]:
        return a
    elif type(a)==set:
        return frozenset(a)
    elif type(a)==list:
        if len(a)==0:
            return ()
        else:
            return immutify((a[0],))+immutify(a[1:])
    elif type(a)==tuple:
        if len(a)==0:
            return ()
        else:
            return (immutify(a[0]),)+immutify(a[1:])
    elif type(a)==dict:
        return immutify([(x,a[x]) for x in sorted(a.keys())])
 
    

def balanced(s : str) -> bool:
    if len(s)==0:
        return True
    elif s[0]==')' or s[-1]=='(':
        return False
    elif s[0]=='(':
        if ')' in s[1:]:
            inde=s.find(')')
            s=s[1:inde]+s[inde+1:]
            return balanced(s)
        else:
            return False
    else:
        return False
            

        
    
def my_str(l : 'int or list of ints with nested lists of ints') -> str:
    checkedlist_set=set()
    def helper(ob):
        if type(ob)==int:
            return ob
        elif type(ob)==list:
            checkedlist_set.add(id(ob))
            li=[]
            for x in ob:
                if type(x)==int:
                    li.append(x)
                elif type(x)==list:
                    if id(x) not in checkedlist_set:
                        checkedlist_set.add(id(x))
                        li.append(helper(x))
                    else:
                        li.append('[...]')
            return li
    li=helper(l)
    re='['+', '.join(str(x) for x in li)+']'
    return re
            

    


if __name__=="__main__":
    
    import predicate,random,driver
    from goody import irange
    x = [1,[2],3]
    x[1] = x
    print(my_str(x))
    '''
    print('Testing odd')
    print(odd(()))
    print(odd((1,)))
    print(odd((1,2)))
    print(odd((1,2,3,4,5,6,7,8,9)))
    print(odd((0,1,2,3,4,5,6,7,8,9)))
    print(odd(('a','b','c','d','e','f','g','h','i')))
    print(odd(('a','b','c','d','e','f','g','h','i','j')))
     
    print('Testing compare')
    print('',      compare('',''),          '')
    print('',      compare('','abc'),       'abc')
    print('abc',   compare('abc',''),       '')
    print('abc',   compare('abc','abc'),    'abc')
    print('bc',    compare('bc','abc'),     'abc')
    print('abc',   compare('abc','bc'),     'bc')
    print('aaaxc', compare('aaaxc','aaabc'), 'aaabc')
    print('aaabc', compare('aaabc','aaaxc'), 'aaaxc')
     
    print('\nTesting get_assoc')
    assoc = ( ('a',1), ('c',3), ('d',4), ('b',2) )
    print(get_assoc(assoc, 'a'))
    print(get_assoc(assoc, 'b'))
    print(get_assoc(assoc, 'c'))
    print(get_assoc(assoc, 'd'))
    try:
        print(get_assoc(assoc, 'x'))
    except KeyError:
        print('Correctly raised exception on bad key')

    print('\nTesting del_assoc')
    assoc = ( ('a',1), ('c',3), ('d',4), ('b',2) )
    assoc = del_assoc(assoc,'b')
    print('assoc now =', assoc)
    try:
        assoc = del_assoc(assoc, 'x')
    except KeyError:
        print('Correctly raised exception on bad key')
    assoc = del_assoc(assoc,'a')
    print('assoc now =', assoc)
    assoc = del_assoc(assoc,'c')
    print('assoc now =', assoc)
    assoc = del_assoc(assoc,'d')
    print('assoc now =', assoc)

    print('\nTesting set_assoc')
    assoc = ()
    assoc = set_assoc(assoc,'b', 2)
    print('assoc now =', assoc)
    assoc = set_assoc(assoc,'a',1)
    print('assoc now =', assoc)
    assoc = set_assoc(assoc,'c',3)
    print('assoc now =', assoc)
    assoc = set_assoc(assoc,'d',4)
    print('assoc now =', assoc)
    assoc = set_assoc(assoc,'b',102)
    print('assoc now =', assoc)
    assoc = set_assoc(assoc,'c',103)
    print('assoc now =', assoc)
    assoc = set_assoc(assoc,'d',104)
    print('assoc now =', assoc)


    print('\nTesting immutify')
    print( immutify(1) )
    print( immutify('a') )
    print (immutify( (1, 2, 3)) )
    print (immutify( frozenset([1, 2, 3])) )
    print( immutify( [1, 2, 3, 4, 5, 6]) )
    print( immutify( [1, 2, [3, [4], 5], 6]) )
    print( immutify( [1, 2, (3, [4], 5), 6]) )
    print( immutify( [{1,2}, {3,frozenset([4,5])}, {6,7}]))
    print( immutify( [{1,2}, {3,frozenset([4,5])}, [{5,6}]]))
    print( immutify( {'b' : [1,2], 'a' : {'ab': {1,2}, 'aa' : (1,2)}}) )
    
    
    print('\nTesting balanced')
    print(balanced( '()' ))
    print(balanced( '()()' ))
    print(balanced( '(()())' ))
    print(balanced( '()(()(()))' ))
    print(balanced( '(()())(()(()))' ))
    print(balanced( '(' ))
    print(balanced( ')' ))
    print(balanced( '()(()(())' ))
   
    print('\nTesting my_str')
    x = [1,[2,3,[4,[[5]],6]]]
    print(str(x), 'should match the result printed below')
    print(my_str(x))
    y = [1,2]
    x = [y,y]
    print(str(x), 'should match the result printed below')
    print(my_str(x))
    x = [1,[2],3]
    x[1] = x
    print(str(x), 'should match the result printed below')
    print(my_str(x))
    x = [1,2,3]
    x[1] = x
    y = [10,11,12]
    x[0] = y
    y[2] = x
    print(str(x), 'should match the result printed below')
    print(my_str(x))
    print(str(y), 'should match the result printed below')
    print(my_str(y))
    print()
    '''
    driver.default_file_name = 'bscq5W22.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
    
