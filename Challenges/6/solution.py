
# define the rule constraints
consecutive_consonants =[['ck', 'c'], ['ss', 's'], ['ff', 'f'], ['tt', 't'], ['nn', 'n']]
vowels = ['a', 'e','h', 'i', 'o', 'u', 'w' , 'y']
consonant_to_digit = {
    1: ['b', 'f' ,'p', 'v'],
    2: ['c','g', 'j', 'k', 'q', 's', 'x', 'z'],
    3: ['d' ,'t'],
    4: ['l'],
    5: ['m' , 'n'],
    6: ['r'],
}

# main 
def soundex(name: str):
    # add first letter to mapped result and remove from name param
    soundexMap = name[0].title() 
    name = name.replace(name[0], '')
    
    # rule 1 remove consec const
    noConsecutiveConstonants = removeConsecutiveConstonants(name)
    
    # remove vowels
    noConsConsOrVowels = removeVolwels(noConsecutiveConstonants)
    
    # convert to numbers
    no_con_cons_no_vowels_digitised = replaceWithDigits(noConsConsOrVowels)
    
    # compound with 0s
    soundexMap += addZeros(no_con_cons_no_vowels_digitised);
    
    return soundexMap


def removeConsecutiveConstonants(name: str):
    for con_cons in consecutive_consonants:
        name = name.replace(con_cons[0], con_cons[1])
    return name

def removeVolwels(name: str):
    for vowel in vowels:
        name = name.replace(vowel, '')
    return name

def replaceWithDigits(name: str):
    for i in range(6):
        letters = consonant_to_digit.get(i+1)
        for char in letters:
            if (name.find(str(i+1)) < 0):
                name = name.replace(char, str(i+1))
            else:
                name = name.replace(char, '')
                
    return(name)  

def addZeros(name: str):
    three = False
    while three != True:
        if (len(name) != 3):
            name += '0'
        else:
            three = True    
    return name

print(soundex('matthew'))