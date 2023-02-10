from predicate import is_even, is_prime, is_positive
from collections import defaultdict  # Use or ignore


def integrate(f : callable, n : int) -> callable:
    assert type(n) is int and n > 0, f'q1solutionS18.integrate: n({n}) in not > 0'
     
    def definite(a : float, b : float) -> float:
        assert a <= b, f'q1solutionS18.integrate: a({a}) is not <= b({b})'
        definite.zcc = 0 # The function object exists when its code executes
        dx = (b-a)/n
        integral = 0
        for i in range(n):
            if i > 0 and (f(a+(i-1)*dx) >= 0) != (f(a+i*dx) >= 0):
                definite.zcc += 1
            integral += f(a+i*dx)*dx
        return integral
    return definite



def stocks(db : {str: [(str,int,int)]}) -> {str}:
    return {stock for transactions in db.values() for stock,_,_ in transactions}



def clients_by_volume(db : {str: [(str,int,int)]}) -> [str]:
    return sorted(db, key = (lambda client : (-sum(abs(shares) for _,shares,_ in db[client]),client))  )



def stocks_by_volume(db : {str: [(str,int,int)]}) -> [(str,int)]:
    return sorted( [(astock,sum([abs(shares) for transactions in db.values() for s,shares,_ in transactions if s==astock]))
                       for astock in stocks(db)],
                    key = lambda x : (-x[1],x[0]))
    


def by_stock(db : {str: [(str,int,int)]}) -> {str: {str: [(int,int)]}}:
    answer = defaultdict(lambda : defaultdict(list))
    for client,transactions in db.items():
        for stock,shares,cost in transactions:
            answer[stock][client].append( (shares,cost) )
    return {k:{k2:v2 for k2,v2 in v.items()} for k,v in answer.items()}



def summary(db : {str: [(str,int,int)]}, prices : {str: int}) -> {str: ({str: int}, int)}:
    def worth(hold : {str: int}):
        return sum(shares*prices[stock] for stock,shares in hold.items())
        
    holdings = defaultdict(lambda : defaultdict(int))
    for client,transactions in db.items():
        for stock,buysell,_ in transactions:
            holdings[client][stock] += buysell
    return {client: ({stock: amount for stock,amount in holdings[client].items() if amount != 0},
                      worth(holdings[client])) for client in holdings}
    # or
    return {client: ({stock: amount for stock,amount in holdings[client].items() if amount != 0},
                      sum((shares*prices[stock] for stock,shares in holdings[client].items()))) for client in holdings}





if __name__ == '__main__':
    print('Testing integrate')
    f = integrate( (lambda x : x), 10)
    print(f(-1,1),f.zcc)
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
    driver.default_file_name = 'bscq1W22.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
