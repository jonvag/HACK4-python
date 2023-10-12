"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    result2 = []
    for x in result:
        result2.append(x)
        result2.append('@')

    return result2  

print(fn_hack_9())