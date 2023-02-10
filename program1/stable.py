# Submitter: zhaoyal5(Zhaoyang,Lu)
import prompt
from goody import safe_open

# Use these global variables to index the list associated with each name in the dictionary.
# e.g., if men is a dictionary, men['m1'][match] is the woman who matches man 'm1', and 
# men['m1'][prefs] is the list of preference for man 'm1'.
# It would seems that this list might be better represented as a named tuple, but the
# preference list it contains is mutated, which is not allowed in a named tuple. 

match = 0   # Index 0 of list associate with name is match (str)
prefs = 1   # Index 1 of list associate with name is preferences (list of str)


def read_match_preferences(open_file : open) -> {str:[str,[str]]}:
    pref_d={}
    with open(open_file.name) as file:
        for line in file:
            line=line.rstrip().split(';')
            po_li=[]
            for po_n in range(1,len(line)):
                po_li.append(line[po_n])
            pref_d[line[0]]=[None,po_li]
    return pref_d


def dict_as_str(d : {str:[str,[str]]}, key : callable=None, reverse : bool=False) -> str:
    s=''
    for x in sorted(d.keys(),key=key,reverse=reverse):
        l=d[x]
        s=s+str('  '+x+" -> "+str(l)+'\n')
    print(s)
    return s


def who_prefer(order : [str], p1 : str, p2 : str) -> str:
    for x in order:
        if x ==p1 or x==p2:
            return x


def extract_matches(men : {str:[str,[str]]}) -> {(str,str)}:
    re=set()
    for x in men.keys():
        t=(x,men[x][0])
        re.add(t)
    return re


def make_match(men : {str:[str,[str]]}, women : {str:[str,[str]]}, trace : bool = False) -> {(str,str)}:
    new_men_d={}
    if trace=='True':
        print("Women Preferences (unchanging)\n"+dict_as_str(women))
    for x in men.keys():
        new_men_l=[None,men[x][1].copy()]
        new_men_d[x]=new_men_l
    unmatched=set()
    for x in new_men_d.keys():
        unmatched.add(x)
    w_match_set=extract_matches(women)
    w_match_d=dict(w_match_set)
    while len(unmatched)!=0:
        anyMan=unmatched.pop()
        w=new_men_d[anyMan][1].pop(0)
        if w_match_d[w]==None:
            new_men_d[anyMan][0]=w
            w_match_d[w]=anyMan
        elif w_match_d[w]!=None:
            p=who_prefer(women[w][1], anyMan, w_match_d[w])
            if p==anyMan:
                new_men_d[w_match_d[w]][0]=None
                unmatched.add(w_match_d[w])
                new_men_d[anyMan][0]=w
                w_match_d[w]=anyMan
            elif p==w_match_d[w]:
                unmatched.add(anyMan)
        if trace=='True':
            print("Men Preferences (current)\n"+dict_as_str(new_men_d))
            print("unmatched men = " + str(unmatched))
            print(str(anyMan) + " proposes to " +str(w), end='')
            if w_match_d[w]==None:
                print(", who is an unmatched woman; so she accepts the proposal")
            elif w_match_d[w]!=None:
                p=who_prefer(women[w][1], anyMan, w_match_d[w])
                if p==anyMan:
                    print(', who is a matched woman who prefers her new match; so she accepts the proposal')
                elif p==w_match_d[w]:
                    print(', who is a matched woman who prefers her current match; so she rejects the proposal')
    re=set()
    for x in new_men_d.keys():
        t=(x,new_men_d[x][0])
        re.add(t)
    return re
  


  
    
if __name__ == '__main__':
    # Write script here
    file_name_men = safe_open('Select a file storing the preferences of the men','r','Illegal file name')
    file_name_women = safe_open('Select a file storing the preferences of the women','r','Illegal file name')
    men_r=read_match_preferences(file_name_men)
    women_r=read_match_preferences(file_name_women)
    print()
    dict_as_str(men_r)
    dict_as_str(women_r)
    while True:
        trac=input("Select Tracing of Execution[True]:")
        if trac in ["True","False",""]:
            m=make_match(men_r, women_r, trac)
            break
        else:
            print("not valid input")
    print("The calculated matches are "+str(m))
    
    
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
