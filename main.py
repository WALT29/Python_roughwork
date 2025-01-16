#   TRY AND EXCEPT STATEMENT
"""
- try/except statements allows us to intercept exceptions

- try - lets you test a block of code for errors
- except - lets you handle the error
- else  - lets you execute the block of code when there is no error
- finally - lets you execute the block of code regardless of the error or not





    EG:
        def divide(num1,num2):
            try:
                division=num1/num2
                print(division)
            except:
                print("An error occurred")

            divide(1,0)
        
        - This results to an error whenever num2 is 0 or non-numerical value

"""


def divide(num1,num2):
    try:
        division=num1/num2
        print(division)
    except:
        print("An error occurred")
        
divide(1,0)

# Adding execeptions 
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else")

"""

Exmaples

"""