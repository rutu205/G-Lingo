def translate(phrase):
    transalation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            transalation= transalation+"g"
        else:
            transalation=transalation+ letter
    return(transalation)
        
print(translate(input("Enter the phrase:")))
            