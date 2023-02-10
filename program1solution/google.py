import prompt 
from  goody       import safe_open,irange
from  collections import defaultdict # Use a defaultdict for prefix and query


def all_prefixes(full : (str,)) -> {(str,)}:
    return {full[0:i] for i in irange(1,len(full))}


def add_query(prefix : {(str,):{(str,)}}, query : {(str,):int}, new_query : (str,)) -> None:
    for p in all_prefixes(new_query):
        prefix[p].add(new_query)
    query[new_query] += 1


def read_queries(open_file : open) -> ({(str,):{(str,)}}, {(str,):int}):
    prefix = defaultdict(set)
    query  = defaultdict(int)
    for l in open_file:
        add_query(prefix, query,tuple(l.rstrip().split(' ')))
    open_file.close()
    return (prefix,query) # in tuple


def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
#     answer = ''
#     for k in sorted(d,key=key,reverse=reverse):
#         answer += '  '+str(k)+' -> '+str(d[k])+'\n'
#     return answer
    return '\n'.join('  '+str(k)+' -> '+str(d[k]) for k in sorted(d,key=key,reverse=reverse))+'\n'


def top_n(a_prefix : (str,), n : int, prefix : {(str,):{(str,)}}, query : {(str,):int}) -> [(str,)]:
#     answer = [x for x in prefix[a_prefix]]
#     answer.sort(key=lambda x: (-query[x],x))
#     return answer[0:n]
    return sorted([x for x in prefix.get(a_prefix,[])],key=lambda x: (-query[x],x))[0:n]




# Script

if __name__  ==  '__main__':
    file_to_read = safe_open('Enter name of file contaiing full queries', 'r', 'Could not find that file',default='googleq0.txt')
    (prefix,query) = read_queries(file_to_read)
    
    while (True):
        print('\nPrefix dictionary:\n' + dict_as_str(prefix,key=lambda x: (len(x),x)),  end='')
        print('\nQuery dictionary:\n'  + dict_as_str(query,key=lambda x: (-query[x],x)),end='')
        a_prefix = prompt.for_string('\nEnter a prefix (or quit)')
        if a_prefix == 'quit':
            break;
        print('  Top 3 (at most) full queries =', top_n(tuple(a_prefix.split(' ')),3,prefix,query))
        a_prefix = prompt.for_string('\nEnter a full query (or quit)')
        if prefix == 'quit':
            break;
        add_query(prefix,query,tuple(a_prefix.split(' ')))
        
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
