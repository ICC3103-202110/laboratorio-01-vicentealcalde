import random 




def table ():
    grand=[]
    while  len(grand)<4:
        row=[random.randint(0,21) for _ in range(5)]
        grand.append(row)
    return grand 

map_table=table()
print(map_table)