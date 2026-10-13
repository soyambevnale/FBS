# 2. Create class television that has members to hold the model number ,screen size
# and price. Take a member function to take input from user, If more than 4 digits
# are entered for model number, if screen size is smaller than 12 inches or greater
# than 70 inches or if the price is negative or greater than 5000 Rs, then throw an
# exception.
# Write a main() that instantiates an object and allows the user to enter and display
# data. If exception is caught, replace all data member values with zero

class television:
    def __init__(self):
        self.model_number=0
        self.screen_size=0
        self.price=0

    def get_model_number(self):
        return self.model_number
    def set_model_number(self,new_model_name):
        self.model_number=new_model_name

    def get_screen_size(self):
        return self.screen_size
    def set_screen_size(self,new_screen_size):
        self.screen_size=new_screen_size

    def get_price(self):
        return self.price
    def set_price(self,new_price):
        self.price=new_price

    def main(self):
        try:
            self.model_number=int(input("Enter model number : "))
            if self.model_number>9999:
                raise Exception ("Enter less than 5 digit model number ")

            self.screen_size=int(input("Enter screen size : "))
            if self.screen_size<12 or self.screen_size>70:
                raise Exception ("Size should be less than 12 inches and greater than 70 inches")       

            self.price=int(input("Enter price : "))
            if self.price<0 or self.price>5000:
                raise Exception ("Price should be between 5000")

            print("--------------------------------------")
            print("Model number : ",self.model_number)
            print("Screen size : ",self.screen_size)
            print("Price : ",self.price)

        except Exception as e:
            print(e)

            self.model_number=0
            self.screen_size=0
            self.price=0

            print("All data members are replaced with zero ")


t=television()
t.main()