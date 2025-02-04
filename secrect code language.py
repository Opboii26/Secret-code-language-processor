# if word has atleast 3 letters the take the first letter and join it to the end add three random characters at the first and the last
# if the word has letter more than 3 characters then simply reverse it

import random

ask = str(input("Do you want to code or decode the string? (code/decode): "))

def rand():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))

# try these!
# ccgashneelytbi si gyjhetfxj decestbamp bwjvperprcc
# wdbamroodijp si bfthettwg lmuiggestbdyq mzroobnrfm ni namhetqxu cpporld!wzin
def code(sg):
    word = sg.split()
    tempo = []
    Line = ""

    for i in word:
        if len(i) >= 3:
            tempo.append(f"{rand()}{i[1:len(i)]}{i[0]}{rand()}")
        elif len(i) < 3:
            tempo.append(i[::-1])
    Line = " ".join(tempo)
    print(Line)

def decode(gs):
    temp = gs.split()
    DecodedString = ""
    nesWord = []
    for i in temp:
        try:
            nesWord.append(f"{i[-4]}{i[3:-4]}")
        except IndexError:
            nesWord.append(i[::-1])
    DecodedString = " ".join(nesWord)
    print(DecodedString)

if ask == "code":
    query = input("Plz tell the string you want to code!: ")
    code(query)

elif ask == "decode":
    decodingQuery = input("Plz tell the string you want to decode!: ")
    decode(decodingQuery)
    
else:
    print("Invalid Input!\nIf you want to code the string say code and if you want to decode then say decode!")