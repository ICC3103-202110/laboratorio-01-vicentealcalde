import random 

def create_table (n_cards): #creation of the game table, use of copy list to guarantee the pairs
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

def cube(table):  #It gives the shape to the matrix, as it can vary, it was tried to have the most optimal shape (the larger the number of cards, the better it looks
    number=len(table)
    if number==2:
        return (1,2)
    if number== 9:
        return(3,3)
    if number==6:
        return (2,3)
    if number==4:
        return (2,2)
    for x in range(20):
        if x!=0:
            if number%x == 0 and x > 3:
                return (x,int(number/x))
    return

def print_table (table,cord_1,cord_2): #print table with *
    number_col=" "
    for number in range (len(table[0])):
        number_col =number_col+'%2s  '% str(number+1) #print the guide numbers above
    print(number_col)
    print()
    n=65
    for x in range(len(table)):
        printin=str(chr(n)+' ') #print the guide A,B,C,D.......
        for i in range(len(table[x])):
            val=0
            
            if table[x][i]==0:
                printin=printin+'%2s '%' '
            else:
                if x+1==cord_1[0] and i+1==cord_1[1]:
                    printin=printin+'%2s '%str(table[x][i])
                    val=1
                if x+1==cord_2[0] and i+1==cord_2[1]:
                    printin=printin +'%2s '% str(table[x][i])
                    val=1

                if val==0:
                    printin=printin + ('%2s '%'*')
        n+=1
        print(printin)
    return() #game table printing

def pairs(cord_1,cord_2,table): #check winner pairs
    if table [cord_1[0]-1][cord_1[1]-1]!=0:
        if table[cord_1[0]-1][cord_1[1]-1]==table[cord_2[0]-1][cord_2[1]-1]:
            return True
    return False #verification that the two coordinates d are the same number

def discount_table(table,cord):
    x=cord[0]
    y=cord[1]
    table[x-1][y-1]=0
    return table #number discount system on the board, if the pairs match the numbers become zeros

def card():
    print('enter a coordinate (EX: A1)')
    cord=input(' ')
    return cord  #use to ask for the letter

def convert_coordinates(card): # converts the coordinates, for use in matrix
    t=card[0]
    n_t=ord(t)
    t=n_t -64
    return (t,int(card[1])) #converts coordinates of type A1 to a tuple

    
def print_player(score_1 , score_2 , turn): #print the points of the players and whose turn it is
    print(
                "----------------------------------------------------------------------------------\n" \
                 "player 1: "+str(score_1)+'                                                     player 2: '+str(score_2) +"\n"
                 "                                   player "+ str(turn)+ " is playing \n"+
    
                  "---------------------------------------------------------------------------------- \n"  )
    return

def cards(): #set of all card parameters, so it is only mentioned once 
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


def shifts_functional_set(turn,score_1,score_2,table,stop,repit ): #this function takes all the previous functions, so I don't have to write it twice 
    while stop!=1:
        if all_sum(table)==False:
            if repit==0:
                cord_1=(0,0) #coordinates ceted at 0,0 so that it does not interfere with the function
                cord_2=(0,0)
                repit=1
            print_player(score_1 , score_2 , turn)
            print_table(table,cord_1,cord_2)
            if repit==1: #to differentiate from the first letter and the second
                cord_1=cards()
                verifi=verification_po(table,cord_1) #minimum coordinate verification, it is not specified that it has to be better than that 

                if verifi==True:
                    print_player(score_1 , score_2 , turn)
                    print_table(table,cord_1,cord_2)
                    repit=2
            if repit==2:
                cord_2=cards()
                verifi=verification_po(table,cord_2)
                if verifi==True:
                    print_player(score_1 , score_2 , turn) #print scores and who plays
                    print_table(table,cord_1,cord_2) #print game table
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
    return score_1,score_2,table

def all_sum(table):  #check to finish the game, the sum of each row must equal zero 
    for x in table :
        row_suma=sum(x)
        if row_suma>0:
            return False
    return True 

def winner(score_1,score_2): #check the winner
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
                 "                          ＼(^o^)／  WINNER player "+name+" ＼(^o^)／                           \n\n"
                 "                          score player 1: "+str(score_1)+"   score player 2: "+str(score_2)+"\n\n"
                 "                                 winner winner chicken dinner                          \n"
                 "---------------------------------------------------------------------------------- \n"
                 "---------------------------------------------------------------------------------- \n"  )
    else:
        print(
            "---------------------------------------------------------------------\n "
              "                there are no winners \n"
              "---------------------------------------------------------------------")
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
        score_1,score_2,table=shifts_functional_set(turn,score_1,score_2,table,stop_1,repit ) #player 1 plays here until he loses
        turn=2
        if all_sum(table)==False:
            score_1,score_2,table=shifts_functional_set(turn,score_1,score_2,table,stop_1,repit ) # player 2 plays here until he loses 
        else:
            stop=1
    else:
        stop=1
winner(score_1,score_2)  # winner is verified and print message


"""
Many of the variables are only for temporary use, this means that their use is only limited once, because they do not have very explanatory names.
"""
















