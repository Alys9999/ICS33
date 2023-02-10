from goody import irange, type_as_str
import math

class Date:
    month_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    @staticmethod
    def is_leap_year(year):
        return (year%4 == 0 and year%100 != 0) or year%400 == 0
    
    @staticmethod
    def days_in(year,month):
        return Date.month_dict[month] + (1 if month == 2 and Date.is_leap_year(year) else 0)

    def __init__(self, year, month, day):
        if type(year)!=int or type(month)!=int or type(day)!=int:
            raise AssertionError('one of the date input is not an int')
        if year<0 or month>12 or month<=0:
            raise AssertionError('year or month value invalid')
        if Date.is_leap_year(year):
            local_month_dict=Date.month_dict.copy()
            local_month_dict[2]=29
        if day not in range(1,Date.days_in(year,month)+1):
            raise AssertionError ('invalid day value')
        self.year=year
        self.month=month
        self.day=day
        
    def __getitem__(self,*i):
        re_tu=()
        if type(i[0])!=tuple:
            i_list=[i[0]]
        else:
            i_list=list(x for x in i[0])
        for x in i_list:
            if x not in ['y','m','d']:
                raise IndexError('invalid index')
            if x=='y':
                re_tu=re_tu+(self.year,)
            elif x=='m':
                re_tu=re_tu+(self.month,)
            elif x=='d':
                re_tu=re_tu+(self.day,)
        if len(re_tu)>1:
            return re_tu
        elif len(re_tu)==1:
            return re_tu[0]

    def __repr__(self):
        return 'Date('+str(self.year)+','+str(self.month)+','+str(self.day)+')'
    
    def __str__(self):
        return str(self.month)+'/'+str(self.day)+'/'+str(self.year)
    
    def __len__(self):
        y_days=math.floor(self.year/4)+self.year*365-math.floor(self.year/100)+math.ceil(self.year/400)
        local_month_dict=Date.month_dict.copy()
        if Date.is_leap_year(self.year):
            local_month_dict[2]=29
            if self.year!=0:
                #print(self.month)
                y_days-=1
            if self.year/1000>=1 and self.year%1000==0:
                y_days+=1
        m_days=sum(list(local_month_dict[x] for x in range(1,self.month)))
        #print(m_days)
        re_days=y_days+m_days+self.day-1
        return re_days
    
    def __eq__(self,right):
        if type(right)!=Date:
            return False
        if self.year==right.year and self.month==right.month and self.day==right.day:
            return True
        else:
            return False
        
    def __lt__(self,right):           
        if type(right)==int:
            return len(self)<right
        elif type(right)==Date:
            return len(self)<len(right)
        else:
            raise NotImplemented
    
    def __add__(self,right):
        if type(right) not in [int]:
            raise NotImplemented
        d_list=[self.year,self.month,self.day]
        abs_r=abs(right)
        local_month_dict=Date.month_dict.copy()
        if right>0:
            for x in range(abs_r):
                if Date.is_leap_year(d_list[0]):
                    local_month_dict[2]=29
                elif Date.is_leap_year(d_list[0])==False:
                    local_month_dict[2]=28
                d_list[2]+=1
                if 1>d_list[2] or d_list[2]>(local_month_dict[d_list[1]]):
                    d_list[2]=1
                    d_list[1]+=1
                    if 1>d_list[1] or d_list[1]>12:
                        d_list[1]=1
                        d_list[0]+=1
        elif right<0:
            for x in range(abs_r):
                if Date.is_leap_year(d_list[0]):
                    local_month_dict[2]=29
                elif Date.is_leap_year(d_list[0])==False:
                    local_month_dict[2]=28
                d_list[2]-=1
                if 1>d_list[2] or d_list[2]>(local_month_dict[d_list[1]]):
                    if d_list[1]>1:
                        m_num=local_month_dict[d_list[1]-1]
                    else: m_num=31
                    d_list[2]=m_num
                    d_list[1]-=1
                    if 1>d_list[1] or d_list[1]>12:
                        d_list[1]=12
                        d_list[0]-=1
        return Date(d_list[0],d_list[1],d_list[2])

    def __radd__(self,left):
        if type(left) not in [int]:
            raise NotImplemented
        d_list=[self.year,self.month,self.day]
        abs_r=abs(left)
        local_month_dict=Date.month_dict.copy()
        if left>0:
            for x in range(abs_r):
                if Date.is_leap_year(d_list[0]):
                    local_month_dict[2]=29
                elif Date.is_leap_year(d_list[0])==False:
                    local_month_dict[2]=28
                d_list[2]+=1
                if 1>d_list[2] or d_list[2]>(local_month_dict[d_list[1]]):
                    d_list[2]=1
                    d_list[1]+=1
                    if 1>d_list[1] or d_list[1]>12:
                        d_list[1]=1
                        d_list[0]+=1
        elif left<0:
            for x in range(abs_r):
                if Date.is_leap_year(d_list[0]):
                    local_month_dict[2]=29
                elif Date.is_leap_year(d_list[0])==False:
                    local_month_dict[2]=28
                d_list[2]-=1
                if 1>d_list[2] or d_list[2]>(local_month_dict[d_list[1]]):
                    if d_list[1]>1:
                        m_num=local_month_dict[d_list[1]-1]
                    else: m_num=31
                    d_list[2]=m_num
                    d_list[1]-=1
                    if 1>d_list[1] or d_list[1]>12:
                        d_list[1]=12
                        d_list[0]-=1
        return Date(d_list[0],d_list[1],d_list[2])
    
    def __sub__(self,right):
        if type(right)==int:
            return Date.__add__(self,-right)
        elif type(right)==Date:
            return len(self)-len(right)
        else:
            raise TypeError

    
    def __call__(self,year,month,day):
        if type(year)!=int or type(month)!=int or type(day)!=int:
            raise AssertionError('one of the date input is not an int')
        if year<0 or month>12 or month<=0:
            raise AssertionError('year or month value invalid')
        if Date.is_leap_year(year):
            local_month_dict=Date.month_dict.copy()
            local_month_dict[2]=29
        if day not in range(1,Date.days_in(year,month)+1):
            raise AssertionError ('invalid day value')
        self.year=year
        self.month=month
        self.day=day
        

    
if __name__ == '__main__':
    # Put in your own simple tests for Date before allowing driver to run
    #d=Date(2016,4,15)
    #len(Date(1912,4,15))
    #d2=Date(2016,1,6) - d
    #print(d2)
    
    
    print()
    import driver
    
    driver.default_file_name = 'bscq31W22.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()



        
        
        
        
        
