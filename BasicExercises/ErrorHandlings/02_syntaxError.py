# Try to see built-in error message

# The faulty line below is placed inside a string and run with exec(), so that
# the SyntaxError can be caught and the notebook can keep running.
import traceback

try:
    exec('print("Hello World!!)')
except SyntaxError as error:
    print('error:', error)