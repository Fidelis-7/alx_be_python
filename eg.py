def has_id():
    return False

age = int(input("Enter your age: "))

match age:
    case 18 | 19: 
        if age >= 18 and has_id():
            print("You are eligible to vote")
        else:
            print("you dont have a voter's card")
            
    case _:
        print("you are not eligible to vote")
    