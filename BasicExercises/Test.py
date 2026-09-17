genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco")  
# print(genres_tuple[-1].index('s'))

C_tuple = (-5, 1, -3)
# print(sorted(C_tuple)) #this will print the index of the searched element

my_list = [1, 2, 3, 4, 5] 
my_list.insert(2, 6) 
# print(my_list)


soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
# print(soundtrack_dic.keys())


inventory = {}

pro1_name = "Mobile phone"
pro2_qty = 5
pro2_price = 20000
pro2_release_year = 2020


inventory["pro1"] = {
    "name": pro1_name,
    "quantity": pro2_qty,
    "price": pro2_price,
    "release_year": pro2_release_year
}

pro2_Name= "Laptop"
pro2_Quantity= 10
pro2_price = 50000
pro2_Release_Year= 2023

inventory["pro2"] = {
    "name": pro2_Name,
    "quantity": pro2_Quantity,
    "price": pro2_price,
    "release_year": pro2_Release_Year
}

# print(inventory)

inventory["pro1"]["release_year"] = 1999
# print(inventory)


# print('release_year' in inventory["pro1"])
# print('release_year' in inventory["pro2"])

# del(inventory["pro1"]["release_year"] )
# del(inventory["pro2"]["release_year"])

# print(inventory)



a = {1, 2, 3, 4, 4, 5, 5}
b = {1, 2, 3, 4, 4, 5, 5}

# print(a.union(b))

data = [1,2,3,4,5,6,70]

# for i in range(-5,5):
#     print(i)


# Write your code below and press Shift+Enter to execute
Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']

# for Genre in Genres:
#     print(Genre)

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
rating = PlayListRatings[0] 
i = 0
while i <= len(PlayListRatings) and (PlayListRatings[i]>=6):
    PlayListRatings[i]
    i+=1

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i=0
while i <=len(squares) and squares[i] == 'orange':
    new_squares.append(squares[i])
    i+=1
# print(new_squares)


for i in range(1, 16):
    if i % 3 == 0:
        continue  # skip multiples of 3
    if i > 12:
        break     # stop if number > 12
    # print(i)

# Write your code below and press Shift+Enter to execute
def custom(a, b):
    return a/b

# print(custom(10,5))

def con(a, b):
    return(a + b)

# print(con(['kinshuk','guha'], [24,2002]))
# print(con(('kinshuk','guha'), (24,2002)))



# Write your code below and press Shift+Enter to execute
def findWord(string,searchString):
    searchString = searchString.split()
    for i in searchString:
        if i == string:
            print(len(string))
            
s_string = "little"
string = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"
# findWord(s_string,string)

L=[1,3,2]

# print(sorted(L)) 

try:
    1/0
except Exception as e:
    pass
    # print(type(e).__name__, "-", e)



def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Division by zero is not allowed.")

a = int(input("Enter the numerator: "))
b = int(input("Enter the denominator: "))
# print(divide(a, b))



#Type your code here
#Type your code here







