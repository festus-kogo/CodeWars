# https://www.codewars.com/kata/54dc6f5a224c26032800005c/python

def stock_list(list_of_art, list_of_cat):

    if list_of_art == [] or list_of_cat == []:
        return ""
    
    dict_values = [0 for _ in range(len(list_of_cat))] 
    my_dict = dict(zip(list_of_cat, dict_values))

    for i in list_of_art:

        if i.split(' ')[0][0] in list_of_cat:
            my_dict[i.split(' ')[0][0]] += int(i.split(' ')[1])
    
    l = [f"({k} : {v})" for k, v in my_dict.items()]
    
    return f"{' - '.join(l)}"



L = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
M = ["A", "B", "C", "W"]

print(f"{stock_list(L, M)}") # (A : 20) - (B : 114) - (C : 50) - (W : 0)