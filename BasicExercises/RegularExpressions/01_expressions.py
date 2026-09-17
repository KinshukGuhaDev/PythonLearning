import re 

a = "Hello! this is kinshuk_guha iam 24 yo person i love dogs such as husky as an example"

# print(re.findall(r'\d', a)) # This will print list ['2', '4'] (digits)
# print(re.findall(r'\D', a)) # This will print list of all non-digit characters non digts

# print(re.findall(r"\w+!", a)) # This will print list of all alphanumeric characters and underscore letter, digit or underscores
# print(re.findall(r"\W", a)) # This will print list of all non-alphanumeric not a letter digit or underscore

# print(re.findall(r"\s", a)) # This will print list of all whitespace characters
# print(re.findall(r"\S", a)) # This will print list of all non-whitespace characters

# print(re.findall(r"\b husky\b", a)) # This will print list of all word boundaries
# print(re.findall(r"\B husky\B", a)) # This will print list of all word boundaries

# ------------------------------------------------------------------

text = "My email is user_12@gmail.com and my PIN is 4567."
pattern = r"\w+@\w+\.\w+\s\D+\d+"
result = re.findall(pattern, text)
# print(result)

# ------------------------------------------------------------------

pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)
if match:
    print("Phone number found:", match.group())
else:
    print("No match")

# ------------------------------------------------------------------

s2 = "The BodyGuard is the best album of 'Whitney Houston'."
result = re.findall("st", s2)
# print(result)  # This will print list of all occurrences of the pattern "st" in the string s2

split_array = re.split(r"\s", s2)
# The split_array contains all the substrings, split by whitespace characters
# print(split_array)

pattern = r"Whitney Houston"

# Define the replacement string
replacement = "legend"
# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE) # re.IGNORECASE makes the search case-insensitive, so it matches "Whitney Houston" in any letter case
# The new_string contains the original string with the pattern replaced by the replacement string
# print(new_string) 

# ------------------------------------------------------------------

s3 = "House number- 132"
# Write your code below and press Shift+Enter to execute
exp = r"\d"
value = re.search(exp, s3)

if value:
    print("found")
else:
    print("not found")

# ------------------------------------------------------------------

str2= "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"

# Write your code below and press Shift+Enter to execute
exp = r"woo"
print(re.findall(exp,str2))

