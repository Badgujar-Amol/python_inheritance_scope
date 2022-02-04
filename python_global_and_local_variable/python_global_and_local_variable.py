# Create Global variable
x = "global"

def foot():
    print("x inside:", x)

foot()
print("x outside:", x)

# Accessing local variable outside the scope
def foot():
    y = "local"

foot()
print(y)


# Create a Local Variable
def foot():
    y = "local"
    print(y)

foot()

# Using Global and Local variables in the same code
x = "global "

def foot():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foot()

# Global variable and Local variable with same name
x = 5

def foot():
    x = 10
    print("local x:", x)

foot()
print("global x:", x)