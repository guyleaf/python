def main():
    correct = []
    guess = []
    correct = list(map(int, input().split()))
    while True:
        guess.append(list(map(int, input().split())))
        if(len(guess[len(guess)-1])==1):
            del guess[len(guess)-1]
            break
    for i in guess:
        A, B = compare(i, correct)
        print("%dA%dB" %(A, B))
def compare(guess, correct):
    A = 0
    B = 0
    copy_guess = []
    copy_correct = []
    copy_guess.extend(guess)
    copy_correct.extend(correct)
    for i, num in enumerate(guess):
        if(findposition(num, correct, i)):
            copy_correct.pop(i-A)
            copy_guess.pop(i-A)
            A +=1
    for num in copy_guess:
        if(findnum(num, copy_correct)):
            B +=1
    B -= check(copy_correct, copy_guess)
    return A, B
def findposition(num, correct, j):
    if(correct[j]==num):
        return 1
    return 0
def findnum(num, correct):
    for i in correct:
        if(i==num):
            return 1
    return 0
def check(copy_correct, copy_guess):
    B = 0
    for i in list(set(copy_guess)):
        if((copy_guess.count(i)>copy_correct.count(i)) and (copy_correct.count(i)!=0)):
            B +=1
    return B
main()