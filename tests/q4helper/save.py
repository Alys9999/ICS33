def alternate_i(ll1 : LN, ll2 : LN) -> LN:
    # Handle the case of ll1 or ll2 being empty
    if ll1==None and ll2==None:
        return None
    elif ll1==None:
        return ll2
    elif ll2==None:
        return ll1
    # Set up for iteration (keep track of front and rear of linked list to retur
    rl=[]
    # while True: with both l1 and l2 not empty and ll1 is in the linked list to return
    while ll1!=None and ll2!=None:
        rl.append(ll1.value)
        rl.append(ll2.value)
        ll1=ll1.next
        ll2=ll2.next
        if ll1 == None:
            while ll2 != None:
                rl.append(ll2.value)
                ll2=ll2.next
        if ll2 == None:
            while ll1 != None:
                rl.append(ll1.value)
                ll1=ll1.next
            
    return list_to_ll(rl)