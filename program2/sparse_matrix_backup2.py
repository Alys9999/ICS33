#Submitter: zhaoyal5 (Lu, Zhaoyang)
#Partner:  ryanjp1 (Park, Ryan)
# We certify that we worked cooperatively on this programming
# assignment, according to the rules for pair programming




import prompt

class Sparse_Matrix:

    # I have written str(...) because it is used in the bsc.txt file and
    #   it is a bit subtle to get correct. This function does not depend
    #   on any other method in this class being written correctly, although
    #   it could be simplified by writing self[...] which calls __getitem__.   
    def __str__(self):
        size = str(self.rows)+'x'+str(self.cols)
        width = max(len(str(self.matrix.get((r,c),0))) for c in range(self.cols) for r in range(self.rows))
        return size+':['+('\n'+(2+len(size))*' ').join ('  '.join('{num: >{width}}'.format(num=self.matrix.get((r,c),0),width=width) for c in range(self.cols))\
                                                                                             for r in range(self.rows))+']'
                                                    
                                                    
                                                    
    def __init__(self, rows, cols, *matrix):
        if type(rows) not in [int] or type(cols) not in [int] or rows<=0 or cols<=0:
            raise AssertionError('Sparse_Matrix.__init__: Invalid row or column') 
        for x in [*matrix]:
            if len(x)!= 3 or type(x[0]) not in [int] or type(x[1]) not in [int] or x[0]>=rows or x[1]>=cols or type(x[2]) not in[int,float]:
                raise AssertionError('Sparse_Matrix.__init__: Invalid index') 
        key_list=[(x[0],x[1]) for x in [*matrix]]
        if len(key_list)!=len(set(key_list)):
            raise AssertionError('Sparse_Matrix.__init__: Reported index') 
        self.rows=rows
        self.cols=cols
        self.matrix=dict(((x[0],x[1]),x[2]) for x in [*matrix] if x[2]!=0)
        
    
    def size(self):
        return (self.rows,self.cols)
    
    def __len__(self):
        return self.rows*self.cols
    
    def __bool__(self):
        if len(self.matrix.keys())!=0:
            return True
        else:
            return False
    
    def __repr__(self):
        l1=[str((x[0][0],x[0][1],x[1])) for x in self.matrix.items() if len(self.matrix.items())!=0]
        i=''.join(i+',' for i in l1)
        return 'Sparse_Matrix('+str(self.rows)+','+str(self.cols)+','+i+')'
    def __getitem__(self,two_tup):
        if type(two_tup)!=tuple or self.rows<=two_tup[0] or two_tup[0]<0 or self.cols<=two_tup[1] or two_tup[1]<0 or len(two_tup)!=2 or type(two_tup[0])!=int or type(two_tup[1])!=int:
            raise TypeError('Sparse_Matrix.__getitem__: Not a legal tuple')
        if two_tup in self.matrix.keys():
            return self.matrix[two_tup]
        elif two_tup not in self.matrix.keys():
            return 0
        
    def __setitem__(self,two_tup,v):
        if type(two_tup)!=tuple or self.rows<=two_tup[0] or two_tup[0]<0 or self.cols<=two_tup[1] or two_tup[1]<0 or len(two_tup)!=2 or type(two_tup[0])!=int or type(two_tup[1])!=int:
            raise TypeError('Sparse_Matrix.__setitem__: Not a legal tuple')
        elif type(v) not in [int, float]:
            raise TypeError('Sparse_Matrix.__setitem__: Not a legal tuple')
        else:
            if v==0 and two_tup in self.matrix.keys():
                del self.matrix[two_tup]
            elif v==0 and two_tup not in self.matrix.keys():
                pass
            else:
                self.matrix[two_tup]=v
                
    def __delitem__(self,two_tup):
        '''This question needs to make the value 0 not delete the index itself'''
        if type(two_tup)!=tuple or self.rows<=two_tup[0] or two_tup[0]<0 or self.cols<=two_tup[1] or two_tup[1]<0 or len(two_tup)!=2 or type(two_tup[0])!=int or type(two_tup[1])!=int:
            raise TypeError('Sparse_Matrix.__delitem__: Not legal tuple')
        elif two_tup not in self.matrix.keys():
            return 0
        else:
            del self.matrix[two_tup]
            
    def row(self,r_v):
        if type(r_v) != int or self.rows<=r_v or r_v<0:
            raise AssertionError
        else:
            row_tup=()
            for x in range(self.cols):
                if (r_v,x) in self.matrix.keys():
                    row_tup=row_tup+(self.matrix[(r_v,x)],)
                else:
                    row_tup=row_tup+(0,)
        return row_tup
    
    def col(self,c_v):
        if type(c_v) != int or self.cols<=c_v or c_v<0:
            raise AssertionError
        else:
            col_tup=()
            for x in range(self.rows):
                if (x,c_v) in self.matrix.keys():
                    col_tup=col_tup+(self.matrix[(x,c_v)],)
                else:
                    col_tup=col_tup+(0,)
        return col_tup
    
    def details(self):
        re_tup=()
        for x in range(self.rows):
            re_tup=re_tup+(Sparse_Matrix.row(self, x),)
        return str(self.rows)+'x'+str(self.cols)+' -> '+str(self.matrix)+' -> '+str(re_tup)
            
    def __call__(self,n_row,n_col):
        if type(n_row) not in [int] or type(n_col) not in [int] or n_row<=0 or n_col<=0:
            raise AssertionError('Sparse_Matrix.__call__: Invalid rows or columns')
        else:
            self.rows=n_row
            self.cols=n_col
            self.matrix=dict((x,self.matrix[x]) for x in self.matrix.keys() if x[0]<self.rows and x[1]<self.cols)

    def __iter__(self):
        for x in sorted(self.matrix.items(),key= lambda x:x[1]):
            yield x[0]+(x[1],)

    def __pos__(self):
        return Sparse_Matrix(self.rows,self.cols,*[x[0]+(x[1],) for x in self.matrix.items()])

    def __neg__(self):
        return Sparse_Matrix(self.rows,self.cols,*[(x[0][0],x[0][1],-x[1]) for x in self.matrix.items()])
    def __abs__(self):
        return Sparse_Matrix(self.rows,self.cols,*[(x[0][0],x[0][1],abs(-x[1])) for x in self.matrix.items()])
    def __add__(self,right):
        if type(right) not in  [Sparse_Matrix,int,float]:
            raise TypeError
        elif type(right)==Sparse_Matrix and (Sparse_Matrix.size(self)!=Sparse_Matrix.size(right)):
            raise AssertionError
        elif type(right)==Sparse_Matrix:
            l=list(((x,y,Sparse_Matrix.__getitem__(self, (x,y))+Sparse_Matrix.__getitem__(right, (x,y)))) for y in range(self.cols) for x in range(self.rows) if Sparse_Matrix.__getitem__(self, (x,y))+Sparse_Matrix.__getitem__(right, (x,y))!=0)
            return Sparse_Matrix(self.rows,self.cols,*l)
        elif type(right) in [int,float]:
            l=list((x,y,Sparse_Matrix.__getitem__(self, (x,y))+right)for y in range(self.cols) for x in range(self.rows) if Sparse_Matrix.__getitem__(self, (x,y))+right != 0)
            return Sparse_Matrix(self.rows,self.cols,*l)
    def __radd__(self,left):
        if type(left) not in  [Sparse_Matrix,int,float]:
            raise TypeError
        elif type(left)==Sparse_Matrix and (Sparse_Matrix.size(self)!=Sparse_Matrix.size(left)):
            raise AssertionError
        elif type(left)==Sparse_Matrix:
            l=list(((x,y,Sparse_Matrix.__getitem__(self, (x,y))+Sparse_Matrix.__getitem__(left, (x,y)))) for y in range(self.cols) for x in range(self.rows) if Sparse_Matrix.__getitem__(self, (x,y))+Sparse_Matrix.__getitem__(left, (x,y))!=0)
            return Sparse_Matrix(self.rows,self.cols,*l)
        elif type(left) in [int,float]:
            l=list((x,y,Sparse_Matrix.__getitem__(self, (x,y))+left)for y in range(self.cols) for x in range(self.rows) if Sparse_Matrix.__getitem__(self, (x,y))+left != 0)
            return Sparse_Matrix(self.rows,self.cols,*l)

    def __sub__(self,right):
        return Sparse_Matrix.__add__(self, -right)

    def __rsub__(self,left):
        return Sparse_Matrix.__radd__(-self,left)

  
    def __mul__(self,right):
        if type(right) not in  [Sparse_Matrix,int,float]:
            raise TypeError
        if type(right)==Sparse_Matrix and self.cols!=right.rows:
            raise AssertionError
        elif type(right)==Sparse_Matrix:
            matrix1 = []
            matrix2= []
            new_Values = []
            newMatrix = []
            for row in range(self.rows):
                matrix1.append(self.row(row))
            for row in range(right.rows):
                matrix2.append(right.row(row))   
            for row in matrix1:
                for col in zip(*matrix2):
                    new_Values.append(sum(item1*item2 for item1, item2 in zip(row, col))) 
            y = 0
            for row in range(self.rows):
                for col in range(right.cols):
                    newMatrix.append((row, col, new_Values[y]))
                    y+= 1
            return Sparse_Matrix(self.rows,right.cols, *newMatrix)
        
        elif type(right)==int:
            newMatrix = []
            new_Values = []
            for row in range(self.rows):
                for value in self.row(row):
                    new_Values.append(value*right)
            y = 0
            for row in range(self.rows):
                for col in range(self.cols):
                    newMatrix.append((row, col, new_Values[y]))
                    y+= 1
            return Sparse_Matrix(self.rows, self.cols, *newMatrix)
        
        elif type(right)==float:
            newMatrix = []
            new_Values = []
            for row in range(self.rows):
                for value in self.row(row):
                    new_Values.append(value*right)
            y = 0
            for row in range(self.rows):
                for col in range(self.cols):
                    newMatrix.append((row, col, new_Values[y]))
                    y+= 1
            return Sparse_Matrix(self.rows, self.cols, *newMatrix)
    
    def __rmul__(self, left):
        if type(left)==int:
            newMatrix = []
            new_Values = []
            for row in range(self.rows):
                for value in self.row(row):
                    new_Values.append(value*left)
            y = 0
            for row in range(self.rows):
                for col in range(self.cols):
                    newMatrix.append((row, col, new_Values[y]))
                    y+= 1
            return Sparse_Matrix(self.rows, self.cols, *newMatrix)
        
        elif type(left)==float:
            newMatrix = []
            new_Values = []
            for row in range(self.rows):
                for value in self.row(row):
                    new_Values.append(value*left)
            y = 0
            for row in range(self.rows):
                for col in range(self.cols):
                    newMatrix.append((row, col, new_Values[y]))
                    y+= 1
            return Sparse_Matrix(self.rows, self.cols, *newMatrix)
        
        else:
            raise TypeError('Sparse_Matrix.__rmult__: Not a valid object for multiplication')

    def __pow__(self, right):
        if type(right) not in [int]:
            raise TypeError
        elif self.rows!=self.cols or right<1:
            raise AssertionError
        else:
            result_self=self
            for x in range(1,right):
                result_self=Sparse_Matrix.__mul__(result_self, self)
        return result_self

    def __eq__(self,right):
        if type(right) in [Sparse_Matrix] and self.rows==right.rows and self.cols==right.cols and self.matrix==right.matrix:
            return True
        elif type(right) in [int, float]:
            if right==0 and self.matrix=={}:
                return True
            elif right!=0 and (self.rows*self.cols)==len(self.matrix):
                re_b=True
                for x in self.matrix.values():
                    if x!=right:
                        re_b==False
                return re_b
            else:
                return False
        else:
            return False

    def __ne__(self,right):
        if type(right) in [Sparse_Matrix] and self.rows==right.rows and self.cols==right.cols and self.matrix==right.matrix:
            return False
        elif type(right) in [int, float]:
            if right==0 and self.matrix=={}:
                return False
            elif right!=0 and (self.rows*self.cols)==len(self.matrix):
                re_b=False
                for x in self.matrix.values():
                    if x!=right:
                        re_b==True
                return re_b
            else:
                return True
        else:
            return True
        


if __name__ == '__main__':
    
    #Simple tests before running driver
    #Put your own test code here to test Sparse_Matrix before doing the bsc tests
    #Debugging problems with these tests is simpler

    print('Printing')
    m = Sparse_Matrix(3,3, (0,0,0),(0,1,2),(0,2,3),(1,0,4),(1,1,5),(1,2,6),(2,0,7),(2,1,8),(2,2,0))

    '''
    print(m)
    print(repr(m))
    print(m.details())
  
    print('\nlen and size')
    print(len(m), m.size(),)
    
    print('\ngetitem and setitem')
    print(m[1,1])
    m[1,1] = 0
    m[0,1] = 2
    print(m.details())

    print('\niterator')
    for r,c,v in m:
        print((r,c),v)
    
    print('\nm, m+m, m+1, m==m, m==1')
    print(m)
    print(m+m)
    print(m+1)
    print(m==m)
    print(m==1)
    print()
    '''
    import driver
    driver.default_file_name = 'bscp22W22.txt'
#     driver.default_show_exception = prompt.for_bool('Show exceptions when testing',True)
#     driver.default_show_exception_message = prompt.for_bool('Show exception messages when testing',True)
#     driver.default_show_traceback = prompt.for_bool('Show traceback when testing',True)
    driver.driver()
