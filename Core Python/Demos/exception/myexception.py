class Myexception(Exception):
    def __init__(self, *args):
        self.age=args
        print("I am in con of myexception class")
    def __str__(self):
        return "Bhai tu age wrong dala hai"
        