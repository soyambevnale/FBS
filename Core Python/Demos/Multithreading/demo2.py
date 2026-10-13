from time import sleep
from threading import Thread

class demo1(Thread):
    def run(self):
        for i in range(5):
            print("Pizza")
            sleep(1)

class demo2(Thread):
    def run(self):
        for i in range(5):
            print("Burger")
            sleep(1)

d1=demo1()
d2=demo2()
# d1.run()
# d2.run()
d1.start()
d2.start()
# d1.join()
# d2.join()
print("I am in main thread")