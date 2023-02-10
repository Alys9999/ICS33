# Submitter: zhaoyal5(Zhaoyang,Lu)

import prompt
from goody       import safe_open
import math
import collections


def read_graph(open_file : open) -> {str:{str}}:
    pre=set()
    pre_d= collections.defaultdict(set)
    rela_d={}
    open_file=open_file.name
    with open(open_file) as file:
        for line in file:
            line=line.rstrip().split(';')
            if len(line)==1:
                pre_d[line[0]]=set()
            else:
                p=(line[0],line[1])
                pre.add(p)
    for k,v in pre:
        pre_d[v].add(k)
        pre_d[k].add(v)
    rela_d=(dict(pre_d))
    return rela_d


def graph_as_str(graph : {str:{str}}) -> str:
    s=''
    for x in sorted(graph.keys()):
        l=sorted(list(graph[x]))
        s=s+str('  '+x+" -> "+str(l)+'\n')
    print(s)
    return s


def find_influencers(graph : {str:{str}}, trace : bool = False) -> {str}:
    infl_dict={}
    for x in graph.keys():
        friend_num=len(graph[x])
        ceil_num=math.ceil(friend_num/2)
        i_zero=friend_num-ceil_num
        if friend_num==0:
            i_zero=-1
        li=[i_zero,friend_num,x]
        infl_dict[x]=li
    while True:
        if trace==str(True):
            print("influencer dictionary = "+str(infl_dict))
        tup_list=[]
        for k in infl_dict.keys():
            if infl_dict[k][0]>=0:
                tup_list.append(infl_dict[k])
        if tup_list==[]:
            return set(infl_dict.keys())
        else:
            min_tup=min(tup_list)
            friends=graph[min_tup[2]]
            del (infl_dict[min_tup[2]])   
            for n in infl_dict.keys():
                if n in friends:
                    infl_dict[n][0]-=1
                    infl_dict[n][1]-=1
        if trace==str(True):
            print("removal candidates = "+ str(tup_list))
            print(str(min_tup)+" is the smallest candidate")
            print("Removing "+min_tup[2]+" as key from influencer dictionary; decrementing every friend's value" )


def all_influenced(graph : {str:{str}}, influencers : {str}) -> {str}:
    c=0
    infl_dict={}
    for k in graph.keys():
        if k in influencers:
            infl_dict[k]=True
            c+=1
        else:
            infl_dict[k]=False
    while True:
        t_count=0
        for k_two in infl_dict.keys():
            m=math.ceil(len(graph[k_two])/2)
            if infl_dict[k_two]==False and len(graph[k_two])!=0:
                infl_n=0
                for i in graph[k_two]:
                    if infl_dict[i]:
                        infl_n+=1
                if infl_n>=m:
                    infl_dict[k_two]=True
        for v in infl_dict.values():
            if v==True:
                t_count=t_count+1
        if c==t_count:
            re=filter(lambda x: infl_dict[x]==True, list(infl_dict.keys()))
            s=set(re)
            return s
        else:
            c=t_count
       
            
    
if __name__ == '__main__':
    # Write script here
    file_name = safe_open('Select a file storing a friendship graph','r','Illegal file name')
    print("Graph: person -> [sorted friends of person]")
    rela_d=read_graph(file_name)
    graph_as_str(rela_d)
    while True:
        trace_tri=input("Select Tracing of Execution[False]:")
        if trace_tri in ["True","False",""]:
            infu_set=find_influencers(rela_d,trace_tri)
            break
        else:
            print("not valid input")
    print('The influencers set calculated is '+str(infu_set))
    while True:
        notValid=False
        n=input("Select a subset of persons (or enter done to stop)"+str(infu_set)+":")
        for x in n.split(';'):
            if x not in list(rela_d.keys()):
                notValid=True 
        if n=="done":
            break
        elif notValid==True:
            print("Please enter a legal String")
        else:
            al_f=all_influenced(rela_d, n)
            per=len(al_f)/len(rela_d.keys())
            print("People influenced by selected subset ("+str(per)+" of graph)"+str(al_f))
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()

