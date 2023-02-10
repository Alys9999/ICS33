import prompt
import goody

# Use these global variables to index the list associated with each name in the dictionary.
# e.g., if men is a dictionary, men['m1'][match] is the woman who matches man 'm1', and 
# men['m1'][prefs] is the list of preference for man 'm1'.
# It would seems that this list might be better represented as a named tuple, but the
# preference list it contains is mutated, which is not allowed in a named tuple. 

match = 0   # Index 0 of list associate with name is match (str)
prefs = 1   # Index 1 of list associate with name is preferences (list of str)

def read_match_preferences(open_file : open) -> {str:[str,[str]]}:
    ds = dict()
    for line in open_file:
        entry = line.rstrip().split(';')
        ds[entry[0]] = [None,entry[1:]]
    open_file.close()
    return ds


def dict_as_str(d : {str:[str,[str]]}, key : callable=None, reverse : bool=False) -> str:
#     answer = ''
#     for k in sorted(d,key=key,reverse=reverse):
#         answer += '  '+str(k)+' -> '+str(d[k])+'\n'
#     return answer
    return '\n'.join('  '+str(k)+' -> '+str(d[k]) for k in sorted(d,key=key,reverse=reverse))+'\n'


def who_prefer(order : [str], p1 : str, p2 : str) -> str:
    return p1 if order.index(p1) < order.index(p2) else p2


def extract_matches(men : {str:[str,[str]]}) -> {(str,str)}:
    return {(m,w) for m,(w,p) in men.items()}


def make_match(men : {str:[str,[str]]}, women : {str:[str,[str]]}, trace : bool = False) -> {(str,str)}:
    men = {m:[w,list(o)] for m,[w,o] in men.items()}
    
    unmatched = {k for k in men}
    
    if trace: print('\nWomen Preferences (unchanging)\n'+dict_as_str(women))
    while unmatched:
        if trace: print('Men Preferences (current)\n'+dict_as_str(men),'\nunmatched men =',unmatched,'\n')
        man = unmatched.pop()
        woman = men[man][prefs].pop(0)
        if trace: print(man,'proposes to',woman,end='; ')
        if women[woman][match] == None:
            if trace: print('unmatched woman accepts proposal\n')
            men[man][match] = woman
            women[woman][match] = man
        else:
            best = who_prefer(women[woman][1],women[woman][match],man)
            if best == man:
                if trace: print('matched woman accepts proposal, rejecting match with', women[woman][match],'\n')
                unmatched.add(women[woman][match])
                men[women[woman][match]][match] = None
                men[man][match] = woman
                women[woman][match] = man
            else:
                unmatched.add(man)
                if trace: print('matched woman rejects proposal (likes current match better)\n')
   
    if trace: print('algorithm terminates, matches =', extract_matches(men))
    return extract_matches(men)
    
  
  

    
if __name__ == '__main__':
    men_file   = goody.safe_open('Enter a file representing mens   preferences', 'r', 'Could not find that file','men3.txt')
    women_file = goody.safe_open('Enter a file representing womens preferences', 'r', 'Could not find that file','women3.txt')
    men = read_match_preferences(men_file)
    women = read_match_preferences(women_file)
    
    print('\nMen Preferences\n'+dict_as_str(men))
    print('Women Preferences\n'+dict_as_str(women))
    
    matches = make_match(men,women,prompt.for_bool('Trace Algorithm',default=True))
    
    print('\nmatches =',matches)
    
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
