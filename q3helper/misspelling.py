from distance_helper import min_dist
import prompt


class Misspelling:
    # __init__ must call this method so I can test Misspelling more easily.
    # This method should consist of only new bindings to attribute names.
    # It should (and will when I grade it) always have a list binding
    #   self.last = some value
    # You may put your own bindings here using any names to test your code;
    #   when I grade your work, I will replace the contents of this method
    #   but the last binding will always be to the attribute last
    def initialize_attributes(self):
        self.amoral = 1
        self.more   = 2
        self.babel  = 3
        self.last   = 4
        
        
    def __init__(self, fix_when_setting=False):
        self.fix_when_setting = fix_when_setting
        self.initialize_attributes()     
     
     
    def closest_matches(self,name):
        possible_list=[x for x in self.__dict__.keys() if min_dist(x,name)<=(len(name)/2)]
        for x in possible_list:
            for y in possible_list:
                if min_dist(x,name)<min_dist(y,name):
                    possible_list.remove(y)
        return possible_list
     
    def __getattr__(self,name):
        re_list=[self.__dict__[x] for x in Misspelling.closest_matches(self, name)]
        if len(re_list)!=1:
            raise NameError
        return re_list[0]



# Uncomment when ready to solve this part; otherwise o.a = v does nothing
    
    def __setattr__(self,name,value):
        if 'last' not in self.__dict__.keys():
            self.__dict__[name]=value
        elif name in self.__dict__.keys():
            self.__dict__[name]=value
        elif 'name' not in self.__dict__.keys() and self.fix_when_setting==True:
            n=Misspelling.closest_matches(self, name)
            if len(n)==1:
                self.__dict__[n[0]]=value
            else:
                raise NameError('there is none or more than one matched attribute')
        elif self.fix_when_setting==False:
            raise NameError ('fix_when_setting is False')

            

    

# You should try to understand the specifications and test your code
#   to ensure it works correctly, according to the specification.
# You are all allowed to ask "what should my code do..." questions online
#   both before and after I post my batch self_check file.
# The driver below will allow you to easily test your code.

if __name__ == '__main__':
    #o = Misspelling(prompt.for_bool("Allow fixing mispelling in __setattr__",True)) 
    # Put code here to test object o the same way each time the code is run

# how is the test used?
    
    '''
    # Use the while loop below to type in code one on-the-fly when prompted
    while True:
        try:
            print("\n" + str(o.__dict__))   
            test = prompt.for_string("Enter test")
            if test == "quit":
                break;
            if '=' not in test:
                print(eval(test))
            else:
                exec(test)
        except Exception as exc:
            print(exc)
    '''

    
    print()
    import driver
    
    driver.default_file_name = 'bscq32W22.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
