class DictList:
    def __init__(self,*d):
        self.dl=[]
        if len(d)==0:
            raise AssertionError(f'DictList.__init__: expect at least one argument, 0 was sent in')
        for x in d:
            if type(x) == dict:
                self.dl.append(x)
            else:
                raise AssertionError(f'DictList.__init__: \'{x}\' is not a dictionary')
    
    def __len__(self):
        k_set=set()
        for x in self.dl:
            for y in x.keys():
                k_set.add(y)
        return len(k_set)
    
    def __repr__(self):
        s='DictList('
        for x in self.dl:
            if x==self.dl[-1]:
                s=s+str(x)
            else:
                s=s+str(x)+','
        return s +')'
    
    def __contains__(self,k):
        for x in self:
            for y in x.keys():
                if y==k:
                    return True
        return False
    
    def __getitem__(self):
    
    
    
    
            
if __name__=='__main__':
    dic1={'a':1,'b':2}
    dic2={'a':3,"d":4}
    d1=DictList(dic1,dic2)
    print(d1.__len__())
    print(d1.dl)
    print(d1.__repr__())