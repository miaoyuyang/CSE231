
VOWELS = 'aeiou'

while True:
    word = input("Enter a word ('quit' to quit): ")
       
    if word.lower() == "quit":
         break
       
    elif word [0] in VOWELS:
        print (word.lower()+'way')
        
    else:
        for i,ch in enumerate(word):
            if ch in VOWELS:
                break
                   
        print (word.lower()[i:] + word.lower()[0:i] + "ay")


