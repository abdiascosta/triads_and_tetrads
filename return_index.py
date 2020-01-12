#This function should return the element index specified

def return_index(list,element):
    index=0
    for i in list:
        if i!=element:
            index+=1
        if i==element:
            return index

