value = input("Enter a value: ")
match value:
    case int():
        print(f"{value} is an integer")
    case str():
        print(f"{value} is a string")
    case _:
        print(f"you have entered a different datatype")