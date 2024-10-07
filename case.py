day = input("Enter the day of the week: ").lower()

match day:
    case "monday":
        print("It's monday already")
    case "tuesday":
        print("It's tuesday")
    case "wednesday":
        print("It's wednesday")
    case "thursday":
        print("Almost there...")
    case "friday":
        print("TGIF!")
    case "saturday" | "sunday":  # Match multiple values with pipe (|)
        print("Weekend vibes!")
    case _:
        print("it's not in my list")        