# Print string as error message

# The try/except below catches the error and prints its message, so that the
# notebook can keep running. (Error handling is covered later in this course --
# for now, just run the cell and read the error message.)
import traceback

# try:
#     frint("Hello, world!")
# except NameError as error:
#     print("Caught an error:", error)


# try:
#     print("This will be printed")
#     frint("This will cause an error")
#     print("This will NOT be printed")
# except NameError:
#     traceback.print_exc()

print(str("123-456-7890"))