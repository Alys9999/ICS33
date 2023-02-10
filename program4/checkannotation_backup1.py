from goody import type_as_str
import inspect

class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (by raising AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check,param,value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (by raising AssertionError) this classes raises AssertionError and prints
      its failure, along with a list of all annotations tried followed by the
      check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check,param,value,check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 



class Check_Annotation:
    # Initially bind the class attribute to True allowing checking to occur (but
    #   only if the object's self._checking_on attribute is also bound to True)
    checking_on  = True
  
    # Initially bind self._checking_on = True, to check the decorated function f
    def __init__(self, f):
        self._f = f
        self._checking_on = True

    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)

        # Initially compare check's function annotation with its arguments
        def is_list(value, annot):
            if type(value)==type(annot):
                if len(annot)==1:
                    for x in value:
                        is_list(x,annot[0])
                else:
                    is_list(value[0],annot[0])
                    is_list(value[1:],annot[1:])
            elif type(value)==annot:
                return True
            else:
                raise AssertionError

        if annot==None:
            pass
        elif type(annot)==type:

            if inspect.signature(self._f).return_annotation != type(self._f(value)) and inspect.signature(self._f).return_annotation!=inspect._empty:
                raise AssertionError
            if not isinstance(value, annot):
                tv=str(type(value))
                ans=str(annot)
                raise AssertionError(f"{param} failed the annotaion check(wrong type): value = {value}\n  was type {tv} ...should be type {ans}")  
        elif type(annot)==list:
            if isinstance(value,type(annot)):
                if len(value)<len(annot):
                    raise AssertionError
                is_list(value,annot)
            else:
                raise AssertionError
        elif type(annot)==tuple:
            if isinstance(value,type(annot)):
                if len(value)<len(annot):
                    raise AssertionError
                is_list(value,annot)
            else:
                raise AssertionError
            
        elif type(annot)==dict:
            if isinstance(value,type(annot)) and len(annot)==1:
                for x in list(value.keys()):
                    if type(x)!=list(annot.keys())[0]:
                        raise AssertionError
                for y in list(value.values()):
                    if type(y)!=list(annot.values())[0]:
                        raise AssertionError
            else:
                raise AssertionError
        
        elif type(annot)==set:
            if isinstance(value,type(annot)) and len(annot)==1:
                for x in value:
                    if type(x) not in annot:
                        raise AssertionError
            else:
                raise AssertionError
            
        elif type(annot)==frozenset:
            if isinstance(value,type(annot)) and len(annot)==1:
                for x in value:
                    if type(x) not in annot:
                        raise AssertionError
            else:
                raise AssertionError
        elif inspect.isfunction(annot):
            if len(inspect.signature(annot).parameters)!=1:
                raise AssertionError
            if hasattr(value, '__iter__'):
                for x in value:
                    if annot(x)==False:
                        raise AssertionError
            elif annot(value)==False:
                raise AssertionError

        else:
            raise AssertionError
            
            
                
            
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):
        
        # Return argument/parameter bindings in an OrderedDict (derived from a
        #   regular dict): bind the function header's parameters with that order
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if not (param.name in bound_f_signature.arguments):
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments

        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        if Check_Annotation.checking_on== False or self._checking_on == False:
            return self._f()
        
        try:
            # For each detected annotation, check it using its argument's value

            # Compute/remember the value of the decorated function
            
            # If 'return' is in the annotation, check it
            
            # Return the decorated answer
            p=param_arg_bindings()
            fa=self._f.__annotations__
            
            for x in range(len(list(p.keys()))):
                Check_Annotation.check(self,list(p.keys())[x],list(fa.values())[x],list(p.values())[x])
            
            
        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError:
            #print(80*'-')
            #for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
                #print(l.rstrip())
            #print(80*'-')
            raise




  
if __name__ == '__main__':     
    # an example of testing a simple annotation  
    
    def f(x : list): pass    
    f = Check_Annotation(f)
    f([1,2])
    #f('abc')
    '''
    def f(x : [int,str]): pass
    f = Check_Annotation(f)    
    f([1,'b'])
    
    def f(x : {str : int}): pass
    f = Check_Annotation(f)
    f({'a':1,'b':2})
    
    def f(x : {str}): pass
    f = Check_Annotation(f)
    f({'a','b'})
    
    def f(x : lambda x : x >= 0): pass
    f = Check_Annotation(f)
    f(3)
    f([0,1,0])
    '''

    #driver tests
    import driver
    driver.default_file_name = 'bscp4W22.txt'
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
