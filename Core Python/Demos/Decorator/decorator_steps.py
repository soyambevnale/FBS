# def login():
#     print("Execution start")
#     print("Login time start")
#     print("Logger added")
#     print("Login in is done .")
#     print("Execution stopped")
#     print("Time stopped")
#     print("Logger removed")
        
# login()


# print("+++++++++++++++++++++++++++++++++++")

# def logout():
#     print("Execution start")
#     print("Login time start")
#     print("Logger added")    
#     print("Logout is done .")
#     print("Execution stopped")
#     print("Time stopped")
#     print("Logger removed")
# #print(type(logout))
# logout()

# print("+++++++++++++++++++++++++++++++++++")

# def authentication():
#     print("Execution start")
#     print("Login time start")
#     print("Logger added")    
#     print("authentication is done .")
#     print("Execution stopped")
#     print("Time stopped")
#     print("Logger removed")
# authentication()



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
# def demo(a):
#     print("I am in demo ")
#     def inner_fun(*args):
#         print("Time started")
#         print("Logger added")
#         a(*args)
#         print("Time stopped")
#         print("Logger removed")
#     return inner_fun
# @demo
# def login():
#     print("Login is done")

# @demo
# def log_out():
#     print("Log out is done")
    
# @demo
# def add(a,b):
#     print(f"Addition is : {a+b}")
    
# add(10,20)

# result=demo(login)
# result()