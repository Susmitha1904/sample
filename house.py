name = input("What's your name? ")
match name:
    case "pinky"| "shiva"| "ajay"| "venu"| "shashi"|"minnu":
        print("samala")
    case "kaveri"| "sindhu":
        print("myana")
    case _:
        print('no idea')
