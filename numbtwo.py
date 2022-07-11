print("Numb two __name__ is set to: {}" .format(__name__))

def function_three():
    print("Function three is executed")

def function_four():
    print("Function four is executed")

if __name__ == "__main__":
    print("Numb two executed when ran directly")
else:
    print("Numb two executed when imported")