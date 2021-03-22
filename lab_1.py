import random 




def create_table (n_cards):
    cards_1=[random.randint(1,n_cards) for _ in range(n_cards)]
    cards_2=cards_1[:]
    table= cards_1 + cards_2
    random.shuffle(table) #first disorder
    random.shuffle(table) #second disorder 
    return table 

def print_table (table):
    return()
table=create_table(20)
print(table)
print(len(table))


