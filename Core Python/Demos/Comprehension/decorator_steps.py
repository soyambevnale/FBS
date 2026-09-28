# dyansetu example

def decorator(a):
    print("I am in demo ")
    def wrapper(*args):
        print("Time started")
        print("Logger added")
        a(*args)
        print("Time stopped")
        print("Logger removed")
    return wrapper
@decorator
def login():
    print("Login is done")

@decorator
def log_out():
    print("Log out is done")
    
@decorator
def add(a,b):
    print(f"Addition is : {a+b}")
    
add(10,20)

# result=demo(login)
# result()

# class example
def demo(a):
    print("I am in demo ")
    def inner_fun(*args):
        print("Time started")
        print("Logger added")
        a(*args)
        print("Time stopped")
        print("Logger removed")
    return inner_fun
@demo
def login():
    print("Login is done")

@demo
def log_out():
    print("Log out is done")
    
@demo
def add(a,b):
    print(f"Addition is : {a+b}")
    
add(10,20)

# result=demo(login)
# result()