"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    length = len(result)
    i= 0
    result_separado =[]

    """ separamos el string por letras """
    while(i < length):
        result_separado.append(result[i])
        """ print(result_separado) """
        i += 1

    """ ahora vemos si son o, i , a """    
    """ ['f', 'o', 'o', 'z', 'i', 'm', 'a', 'n'] """
    """   0    1    2    3...                    """
    result_resutante = []
    i = 0
    for x in result_separado:

        if x == 'o' or x == 'i' or x == 'a':
            if x == 'o':
                result_resutante.append('0') 
                
            if x == 'i':
                result_resutante.append('1') 
                
            if x == 'a':
                result_resutante.append('@') 
        else:
            x = x.upper()
            result_resutante.append(x) 

        i += 1
    
    return result_resutante 

print(fn_hack_10())