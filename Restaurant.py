menu = {"fish": 5, "fries": 3, "steak": 14, "burger": 9}


def restaurant():
    price = 0

    while True:

        user_input = input("Choose dish").strip()

        if not user_input: 
            print(f"your total is {price}")
            break
        elif user_input in menu:
            price += menu.get(user_input)
            print(price)
        elif user_input not in menu and user_input != "":
            print(f"We dont serve {user_input} ")          

restaurant()
