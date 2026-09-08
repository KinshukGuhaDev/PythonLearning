# STRING FUNCTIONS 
a = "Hello!! My name is kinshuk guha"

print(len(a)) #PRINTS (31)
print(a.endswith("guha")) #THIS CHECKS WHETHER THE VARIABLE STRING ENDS WITH THE SPECIFIC STRING RETURNS TRUE/FALSE. THIS IS CASSE SENSITIVE.
print(a.startswith("HELLO!!")) #RETURNS FALSE BECAUSE ITS CASE SENSITIVE
print(a.strip()) #This works as a trim method to remove white spaces from first and last index
print(a.replace("Hello", "Bonjour")) #This method is also case sensitive it finds and replaces the required value in a variable.
print(a.split()) #This first breaks words by blank spaces and then converts it into a list
print(a.count("He")) # This finds that in which places the searched string was found and gives a count of all occurances in the string