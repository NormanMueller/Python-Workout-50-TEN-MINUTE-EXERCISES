def run_timing(): 
    
    counter = 0
    time_for_run = 0 
    
    def calc_mean(counter , time_for_run):
        return time_for_run / counter
    
    while True :
        
        user_input = input('Enter 10 km run time: ')

        if user_input == '' :
            print(calc_mean(counter, time_for_run))
            break

        try :
            time_for_run  += int(user_input)
            counter +=1 
        except :
            pass

run_timing()