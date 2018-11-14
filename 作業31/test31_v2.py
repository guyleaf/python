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
            new, inf = inf.split(' ', 1)
            identifier(new)
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
            new, inf = inf.split(' ', 1)
            number(new)
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
            new, inf = inf.split(' ', 1)
            invalid(new)
            break
        i += 1
    return inf
        
def number(new):
    print(new + ' - Number')
    
def invalid(new):
    print(new + ' - Invalid')
    
def identifier(new):
    print(new + ' - Identifier')

inf = input()
start(inf)