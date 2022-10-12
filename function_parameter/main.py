
#simple function
def greet():
    print("Hello Angela")
    print("How do you do")
    print("Isn't not the weather nice today?")
greet()

#function with input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do{name}")
greet_with_name("Angela")

#function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name,}")
    print(f"How is like in {location}")
greet_with("Angela", "local")

#keyword arguments
def greet_with(name="Angela", location="local"):
    print(f"Hello {name,}")
    print(f"How is like in {location}")
greet_with("Angela", "local")
