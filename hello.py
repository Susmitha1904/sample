#name = input("what's your name? ").strip().title()

# remove whitespaces from str
#name=name.strip()

#capitalize the first letter
#name=name.capitalize()

#capitalize the letters and also we can use 2 functions and more
#name=name.title().strip()

#split name into first & last name
#firstname,lastname = name.split(" ")
#print(f"Hello, {firstname}")

#other way of printing the str
#print(f"Hello, {name}")

#defining function
#def hello():
    #name = input("name: ")
    #hello(name)
    #print(name)

def hello():
    name = input("first name: ")
    hello()
    print(name)