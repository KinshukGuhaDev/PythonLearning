file_dir = "BasicExercises/Assets"
filename = "test.txt"
# with open(f"{file_dir}/{filename}", "w") as file:
#     file.write("Hello, World!\n")
#     file.write("This is a test file.\n")
#     file.write("File management in Python is easy!\n")
with open(f"{file_dir}/{filename}", "r") as file:   
    print(file.read())