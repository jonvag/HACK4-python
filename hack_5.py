"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
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
            result_resutante.append(x) 

        i += 1
    result = ''
    for x in result_resutante:

        result = result + x
    return result  

print(fn_hack_5())