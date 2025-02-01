# Unlimited positional arguments
def add(*args):
    sum_of_args = 0
    for n in args:
        sum_of_args += n
    return sum_of_args

# sum_of_nums = add(1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(sum_of_nums)

# Unlimited keyword arguments
def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

# class Car:
#     def __init__(self, **kwargs):
#         self.make = kwargs["make"]
#         self.model = kwargs["model"]
#
# my_car = Car(make="Nissan", model="GT-R")
# print(my_car.model)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs.get("model")

my_car = Car(make="Nissan")
print(my_car.model)