from predicate import is_even, is_prime, is_positive
from collections import defaultdict  # Use or ignore


def integrate(f : callable, n : int) -> callable:
    if n <= 0:
        raise AssertionError("n not greater than 0")
    def int_f(a:float,b:float)->float:
        int_f.zcc=0
        if a>b:
            raise AssertionError("a is not less or equal to b")
        dx=(b-a)/n
        height_list=[]
        height=0
        for x in range(0,n):
            height=f(a+x*dx)
            height_list.append(height)
        for h in range(len(height_list)-1):
            if height_list[h]*height_list[h+1]<=0.0:
                if height_list[h]==0.0:
                    int_f.zcc-=1
                int_f.zcc+=1
        total_height=sum(height_list)
        return total_height*dx  
    return int_f


def stocks(db : {str: [(str,int,int)]}) -> {str}:
    stock_names=set()
    all_lists=list(db.values())
    for x in range(len(all_lists)):
        one_list=all_lists[x]    
        for i in one_list:
            stock_names.add(i[0])
    return stock_names



def clients_by_volume(db : {str: [(str,int,int)]}) -> [str]:
    c=db.keys()
    re_dict=dict()
    re_list=[]
    for i in c:
        re_dict[i]=0
        for x in db[i]:
            num=re_dict[i]+abs(x[1])
            re_dict[i]=num
    sorted_key=dict()
    for key in sorted(re_dict):
        sorted_key[key]=re_dict[key]
    client_list=sorted(sorted_key.items(), key=lambda x:x[1], reverse=True)
    for client in client_list:
        re_list.append(client[0])
    return re_list




def stocks_by_volume(db : {str: [(str,int,int)]}) -> [(str,int)]:
    s=list(db.values())
    name_list=list(stocks(db))
    stock_dict=dict()
    for stock in name_list:
        stock_dict[stock]=0
    re_list=[]
    for x in range(len(s)):
        for y in s[x]:
            num=stock_dict[y[0]]+abs(y[1])
            stock_dict[y[0]]=num
    sorted_key=dict()
    for key in sorted(stock_dict):
        sorted_key[key]=stock_dict[key]
    stock_sorted_list=sorted(sorted_key.items(), key=lambda x:x[1], reverse=True)

    return stock_sorted_list



def by_stock(db : {str: [(str,int,int)]}) -> {str: {str: [(int,int)]}}:
    stock_names=set()
    full_dict={}
    all_lists=list(db.values())
    for x in range(len(all_lists)):
        one_list=all_lists[x]    
        for i in one_list:
            stock_names.add(i[0])
    c=list(db.keys())
    for stock in sorted(list(stock_names)):
        full_dict[stock]=[]
        client_share_dict={}
        for cli in c:
            for tup in db[cli]:
                if tup[0]==stock:
                    client_share_list=[]
                    if cli in client_share_dict:
                        client_share_list=client_share_dict[cli]
                    client_share_list.append((tup[1],tup[2]))
                    client_share_dict[cli]=client_share_list
                    full_dict[stock]=client_share_dict
                    
    return full_dict
                    
                    
                    




def summary(db : {str: [(str,int,int)]}, prices : {str: int}) -> {str: ({str: int}, int)}:
    client_dict={}
    c=db.keys()
    for x in c:
        stock_dict={}
        trade_num=0
        for y in db[x]:
            if y[0] in stock_dict:
                num=stock_dict[y[0]]+y[1]
                stock_dict[y[0]]=num
            elif y[0] not in stock_dict:
                stock_dict[y[0]]=y[1]
            if stock_dict[y[0]]==0:
                del stock_dict[y[0]]
        for i in stock_dict.keys():
            for s in prices.keys():
                if s==i:
                    trade_num=trade_num+stock_dict[i]*prices[s]
            
        stock_tuple=(stock_dict, trade_num)
        client_dict[x]=stock_tuple
        
    return client_dict



if __name__ == '__main__':
    print('Testing integrate')

    f = integrate( (lambda x : 3*x**2 - 6*x + 1), 1000)
    print(f(-1,2),f.zcc)
    f = integrate( (lambda x : -5*x**5 + 3*x**4 + 8*x**3 - 1), 1000)
    print(f(-2,2),f.zcc)
  
   
    # Note: the keys in this dicts are not specified in alphabetical order
    db1 = {
            'Carl': [('Intel', 30, 40), ('Dell' , 20, 50), ('Intel',-10, 60), ('Apple', 20, 55)],
            'Barb': [('Intel', 20, 40), ('Intel',-10, 45), ('IBM',   40, 30), ('Intel',-10, 35)],
            'Alan': [('Intel', 20, 10), ('Dell',  10, 50), ('Apple', 80, 80), ('Dell', -10, 55)],
            'Dawn': [('Apple', 40, 80), ('Apple', 40, 85), ('Apple',-40, 90)]
           }

    db2 = {
            'Hope': [('Intel',30,40), ('Dell',20,50), ('IBM',10,80), ('Apple',20,90), ('QlCom',20,20)],
            'Carl': [('QlCom',30,22), ('QlCom',20,23), ('QlCom',-20,25), ('QlCom',-30,28)],
            'Barb': [('Intel',80,42), ('Intel',-80,45), ('Intel',90,28)],
            'Fran': [('BrCom',210,62), ('BrCom',-20,64), ('BrCom',-10,66), ('BrCom',10,55)],
            'Alan': [('Intel',20,10), ('Dell', 10,50), ('Apple',80,80), ('Dell',-10,55)],
            'Gabe': [('IBM',40,82), ('QlCom',80,25), ('IBM',-20,84), ('BrCom',50,65), ('QlCom',-40,28)],
            'Dawn': [('Apple',40,92), ('Apple',40,98), ('Apple',-40,92)],
            'Evan': [('Apple',50,92), ('Dell',20,50), ('Apple',-10,95), ('Apple',20,95), ('Dell',-20,90)]
           }

    prices1 = {'IBM': 65, 'Intel': 60, 'Dell': 55, 'Apple': 70}
    
    prices2 = {'IBM': 85, 'Intel': 45, 'Dell': 50, 'Apple': 90, 'QlCom': 20, 'BrCom': 70}
   

    print('\nTesting stocks')
    print('stocks(db1):',stocks(db1))
    print('stocks(db2):',stocks(db2))


    print('\nTesting clients_by_volume')
    print ('clients_by_volume(db1):',clients_by_volume(db1))
    print ('clients_by_volume(db2):',clients_by_volume(db2))


    print('\nTesting stocks_by_volume')
    print ('stocks_by_volume(db1):',stocks_by_volume(db1))
    print ('stocks_by_volume(db2):',stocks_by_volume(db2))


    print('\nTesting by_stock')
    print ('by_stock(db1):',by_stock(db1))
    print ('by_stock(db2):',by_stock(db2))


    print('\nTesting summary')
    print ('summary(db1):',summary(db1,prices1))
    print ('summary(db2):',summary(db2,prices2))


    print('\ndriver testing with batch_self_check:')
    import driver
    driver.default_file_name = '1.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
