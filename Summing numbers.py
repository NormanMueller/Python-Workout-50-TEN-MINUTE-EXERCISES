def my_sum(*args) :
 
    sum_overall = 0
    skipped_argument = []
    
    def check_if_is_list (argument):
        return isinstance(argument, list)

    def add_single_entry(argument , sum_overall ,skipped_argument):
        
        try: 
            sum_overall += argument
        except:
            skipped_argument.append(argument)

        return sum_overall ,skipped_argument 

    
    def add_list_entry(argument , sum_overall ,skipped_argument) :
        
        for list_entry in argument : 
             sum_overall ,skipped_argument = add_single_entry(list_entry,sum_overall ,skipped_argument)

        return sum_overall ,skipped_argument
        

    for argument in args :
        
        if  check_if_is_list (argument) == True :
            sum_overall, skipped_argument = add_list_entry(argument, sum_overall, skipped_argument)
        else :    
            sum_overall, skipped_argument = add_single_entry(argument, sum_overall, skipped_argument) 
    
    return f'Your sum is: {sum_overall} we cant eval: {skipped_argument}'

input_num = [1,2,3,4]
print(my_sum(input_num, 6, 8, [3,2],'w', ['a'] , [[2]]))

