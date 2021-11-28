from random import randint

def guessing_game ():
     
    guessing_number = int(randint(0, 10))


    def get_user_input():
        
        user_input = int(input('Whats your number?'))
        return user_input

    def evaluate_user_input(user_input, guessing_number) : 
        
        if user_input > guessing_number: 
            return 'your number os to high'
        
        elif user_input < guessing_number: 
            return 'your number os to low'

        elif user_input == guessing_number: 
            return (f'you have the rigth number , the number is {user_input}') 



    while True :
        
        user_input = get_user_input()
        eval = evaluate_user_input(user_input, guessing_number)
        print(eval)
        if eval == 'you have the rigth number , the number is {user_input}' :
            break     
guessing_game ()

