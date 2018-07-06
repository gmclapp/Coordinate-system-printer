import random

class item():
    def __init__(self):
        self.fcost = new = 10*random.random()
        
def sort_up(stuff):
    i = len(stuff)-1
    while(len(stuff)>1):
        p_i = int((i-1)/2)
        try:
            if stuff[i].fcost<stuff[p_i].fcost:
                stuff[i],stuff[p_i] = stuff[p_i],stuff[i]
                i = p_i
            else:
                break
        except IndexError:
            break

def sort_down(stuff):
    i = 0
    while(len(stuff)>1):
        lt_child_i = i*2 + 1
        rt_child_i = i*2 + 2

        try:
            if (stuff[i].fcost>stuff[lt_child_i].fcost
                or stuff[i].fcost>stuff[rt_child_i].fcost):
                if (stuff[lt_child_i].fcost<stuff[rt_child_i].fcost):
                    stuff[i],stuff[lt_child_i] = stuff[lt_child_i],stuff[i]
                    i=lt_child_i
                else:
                    stuff[i],stuff[rt_child_i] = stuff[rt_child_i],stuff[i]
                    i=rt_child_i
            else:
                break
            
        except IndexError:
            break

def next_num(stuff):
    new = item()
    stuff.append(new)
    sort_up(stuff)
##    for i in stuff:
##        print("%5.3f" %i.fcost)
    return(stuff)

def extract_num(stuff):
    stuff[-1],stuff[0]=stuff[0],stuff[-1]
    e = stuff.pop(-1)
    print("%5.3f" %e.fcost,'\n')
    sort_down(stuff)
##    for i in stuff:
##        print("%5.3f" %i.fcost)
    return(stuff)
    

stuff = []

    
    
