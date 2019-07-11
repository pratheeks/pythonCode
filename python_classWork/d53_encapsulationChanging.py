class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()


Computer.__maxprice=10
print(Computer.__maxprice)
c.sell()
print(c.__maxprice)



c._Computer__maxprice=45
c.sell()



d=Computer()
d.sell()
