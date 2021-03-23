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
        number_col =number_col+' %2s  '% str(number+1) #IMprime los mu,erps de arriba 
    print(number_col)
    print()
    n=65
    for x in range(len(table)):
        printin=str(chr(n)+' ')
        for i in range(len(table[x])):
            val=0
            
            if table[cord_1[0]-1][cord_1[1]-1]== ' ' or table[cord_2[0]-1][cord_2[1]-1]== ' ':
                printin=printin+'  '
            else:
                if x+1==cord_1[0] and i+1==cord_1[1]:
                    printin=printin+'%2s '%str(table[x][i])
                    val=1
                if x+1==cord_2[0] and i+1==cord_2[1]:
                    printin=printin +'%2s '% str(table[x][i])
                    val=1

                if val==0:
                    printin=printin + (' %2s '%'*')
        n+=1
        print(printin)
    return()

def pairs(cord_1,cord_2,table): #check winner pairs
    if table[cord_1[0]-1][cord_1[1]-1]==table[cord_2[0]-1][cord_2[1]-1]:
        return True
    return False 

def discount_table(table,cord):
    x=cord[0]
    y=cord[1]
    print(y)
    table[x-1][y-1]='  '
    return table 

def card():
    print('enter a coordinate ')
    cord=input(' ')
    return cord  #se tienes que aplicar los filtros aun 

def convert_coordinates(card):
    t=card[0]
    n_t=ord(t)
    t=n_t -64
    return (t,int(card[1]))

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


stop=0
score_1=0
score_2=0
repit=0
n_cards= int(input ('enter a number of cards ot press 0 to exit '))
if n_cards==0:
     stop=1
repit=0
table=create_table(n_cards)
turn=1
while stop!=1:

    

    if repit==0:
        cord_1=(0,0)
        cord_2=(0,0)
        if turn==1:
         turn=2
        if turn==2:
           turn=1
    repit+=1
      
    
    print_player(score_1 , score_2 , turn)
    print_table(table,cord_1,cord_2)
    q_card=card()
    if repit==1:
        cord_1=convert_coordinates(q_card)
    if repit==2:
        cord_2=convert_coordinates(q_card)
        print_table(table,cord_1,cord_2)
        if pairs(cord_1,cord_2,table)==True:
            table=discount_table(table,cord_1)
            table=discount_table(table,cord_2)
            if turn==1:
                score_1+=1
            if turn==2:
                score_2+=1
        else:
            repit=0
        cord_1=(0,0)
        cord_2=(0,0)


    

score_1=0
score_2=0
n_cards= int(input ('enter a number of cards '))
print_player(23,56,2)
table=create_table(n_cards)
print_table(table,(1,1),(2,2))