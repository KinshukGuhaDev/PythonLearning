#Detect double space in a string
string = "This is to inform my name is kinshuk  guha"
isExist = bool(string.count("  "))
print("Is my string has double spaces?", isExist)

#now replace the double string to single string
if(isExist) :
    print(string.replace("  ", " "))

