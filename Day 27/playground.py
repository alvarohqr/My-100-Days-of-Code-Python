# *args -> tuple
# **kargs -> dict
def add(*args):
    # *args = unlimited/unspecified position arguments
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    print(sum)
    
#add(1,2,3)

def calculate(n, **kwargs):
    print(kwargs)
    # for (key, value) in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add =3, multiply= 5)

class Car:
    def __init__(self, **kargs) -> None:
        # self.make = kargs["make"]
        # self.model = kargs["model"]
        # if the key doesn't exist will return none
        self.make = kargs.get("make")
        self.model = kargs.get("model")

my_car = Car(make = "Nissan")
print(my_car.make)
print(my_car.model)