from time import sleep
from threading import Thread
def fun1():
    for i in range(5):
        print("Virat")
        sleep(5)
        
def fun2():
    for i in range(5):
        print("Rohit")
        sleep(5)
        
t1=Thread(target=fun1)
t2=Thread(target=fun2)
t1.start()            #Start the execution and call run() function
t2.start()
t1.join()              # gives assurity to complete task first and execute later which is written after join
t2.join()
print("I am in main thread ")