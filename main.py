def my_name():
    print("My name is Abdullah")

my_name()        

def my_meal(Food, Drink):
    print(f"I like to eat {Food} and while drinking {Drink}")

my_meal('pizza', 'cola')

def cube(number):
    return number**3

print(cube(9))


def by_three(number):
    if number % 3 == 0:
        result = cube(number)  
        print(f"The answer is {result}")  
        return result  
        
    else: 
        return print("false")


by_three(3)