# def demo():
#     print("I am in demo ")
    
# # print(type(demo))
# # a=10
# # print(type(a))
# x=demo
# # demo()
# x()


# def fun(a):
#     a()
# def demo():
#     print("I am in demo .")
# x=demo
# fun(x)

def outer():
    print("I am in outer .")
    def inner():
        print("I am from inner function")
    return inner
x=outer()
x()

def outer():
    a="Virat"
    def inner():
        print(a)
    return inner
x=outer()
x()
    