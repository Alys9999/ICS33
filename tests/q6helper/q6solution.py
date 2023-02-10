import prompt
from goody import irange
from collections import defaultdict


# List Node class and helper functions (to set up problem)

class LN:
    created = 0
    def __init__(self,value,next=None):
        self.value = value
        self.next  = next
        LN.created  += 1

def list_to_ll(l):
    if l == []:
        return None
    front = rear = LN(l[0])
    for v in l[1:]:
        rear.next = LN(v)
        rear = rear.next
    return front

def str_ll(ll):
    answer = ''
    while ll != None:
        answer += str(ll.value)+'->'
        ll = ll.next
    return answer + 'None'



# Tree Node class and helper functions (to set up problem)

class TN:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left  = left
        self.right = right

def list_to_tree(alist):
    if alist == None:
        return None
    else:
        return TN(alist[0],list_to_tree(alist[1]),list_to_tree(alist[2])) 
    
def str_tree(atree,indent_char ='.',indent_delta=2):
    def str_tree_1(indent,atree):
        if atree == None:
            return ''
        else:
            answer = ''
            answer += str_tree_1(indent+indent_delta,atree.right)
            answer += indent*indent_char+str(atree.value)+'\n'
            answer += str_tree_1(indent+indent_delta,atree.left)
            return answer
    return str_tree_1(0,atree) 


# Define alternate ITERATIVELY

def alternate_i(ll1 : LN, ll2 : LN) -> LN:
    # Handle the case of ll1 or ll2 being empty
    if ll1==None and ll2==None:
        return None
    elif ll1==None:
        return ll2
    elif ll2==None:
        return ll1
    # Set up for iteration (keep track of front and rear of linked list to return)
    # while True: with both l1 and l2 not empty and ll1 is in the linked list to return
    ll=ll1
    while ll1!=None and ll2!=None:
        l1_sec=ll1.next
        l2_sec=ll2.next
        ll1.next=ll2
        if l1_sec== None:
            ll2=l2_sec
        else:
            ll2.next=l1_sec
        ll1=l1_sec
        ll2=l2_sec
    return ll
        # return correct result if ll1 or ll2 is empty (after advancing ll1 and ll2)
        # continue looping if both ll1/ll2 are not empty, with ll1 in the linked list to return        


# Define alternate RECURSIVELY

def alternate_r(ll1 : LN, ll2 : LN) -> LN:
    if ll1==None and ll2==None:
        return None
    elif ll1==None:
        return ll2
    elif ll2==None:
        return ll1
    else:
        l1_sec=ll1.next
        l2_sec=ll2.next
        ll1.next=ll2
        if l1_sec== None:
            ll2=l2_sec
        else:
            ll2.next=l1_sec
        alternate_r(l1_sec,l2_sec)
        return ll1



# Define count RECURSIVELY

def count(t,value):
    c=0
    if t==None:
        return 0
    elif t.value==value:
        c+=1
        return c+count(t.left,value)+count(t.right,value)
    else:
        return c+count(t.left,value)+count(t.right,value)




class bidict(dict):
    created=[]
    def __init__(self, **kargs):
        
        def _is_hashable(item):
            if type(item)!=str:
                if hasattr(item,'__hash__')==False or item.__hash__ == None:
                    raise ValueError
                else:
                    if type(item)==int:
                        return True
                    elif len(item)==0:
                        return True
                    _is_hashable(item[0])
                    _is_hashable(item[1:])
                    
        for x in kargs.keys():
            _is_hashable(x)
        for y in kargs.values():
            _is_hashable(y)
        dict.__init__(self,kargs)
        self.created.append(self)

        
        self._rdict={}
        for x in self.items():
            if x[1] not in self._rdict.keys():
                s=set(x[0])
                self._rdict[x[1]]=s
            elif x[1] in self._rdict.keys():
                self._rdict[x[1]].add(x[0])
        
    def __setitem__ (self,key,value):
        super().__setitem__(key,value)
        if value not in self._rdict.keys():
            s=set(key)
            self._rdict[value]=s
        elif value in self._rdict.keys():
            self._rdict[value].add(key)
        l=list(self._rdict.keys())
        l.remove(value)
        for x in l:
            if key in self._rdict[x]:
                self._rdict[x].remove(key)
            if len(self._rdict[x])==0:
                del self._rdict[x]
    
    def __delitem__ (self,key):
        super().__delitem__(key)
        l=list(self._rdict.keys())
        for x in l:
            if key in self._rdict[x]:
                self._rdict[x].remove(key)
            if len(self._rdict[x])==0:
                del self._rdict[x]
                
    def __call__ (self,value):
        return self._rdict[value]
    
    def clear (self):
        super().clear()
        self._rdict={}
        
    @staticmethod    
    def all_objects():
        return bidict.created
    
    @staticmethod
    def forget(object):
        i=bidict.created.index(object)
        del bidict.created[i]
        






    
# Testing Script

if __name__ == '__main__':
    print('\n\nTesting bidict')
    b1 = bidict(a=1,b=2,c=1)
    b2= bidict(a=1,b=2,c=1)
    print(b1, b1._rdict)
    b1['a']= 2
    print(b1, b1._rdict)
    b1['d']= 2
    print(b1, b1._rdict)
    b1['c']= 2
    print(b1, b1._rdict)
    b1.__delitem__('a')
    print(b1, b1._rdict)
    b1.clear()
    print(b1, b1._rdict)
    print(bidict.all_objects())
    
    '''
    print('Testing alternate_i')
    ll1 = list_to_ll([])
    ll2 = list_to_ll([])
    print('\n  ll1= ',str_ll(ll1))
    print(  '  ll2= ',str_ll(ll2))
    ll = alternate_i(ll1,ll2)
    print('  alternate  = ',str_ll(ll))
    print('  ll1= ',str_ll(ll1))
    print('  ll2= ',str_ll(ll2))
    
    ll1 = list_to_ll([1])
    ll2 = list_to_ll([])
    print('\n  ll1= ',str_ll(ll1))
    print('  ll2= ',str_ll(ll2))
    ll = alternate_i(ll1,ll2)
    print('  alternate  = ',str_ll(ll))
    print('  ll1= ',str_ll(ll1))
    print('  ll2= ',str_ll(ll2))
    
    ll1 = list_to_ll([])
    ll2 = list_to_ll([1])
    print('\n  ll1= ',str_ll(ll1))
    print(  '  ll2= ',str_ll(ll2))
    ll = alternate_i(ll1,ll2)
    print('  alternate  = ',str_ll(ll))
    print('  ll1= ',str_ll(ll1))
    print('  ll2= ',str_ll(ll2))
    
    ll1 = list_to_ll([1])
    ll2 = list_to_ll([2])
    print('\n  ll1= ',str_ll(ll1))
    print(  '  ll2= ',str_ll(ll2))
    ll = alternate_i(ll1,ll2)
    print('  alternate  = ',str_ll(ll))
    print('  ll1= ',str_ll(ll1))
    print('  ll2= ',str_ll(ll2))
    
    ll1 = list_to_ll(['a','b','c','d'])
    ll2 = list_to_ll(['w','x','y','z'])
    print('\n  ll1= ',str_ll(ll1))
    print(  '  ll2= ',str_ll(ll2))
    ll = alternate_i(ll1,ll2)
    print('  alternate  = ',str_ll(ll))
    print('  ll1= ',str_ll(ll1))
    print('  ll2= ',str_ll(ll2))
    
    ll1 = list_to_ll(['a','b','c','d','e','f','g'])
    ll2 = list_to_ll(['w','x','y','z'])
    print('\n  ll1= ',str_ll(ll1))
    print(  '  ll2= ',str_ll(ll2))
    ll = alternate_i(ll1,ll2)
    print('  alternate  = ',str_ll(ll))
    print('  ll1= ',str_ll(ll1))
    print('  ll2= ',str_ll(ll2))
    
    ll1 = list_to_ll(['a','b','c','d'])
    ll2 = list_to_ll(['w','x','y','z',1,2,3,4])
    print('\n  ll1= ',str_ll(ll1))
    print(  '  ll2= ',str_ll(ll2))
    ll = alternate_i(ll1,ll2)
    print('  alternate  = ',str_ll(ll))
    print('  ll1= ',str_ll(ll1))
    print('  ll2= ',str_ll(ll2))
    
    # Put in your own tests here

    
    print('\n\nTesting alternate_r')
    ll1 = list_to_ll([])
    ll2 = list_to_ll([])
    print('\n  ll1= ',str_ll(ll1))
    print(  '  ll2= ',str_ll(ll2))
    ll = alternate_r(ll1,ll2)
    print('  alternate  = ',str_ll(ll))
    print('  ll1= ',str_ll(ll1))
    print('  ll2= ',str_ll(ll2))

    ll1 = list_to_ll([1])
    ll2 = list_to_ll([])
    print('\n  ll1= ',str_ll(ll1))
    print(  '  ll2= ',str_ll(ll2))
    ll = alternate_r(ll1,ll2)
    print('  alternate  = ',str_ll(ll))
    print('  ll1= ',str_ll(ll1))
    print('  ll2= ',str_ll(ll2))
    
    ll1 = list_to_ll([])
    ll2 = list_to_ll([1])
    print('\n  ll1= ',str_ll(ll1))
    print(  '  ll2= ',str_ll(ll2))
    ll = alternate_r(ll1,ll2)
    print('  alternate  = ',str_ll(ll))
    print('  ll1= ',str_ll(ll1))
    print('  ll2= ',str_ll(ll2))
    
    ll1 = list_to_ll([1])
    ll2 = list_to_ll([2])
    print('\n  ll1= ',str_ll(ll1))
    print(  '  ll2= ',str_ll(ll2))
    ll = alternate_r(ll1,ll2)
    print('  alternate  = ',str_ll(ll))
    print('  ll1= ',str_ll(ll1))
    print('  ll2= ',str_ll(ll2))
    
    ll1 = list_to_ll(['a','b','c','d'])
    ll2 = list_to_ll(['w','x','y','z'])
    print('\n  ll1= ',str_ll(ll1))
    print(  '  ll2= ',str_ll(ll2))
    ll = alternate_r(ll1,ll2)
    print('  alternate  = ',str_ll(ll))
    print('  ll1= ',str_ll(ll1))
    print('  ll2= ',str_ll(ll2))
    
    ll1 = list_to_ll(['a','b','c','d','e','f','g'])
    ll2 = list_to_ll(['w','x','y','z'])
    print('\n  ll1= ',str_ll(ll1))
    print(  '  ll2= ',str_ll(ll2))
    ll = alternate_r(ll1,ll2)
    print('  alternate  = ',str_ll(ll))
    print('  ll1= ',str_ll(ll1))
    print('  ll2= ',str_ll(ll2))

    ll1 = list_to_ll(['a','b','c','d'])
    ll2 = list_to_ll(['w','x','y','z',1,2,3,4])
    print('\n  ll1= ',str_ll(ll1))
    print(  '  ll2= ',str_ll(ll2))
    ll = alternate_r(ll1,ll2)
    print('  alternate  = ',str_ll(ll))
    print('  ll1= ',str_ll(ll1))
    print('  ll2= ',str_ll(ll2))
    
    # Put in your own tests here

    
    print('\n\nTesting count')
    tree = list_to_tree(None)
    print('\nfor tree = \n',str_tree(tree))
    for i in [1]:
        print('count(tree,'+str(i)+') = ', count(tree,i))
          
    tree = list_to_tree([1, [2, None, None], [3, None, None]])
    print('\nfor tree = \n',str_tree(tree))
    for i in irange(1,3):
        print('count(tree,'+str(i)+') = ', count(tree,i))
          
    tree = list_to_tree([3, [2, None, [3, None, None]], [1, [3, None, None], None]])
    print('\nfor tree = \n',str_tree(tree))
    for i in irange(1,3):
        print('count(tree,'+str(i)+') = ', count(tree,i))
          
    tree = list_to_tree([3, [2, [3, None, [2, None, None]], [3, None, None]], [1, [3, None, None], None]])
    print('\nfor tree = \n',str_tree(tree))
    for i in irange(1,3):
        print('count(tree,'+str(i)+') = ', count(tree,i))
          
         
    # Put in your own tests here

    
    print('\n\nTesting bidict')
    b1 = bidict(a=1,b=2,c=1)
    print(b1, b1._rdict)
    b1['a']= 2
    print(b1, b1._rdict)
    b1['d']= 2
    print(b1, b1._rdict)
    b1['c']= 2
    print(b1, b1._rdict)
    
    b1.clear()
    print(b1, b1._rdict)
    
    b2 = bidict(a=1,b=2,c=1,d=2)
    del b2['a']
    print(b2, b2._rdict)
    del b2['b']
    print(b2, b2._rdict)
    del b2['c']
    print(b2, b2._rdict)
    del b2['d']
    print(b2, b2._rdict)
    print(b2._rdict)
    
    b3 = bidict(a=1,b=2,c=1,d=2)
    print(b3(1))
    print(b3(2))
    
    print(bidict.all_objects())
    bidict.forget(b2)
    print(bidict.all_objects())
    bidict.forget(b3)
    print(bidict.all_objects())
    bidict.forget(b1)
    print(bidict.all_objects())

    # Put in your own tests here

   

    '''
    import driver
    driver.default_file_name = 'bscq6W22.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    print('\n\n')
    driver.driver()
    
