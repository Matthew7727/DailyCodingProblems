ns = [6]

def look_and_say(n):
    x = 1;
    nthTerm = '0'
    print('START OF X LOOP')
    while x <= n:
        currentNthTerm = nthTerm
        nthTerm = ''
        currentDigit = currentNthTerm[0]
        count = 1
        i = 1

        while i <= len(currentNthTerm):
            if x == 1:
                nthTerm = '1'
            elif i == len(currentNthTerm):
                if count != 0:
                    nthTerm = nthTerm + str(count) + currentDigit
                else:
                    nthTerm = nthTerm + currentDigit
            else:
                if currentDigit == currentNthTerm[i]:
                    count += 1
                else:
                    nthTerm = nthTerm + str(count) + currentDigit
                    currentDigit = currentNthTerm[i]
                    count = 1
            i += 1
        
        print(x, nthTerm)
        x += 1
        

for n in ns:
    look_and_say(n)     
    



        
        
