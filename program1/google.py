import prompt 
from goody       import safe_open,irange
from collections import defaultdict # Use defaultdict for prefix and query


def all_prefixes(fq : (str,)) -> {(str,)}:
    s=set()
    for x in range(1,len(fq)+1):
        s.add(fq[:x])
    return s

        
def add_query(prefix : {(str,):{(str,)}}, query : {(str,):int}, new_query : (str,)) -> None:
    all_p_new=all_prefixes(new_query)
    for x in all_p_new:
        if x in prefix.keys():
            cont=prefix[x]
            cont.add(new_query)
            prefix[x]=cont
        else:
            prefix[x]={new_query}
    if new_query in query.keys():
        query[new_query]+=1
    else:
        query[new_query]=1


def read_queries(open_file : open) -> ({(str,):{(str,)}}, {(str,):int}):
    prefix=defaultdict()
    query=defaultdict()
    with open(open_file.name) as open_file:
        for line in open_file:
            line=tuple(line.replace('\n','').split(' '))
            add_query(prefix,query,line)
    return prefix,query
            


def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    s=''
    sorted_q=sorted(d.keys(),key=key,reverse=reverse)
    for x in sorted_q:
        s+='  '+str(x)+' -> '+str(d[x])+'\n'
    print(s)
    return s


def top_n(a_prefix : (str,), n : int, prefix : {(str,):{(str,)}}, query : {(str,):int}) -> [(str,)]:
    sorted_q=dict(sorted(query.items(), key=lambda kv: (-kv[1], kv[0])))
    re_li=[]
    try:
        possibles=prefix[a_prefix]
    except KeyError:
        re_li=[]
        return re_li
    c=0
    for x in sorted_q.keys():
        for possible in possibles:
            if x==possible:
                re_li.append(x)
                c+=1
        if c==n:
            break
    return re_li

# Script

if __name__ == '__main__':
    # Write script here
    #all_prefixes(('uci','medical','center'))
    #add_query(p,q,('u','m','c'))
    #p,q = read_queries(open('googleq0.txt'))
    #d = defaultdict(a=5, ab=2, am=5, ax=4, abc=3, abz=6, aza=1, lmnop=3)
    #dict_as_str(d,lambda x : (len(x),x))  
    #p = {('u', 'w', 's'): {('u', 'w', 's')}, ('u', 'w'): {('u', 'w', 's'), ('u', 'w', 'b')}, ('u', 'm', 'c'): {('u', 'm', 'c')}, ('u', 'l'): {('u', 'l')}, ('u', 'm'): {('u', 'm', 'c')}, ('u',): {('u', 'w', 's'), ('u', 'l'), ('u', 'm', 'c'), ('u', 'w', 'b')}, ('u', 'w', 'b'): {('u', 'w', 'b')}}
    #q = {('u', 'w', 's'): 2, ('u', 'l'): 2, ('u', 'm', 'c'): 1, ('u', 'w', 'b'): 3} 
    #top_n(('x',),3,p,q)
    q_file = safe_open('Select a file storing multiple full queries','r','Illegal file name')
    p,q=read_queries(q_file)
    print('Prefix dictionary:')
    dict_as_str(p, key=lambda x:len(x))
    print('Query dictionary:')
    dict_as_str(q, key= lambda x:q[x], reverse=True)
    while True:
        inp=input(' Select a single prefix sequence (or done to stop):')
        if inp=='done':
            break
        matching_q=top_n(tuple(inp.split(' ')), 3, p, q)
        print('Matching full queries (up to 3; High->Low frequency) = '+str(matching_q))
        inp2=input('Select a single full query sequence (or done to stop):')
        if inp2=='done':
            break
        add_query(p, q, tuple(inp2.split(' ')))
        print('Prefix dictionary:')
        dict_as_str(p,key = lambda x:len(x[0]))
        print('Query dictionary:')
        dict_as_str(q, key=lambda x:x[1], reverse=True)
    
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
