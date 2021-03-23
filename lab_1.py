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
            
            if table[x][i]==0:
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
    if table [cord_1[0]-1][cord_1[1]-1]!=0:
        if table[cord_1[0]-1][cord_1[1]-1]==table[cord_2[0]-1][cord_2[1]-1]:
            return True
    return False 

def discount_table(table,cord):
    x=cord[0]
    y=cord[1]
    table[x-1][y-1]=0
    return table 

def card():
    print('enter a coordinate (EX: A1)')
    cord=input(' ')
    return cord  #se tienes que aplicar los filtros aun 

def convert_coordinates(card):
    t=card[0]
    n_t=ord(t)
    t=n_t -64
    return (t,int(card[1])) #convierte las coordenadas de tipo A1 a una tupla 

    
def print_player(score_1 , score_2 , turn): #print the points of the players and whose turn it is
    print(
                "----------------------------------------------------------------------------------\n" \
                 "player 1: "+str(score_1)+'                                                     player 2: '+str(score_2) +"\n"
                 "                                   player "+ str(turn)+ " is playing \n"+
    
                  "---------------------------------------------------------------------------------- \n"  )
    return

def cards(): #conjunto de todos los parametros de carta 
    q=card()
    cord=convert_coordinates(q)
    return cord 

def verification_po(table,cord):  #verification of the coordinates of use, so that it does not leave the matrix
    if cord[0]<1 or cord[1]<1:
        return False 
    else:
        if cord[0]<(len(table)+1) or cord[1]<(len(table[0])+1):
            return True 
        else:
            return False 
    return False 


def shifts_functional_set(turn,score_1,score_2,table,stop,repit ): #esta funciuon toma todas las funciones anterioires, asi no tengo que escribirlo 2 veces 
    while stop!=1:
        if all_sum(table)==False:
            if repit==0:
                cord_1=(0,0)
                cord_2=(0,0)
                repit=1
            print_player(score_1 , score_2 , turn)
            print_table(table,cord_1,cord_2)
            if repit==1: #para diferenciar de la primera carta y la segunda 
                cord_1=cards()
                verifi=verification_po(table,cord_1)

                if verifi==True:
                    print_player(score_1 , score_2 , turn)
                    print_table(table,cord_1,cord_2)
                    repit=2
            if repit==2:
                cord_2=cards()
                verifi=verification_po(table,cord_2)
                if verifi==True:
                    print_player(score_1 , score_2 , turn)
                    print_table(table,cord_1,cord_2)
                    if pairs(cord_1,cord_2,table)==True:
                        table=discount_table(table,cord_1)
                        table=discount_table(table,cord_2)
                        if turn==1:
                           score_1+=1
                        else:
                            score_2+=1
                        if all_sum(table)==True:
                            return score_1,score_2,table
                    else:
                        stop=1
                        return score_1,score_2,table
                    repit=0
        else:
                stop=1
                return score_1,score_2,table
                print('hola como estas')
    return score_1,score_2,table

def all_sum(table):  #comprobar para acabar el juego 
    for x in table :
        row_suma=sum(x)
        if row_suma>0:
            return False
    return True 

def winner(score_1,score_2):
    if score_1>score_2:
        name='1'
    elif score_2> score_1:
        name='2'
    else:
        name='0'
    if name!='0':
       print(
                "----------------------------------------------------------------------------------\n" 
                "----------------------------------------------------------------------------------\n"
                 "                          ＼(^o^)／  WINNER player "+name+" ＼(^o^)／                           \n"
                 "                                 winner winner chicken dinner                          "
                 "---------------------------------------------------------------------------------- \n"
                 "---------------------------------------------------------------------------------- \n"  )
    else:
        print("there are no winners")
    return

    
stop=0
score_1=0
score_2=0
n_cards= int(input ('enter a number of cards or press 0 to exit '))
if n_cards==0:
     stop=1
repit=0
table=create_table(n_cards)
while stop!=1:
    if all_sum(table)==False:
        repit=0
        turn=1
        stop_1=0
        score_1,score_2,table=shifts_functional_set(turn,score_1,score_2,table,stop_1,repit )
        turn=2
        if all_sum(table)==False:
            score_1,score_2,table=shifts_functional_set(turn,score_1,score_2,table,stop_1,repit )
        else:
            stop=1
    else:
        stop=1
winner(score_1,score_2)  



















