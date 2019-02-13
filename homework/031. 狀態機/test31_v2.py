def start(inf, i):
    if(inf[i+1].isdigit()):
        build_num(inf, i+1)
    elif(inf[i+1].isalpha()):
        build_id(inf, i+1)

def build_id(inf, i):
    new = []
    while True:
        if(inf[i]!=' ' and not(inf[i].isdigit()) and not(inf[i].isalpha()) and inf[i]!= '_'):
            build_invalid(new, inf, i)
            break
        elif(inf[i]!=' '):
            new.append(inf[i])
        else:
            identifier(new)
            start(inf, i)
            break
        i += 1

def build_num(inf, i):
    new = []
    while True:
        if(inf[i]!=' ' and not(inf[i].isdigit())):
            build_invalid(new, inf, i)
            break
        elif(inf[i]!=' '):
            new.append(inf[i])
        else:
            number(new)
            start(inf, i)
            break
        i += 1
          
def build_invalid(new, inf, i):
    while True:
        if(inf[i]!=' '):
            new.append(inf[i])
        else:
            invalid(new)
            start(inf, i)
            break
        i += 1
  
def number(new):
    print(''.join(str(e) for e in new) + ' - Number')
    
def invalid(new):
    print(''.join(str(e) for e in new) + ' - Invalid')
    
def identifier(new):
    print(''.join(str(e) for e in new) + ' - Identifier')

inf = input()
i = -1
start(inf, i)