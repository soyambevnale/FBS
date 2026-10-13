from threading import Thread,Lock
from time import sleep
class bank:
    balance=1000
    l1=Lock()
    def withdraw(self,amount):
        bank.l1.acquire()
        if amount < bank.balance:
            print(f"Bank balance : {bank.balance}   Amount : {amount}")
            old_balance=bank.balance
            sleep(1)
            bank.balance=old_balance-amount
            print("Withdraw")
        else:
            print("Insufficient balance for ",amount)
        bank.l1.release()
            
b1=bank()
t1=Thread(target=b1.withdraw,args=(700,))
t2=Thread(target=b1.withdraw,args=(500,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Reamaining balance = ",bank.balance)
