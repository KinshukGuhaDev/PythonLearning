#Fill the name and date with data
letter = '''
    Dear <|Name|>,
    You are selected!
    <|Date|>
'''
letter = letter.replace("<|Name|>", "Kinshuk Guha")
letter = letter.replace("<|Date|>", "08, September 2026")
print(letter)