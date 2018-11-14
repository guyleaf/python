def start(inf):
    while inf != '.':
        if(inf[0].isdigit()):
            inf = build_num(inf)
        else:
            inf = build_id(inf)

def build_id(inf):
    i = 0
    while True:
        if(inf[i]==' '):
            inf = identifier(inf)
            break
        elif(inf[i]!=' ' and not(inf[i].isdigit()) and not(inf[i].isalpha()) and inf[i]!= '_'):
            inf = build_invalid(inf, i)
            break
        i += 1
    return inf
        
def build_num(inf):
    i = 0
    while True:
        if(inf[i]==' '):
            inf = number(inf)
            break
        elif(inf[i]!=' ' and not(inf[i].isdigit())):
            inf = build_invalid(inf, i)
            break
        i += 1
    return inf
    
        
def build_invalid(inf, i):
    i += 1
    while True:
        if(inf[i]==' '):
            inf = invalid(inf)
            break
        i += 1
    return inf
        
def number(inf):
    new, inf = inf.split(' ', 1)
    print(new + ' - Number')
    return inf
    
def invalid(inf):
    new, inf = inf.split(' ', 1)
    print(new + ' - Invalid')
    return inf
    
def identifier(inf):
    new, inf = inf.split(' ', 1)
    print(new + ' - Identifier')
    return inf

inf = input()
start(inf)