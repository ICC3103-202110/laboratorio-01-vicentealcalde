import random 

def create_table (n_cards):
    cards_1=[random.randint(1,n_cards) for _ in range(n_cards)]
    cards_2=cards_1[:]
    tabl= cards_1 + cards_2 #tabl = table 
    random.shuffle(tabl) #first disorder
    random.shuffle(tabl) #second disorder 
    n=cube(tabl)
    if n[0]>n[1]:
        row=n[0]
        column=n[1]
    else :
        row=n[1]
        column=n[0]
    table=[]
    for r in range(row):
        comp=[]
        for c in range(column):
            comp.append(tabl[0])
            tabl.pop(0)
        table.append(comp)
    return table

def cube(table):
    number=len(table)
    if number==2:
        return (1,2)
    if number== 9:
        return(3,3)
    if number==6:
        return (2,3)
    for x in range(20):
        if x!=0:
            if number%x == 0 and x > 3:
                return (x,int(number/x))
    return

def print_table (table,cord_1,cord_2): #print table with *
    number_col=" "
    for number in range (len(table[0])):
        number_col =number_col+str(number+1) +'  '
    print(number_col)
    print()
    for x in range(len(table)):
        printin=" "
        
        for i in range(len(table[x])):
            val=0
            if table[cord_1[0]][cord_1[1]]== ' ' or table[cord_2[0]][cord_2[1]]== ' ':
                printin=printin+' '
            else:
                if x+1==cord_1[0] and i+1==cord_1[1]:
                    printin=printin+ str(table[x][i])+' '
                    val=1
                if x+1==cord_2[0] and i+1==cord_2[1]:
                    printin=printin + str(table[x][i])+' '
                    val=1

                if val==0:
                    printin=printin + ('*  ')
        print(printin)
    return()

def pairs(cord_1,cord_2,table): #check winner pairs
    if table[cord_1[0]][cord_1[1]]==table[cord_1[0]][cord_1[1]]:
        return True
    return False 



def dimensions(table,cord):
    x=len(table)
    y=len(table[0])
    return
    
def print_player(score_1 , score_2 , turn): #print the points of the players and whose turn it is
    print(
                "----------------------------------------------------------------------------------\n" \
                 "player 1: "+str(score_1)+'                                                     player 2: '+str(score_2) +"\n"
                 "                                   player "+ str(turn)+ " is playing \n"+
    
                  "---------------------------------------------------------------------------------- \n"  )
    return



print_player(23,56,2)

n_cards= int(input ('enter a number of cards '))
print_player(23,56,2)
table=create_table(n_cards)
print_table(table,(1,1),(2,2))