import prompt                          # for driver, which prompts user
from collections import defaultdict    # use if you want (see problem descriptions)

# You might use the following abbreviations (or their full names)
#   for the various parts of the Warehouse database

# i    : inventory (how many products are available)
# p    : product
# w    : warehouse


def read_db  (openfile : open)  ->  {str:{str:int}}:
    re_li=[]
    re_d={}
    with open(openfile.name) as open_file:
        for line in open_file:
            line=line.strip().split(':')
            ty=line[0]
            for x in range(1,len(line),2):
                if line[x].isalpha():
                    re_li.append((line[x],ty,line[x+1]))
    for x in re_li:
        pair_d={}
        if x[0] not in re_d.keys():
            pair_d[x[1]]=int(x[2])
            re_d[x[0]]=pair_d
        elif x[0] in re_d.keys():
            pair_d=re_d[x[0]]
            pair_d[x[1]]=int(x[2])
            re_d[x[0]]=pair_d
    return re_d


        
def inventory  (db : {str:{str:int}})  ->  [(str,int)]: 
    re_d={}
    for x in db.keys():
        for y in db[x].keys():
            if y not in re_d.keys():
                re_d[y]=db[x][y]
            elif y in re_d.keys():
                num=re_d[y]
                num+=db[x][y]
                re_d[y]=num
    re_li=list((i[0],i[1]) for i in sorted(re_d.items(), key= lambda o:o[1], reverse=True))
    return re_li



def resupply  (db : {str:{str:int}},   must_have : int)  ->  {str: {(str,int)}}:    
    re_d={}
    for x in db.keys():
        for y in db[x].keys():
            if db[x][y]<3:
                num=3-int(db[x][y])
                if y not in re_d.keys():
                    tu=((x,num))
                    s=set()
                    s.add(tu)
                    re_d[y]=s
                else:
                    co=set(re_d[y])
                    tu=(x,num)
                    co.add(tu)
                    re_d[y]=co
            else:
                continue
    return re_d


            
def update_purchases  (db : {str:{str:int}},  purchases : [(str,str)] )  ->  {(str,str)}:    
    pass


      
def product_locations  (db : {str:{str:int}})  ->  [(str,[(str,int)])]:    
    re_li=[]
    re_d={}
    for k in db.keys():
        for k2 in db[k]:
            place=k
            ty=k2
            inte=db[k][k2]
            re_li.append((k2,k,db[k][k2]))
    for x in re_li:
        pair_d={}
        if x[0] not in re_d.keys():
            pair_d[x[1]]=int(x[2])
            re_d[x[0]]=pair_d
        elif x[0] in re_d.keys():
            pair_d=re_d[x[0]]
            pair_d[x[1]]=int(x[2])
            re_d[x[0]]=pair_d
    re_li=[]
    for a in re_d.keys():
        for b in re_d[a].keys():
            re_li.append((a,[(b,re_d[a][b])]))
    return re_li



def unique_supplier  (db : {str:{str:int}})  ->  {str:{str}}:    
    pass


 
if __name__ == '__main__':
    # You can add any of your own specific testing code here
    # You can comment-out tests after your code passes them (but don't change your code!)
     
    # checks whether answer is correct, printing appropriate information
    # Note that dict/defaultdict will compare == if they have the same keys and
    #   associated values, regardless of the fact that they print differently
    def check (answer, correct):
        if (answer == correct):
            print ('    CORRECT')
        else:
            print ('    INCORRECT')
            print ('      was       =',answer)
            print ('      should be =',correct)
        print()
 
  
    # These tests are similar to those that the driver will execute for batch self-checks
    # To run a test, enter True (or just press enter); to skip a test, enter False 
         
    '''if prompt.for_bool('Test read_db?', True): 
        db = 'db1.txt'
        answer = read_db(open(db))
        print('  db =',db,'\n  read_db =',answer)
        check(answer, {'Irvine':  {'brush': 3,    'comb': 2,    'wallet': 2},
                       'Newport': {'comb': 1,     'stapler': 0},
                       'Tustin' : {'keychain': 3, 'pencil': 4,  'wallet': 3}})


        db = 'db2.txt'
        answer = read_db(open(db))
        print('  db =',db,'\n  read_db =',answer)
        check(answer, {'Irvine':  {'brush': 4, 'comb': 2, 'keychain': 6, 'lipgloss': 3, 'wallet': 3},
                       'Newport': {'brush': 1, 'comb': 5, 'keychain': 3, 'lipgloss': 6, 'wallet': 1},
                       'Tustin':  {'brush': 1, 'comb': 3, 'keychain': 2, 'lipgloss': 4, 'wallet': 2}})

    ##################################################
              

    if prompt.for_bool('Test inventory?', True): 
        db = {'Irvine':  {'brush': 3,    'comb': 2,    'wallet': 2},
              'Newport': {'comb': 1,     'stapler': 0},
              'Tustin' : {'keychain': 3, 'pencil': 4,  'wallet': 3}}

        answer = inventory(db)
        print('  db =',db,'\n  inventory =',answer)
        check(answer, [('wallet', 5), ('pencil', 4), ('brush', 3), ('comb', 3), ('keychain', 3), ('stapler', 0)])

 
        db = {'Irvine':  {'brush': 4, 'comb': 2, 'keychain': 6, 'lipgloss': 3, 'wallet': 3},
              'Newport': {'brush': 1, 'comb': 5, 'keychain': 3, 'lipgloss': 6, 'wallet': 1},
              'Tustin':  {'brush': 1, 'comb': 3, 'keychain': 2, 'lipgloss': 4, 'wallet': 2}}

        answer = inventory(db)
        print('  db =',db,'\n  inventory =',answer)
        check(answer, [('lipgloss', 13), ('keychain', 11), ('comb', 10), ('brush', 6), ('wallet', 6)])

 
    ##################################################
              
'''
    if prompt.for_bool('Test resupply?', True): 
        db = {'Irvine':  {'brush': 3,    'comb': 2,    'wallet': 2},
              'Newport': {'comb': 1,     'stapler': 0},
              'Tustin' : {'keychain': 3, 'pencil': 4,  'wallet': 3}}

        answer = resupply(db,3)
        print('  db =',db,'\n  resupply =',answer)
        check(answer, {'comb': {('Newport', 2), ('Irvine', 1)}, 'wallet': {('Irvine', 1)}, 'stapler': {('Newport', 3)}})

 
        db = {'Irvine':  {'brush': 4, 'comb': 2, 'keychain': 6, 'lipgloss': 3, 'wallet': 3},
              'Newport': {'brush': 1, 'comb': 5, 'keychain': 3, 'lipgloss': 6, 'wallet': 1},
              'Tustin':  {'brush': 1, 'comb': 3, 'keychain': 2, 'lipgloss': 4, 'wallet': 2}}

        answer = resupply(db,4)
        print('  db =',db,'\n  resupply =',answer)
        check(answer, {'comb': {('Tustin', 1), ('Irvine', 2)}, 'lipgloss': {('Irvine', 1)}, 'wallet': {('Tustin', 2), ('Newport', 3), ('Irvine', 1)}, 'brush': {('Tustin', 3), ('Newport', 3)}, 'keychain': {('Tustin', 2), ('Newport', 1)}})

 
    ##################################################
    
         
    if prompt.for_bool('Test update_purchases?', True): 
        db = {'Irvine':  {'brush': 3,    'comb': 2,    'wallet': 2},
              'Newport': {'comb': 1,     'stapler': 0},
              'Tustin' : {'keychain': 3, 'pencil': 4,  'wallet': 3}}
        purchases = [('Irvine', 'brush'), ('Newport','comb'), ('Tustin', 'car'), ('Newport', 'comb')]

        answer = update_purchases(db,purchases)
        print('  db =',db,'\n  update_purchases =',answer)
        check(answer, {('Tustin', 'car'), ('Newport', 'comb')})
        print('  db mutated =',db)
        check(db, {'Irvine':  {'brush': 2,    'comb': 2,    'wallet': 2},
                   'Newport': {'comb': 0,     'stapler': 0},
                   'Tustin' : {'keychain': 3, 'pencil': 4,  'wallet': 3}})

        
        db = {'Irvine':  {'brush': 4, 'comb': 2, 'keychain': 6, 'lipgloss': 3, 'wallet': 3},
              'Newport': {'brush': 1, 'comb': 5, 'keychain': 3, 'lipgloss': 6, 'wallet': 1},
              'Tustin':  {'brush': 1, 'comb': 3, 'keychain': 2, 'lipgloss': 4, 'wallet': 2}}
        purchases = [('Santa-Ana','brush'), ('Tustin', 'brush'), ('Newport','keychain'), ('Newport', 'food'), ('Tustin', 'brush')]

        answer = update_purchases(db,purchases)
        print('  db =',db,'\n  update_purchases =',answer)
        check(answer, {('Newport', 'food'), ('Santa-Ana','brush'),('Tustin', 'brush')})
        print('  db mutated =',db)
        check(db, {'Irvine':  {'brush': 4, 'comb': 2, 'keychain': 6, 'lipgloss': 3, 'wallet': 3},
                   'Newport': {'brush': 1, 'comb': 5, 'keychain': 2, 'lipgloss': 6, 'wallet': 1},
                   'Tustin':  {'brush': 0, 'comb': 3, 'keychain': 2, 'lipgloss': 4, 'wallet': 2}})

        
    ##################################################
   
         
    if prompt.for_bool('Test product_locations?', True): 
        db = {'Irvine':  {'brush': 3,    'comb': 2,    'wallet': 2},
              'Newport': {'comb': 1,     'stapler': 0},
              'Tustin' : {'keychain': 3, 'pencil': 4,  'wallet': 3}}


        answer = product_locations(db)
        print('  db =',db,'\n  product_locations =',answer)
        check(answer, [('brush', [('Irvine', 3)]),
                       ('comb', [('Irvine', 2), ('Newport', 1)]),
                       ('keychain', [('Tustin', 3)]),
                       ('pencil', [('Tustin', 4)]),
                       ('stapler', [('Newport', 0)]),
                       ('wallet', [('Irvine', 2), ('Tustin', 3)])])
 
 
        db = {'Irvine':  {'brush': 4, 'comb': 2, 'keychain': 6, 'lipgloss': 3, 'wallet': 3},
              'Newport': {'brush': 1, 'comb': 5, 'keychain': 3, 'lipgloss': 6, 'wallet': 1},
              'Tustin':  {'brush': 1, 'comb': 3, 'keychain': 2, 'lipgloss': 4, 'wallet': 2}}


        answer = product_locations(db)
        print('  db =',db,'\n  product_locations =',answer)
        check(answer,  [('brush', [('Irvine', 4), ('Newport', 1), ('Tustin', 1)]),
                        ('comb', [('Irvine', 2), ('Newport', 5), ('Tustin', 3)]),
                        ('keychain', [('Irvine', 6), ('Newport', 3), ('Tustin', 2)]),
                        ('lipgloss', [('Irvine', 3), ('Newport', 6), ('Tustin', 4)]),
                        ('wallet', [('Irvine', 3), ('Newport', 1), ('Tustin', 2)])])
 
 
    ##################################################
              

    if prompt.for_bool('Test unique_supplier?', True): 
        db = {'Irvine':  {'brush': 3,    'comb': 2,    'wallet': 2},
              'Newport': {'comb': 1,     'stapler': 0},
              'Tustin' : {'keychain': 3, 'pencil': 4,  'wallet': 3}}
        answer = unique_supplier(db)
        print('  db =',db,'\n  unique_supplier =',answer)
        check(answer, {'Irvine': {'brush'}, 'Newport': {'stapler'}, 'Tustin': {'pencil', 'keychain'}})

        
        db = {'Irvine':  {'brush': 4, 'comb': 2, 'keychain': 6,                'wallet': 3},
              'Newport': {            'comb': 5, 'keychain': 3, 'lipgloss': 6, 'wallet': 1},
              'Tustin':  {            'comb': 3, 'keychain': 2,                'wallet': 2}}


        answer = unique_supplier(db)
        print('  db =',db,'\n  unique_supplier =',answer)
        check(answer, {'Irvine':{'brush'}, 'Newport': {'lipgloss'}})
 
 
 
    ##################################################
