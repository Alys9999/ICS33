import re, traceback, keyword

def pnamedtuple(type_name, field_names, mutable = False,  defaults =  {}):
    def show_listing(s):
        for line_number, text_of_line in enumerate(s.split('\n'),1):         
            print(f' {line_number: >3} {text_of_line.rstrip()}')

    # put your code here
    # bind class_definition (used below) to the string constructed for the class
    if type(field_names)==str:
        fn_list=field_names.replace(',',' ').split()
    elif type(field_names)==list:
        fn_list=field_names
    else:
        raise SyntaxError
    fn_str=','.join(fn_list)
    if not re.match('^[a-zA-Z][\w_]*$', str(type_name)) or type_name in keyword.kwlist:
        raise SyntaxError
    for fn in fn_list:
        if not re.match('^[a-zA-Z][\w_]*$', str(fn)) or fn in keyword.kwlist:
            raise SyntaxError
    set_attr='\n        '.join(['self.'+x+'='+x for x in fn_list])
    gets=''.join(['def get_'+str(x)+'(self):\n'+'        return self.'+str(x)+'\n    ' for x in fn_list])
    
    def iter_to_str(iterale):
        return ','.join(iterable)
    
    
    
    class_definition=f"""\
class {type_name}:

    _fields={fn_list}
    _mutable={mutable}
    
    def __init__(self,{fn_str}):
        {set_attr}
    
    def __repr__(self):
        t=tuple(self.__dict__.items())
        l=()
        for x in t:
            l=l+((x[0]+'='+str(x[1])),)
        
        return f'{type_name}' +'('+','.join(l)+')'
    
    def __call__(self,*vs):
        for x in range(len(fn_list)):
            self.__dict__[fn_list[x]]=vs[x]          
        return self
        
    {gets}
    
    def __getitem__(self, index):
        if type(index)==int:
            return self.__dict__[{type_name}._fields[index]]
        elif type(index)==str:
            try:
                return self.__dict__[index]
            except KeyError:
                raise IndexError
        else:
            raise IndexError
    
    def __eq__(self,right):
        return type(self)==type(right) and self.__dict__.items()==right.__dict__.items()
        
    def _asdict(self):
        return self.__dict__
        
    def _make(iterable):
        t1={type_name}(*iterable)
        
        return t1

    def _replace(self, **kargs):
        if self._mutable:
            for x in self._fields:
                y = self.__getitem__(x)
                for key, val in kargs.items():
                    if key not in self._fields:
                        raise TypeError
                    elif x==key:
                        self.__dict__[x] = val
            return None
        else:
            newParams = []
            trackkeys = []
            checkError = []
            for x in self._fields:
                y = self.__getitem__(x)
                checkError.append(y)
                for key, val in kargs.items():
                    if key not in self._fields:
                        raise TypeError
                    elif x==key and x not in trackkeys:
                        newParams.append((val))
                        trackkeys.append(x)
                    elif x!= key and x not in kargs.keys() and x not in trackkeys:
                        newParams.append((y))
                        trackkeys.append(x)
            if checkError == newParams:
                raise TypeError
            return {type_name}(*newParams)
            
    def __setattr__(self,k,v):
        if {type_name}._mutable == False:
            if k in self.__dict__.keys():
                raise AttributeError
            else:
                self.__dict__[k]=v
        else:
            self.__dict__[k]=v
    
"""
    
    # Debugging aid: uncomment next call to show_listing to display source code
    #show_listing(class_definition)
    
    # Execute str in class_definition in name_space; then bind the attribute
    #   source_code to the class_definition str; finally, return the class
    #   object created; any syntax errors will print a listing of the
    #   of class_definition and trace the error (see the except clause).
    
    name_space = dict( __name__ = f'pnamedtuple_{type_name}' )                  
    try:
        exec(class_definition,name_space)
        name_space[type_name].source_code = class_definition
    except (TypeError,SyntaxError):                      
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]
    

    
if __name__ == '__main__':
    # Test simple pnamedtuple below in script: Point=pnamedtuple('Point','x,y')


    
    #driver tests
    import driver  
    driver.default_file_name = 'bscp3W22.txt'
#     driver.default_show_exception_message = True
#     driver.default_show_traceback = True
    driver.driver()
