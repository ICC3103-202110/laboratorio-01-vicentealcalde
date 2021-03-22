
import random 
def create_table (n_cards):
    cards_1=[random.randint(1,n_cards) for _ in range(n_cards)]
    cards_2=cards_1[:]
    tabl= cards_1 + cards_2 #tabl = table 
    random.shuffle(tabl) #first disorder
    random.shuffle(tabl) #second disorder 
    n=cube(tabl)
    print(n)
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
            print(comp)
            print('hola')
        print('hola 2')
        table.append(comp)
    return table

    
def cube(table):
    number=len(table)
    print(number)
    if number==2:
        return (1,2)
    if number== 9:
        return(3,3)
    if number==6:
        return (2,3)
    for x in range(20):
        if x!=0:
            if number%x == 0 and x > 3:
                print(x)
                return (x,int(number/x))
    return 
n_cards= int(input ('enter a number of cards'))
table=create_table(n_cards)

print(table)
print(len(table))
