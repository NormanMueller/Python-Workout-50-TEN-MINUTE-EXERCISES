def my_sum(*args) :

    ret_val = 0
    skipped = []

    def list_add(argument , ret_val ,skipped) :
        
        for list_entry in argument : 
            try:
                ret_val += list_entry
            except:
                skipped.append(list_entry) 
        return ret_val ,skipped


    def int_add(argument , ret_val ,skipped):
        
        try: 
            ret_val += argument
        except:
            skipped.append(argument)
        return ret_val ,skipped 
    
    for argument in args :
        
        if isinstance(argument, list) == True :
            ret_val, skipped = list_add(argument, ret_val, skipped) 
        else :    
            ret_val, skipped =int_add(argument, ret_val, skipped)
    
    return f'Your sum is: {ret_val} we cant eval: {skipped}'

input_num = [1,2,3,4]
print(my_sum(input_num, 6, 8, [3,2],'w', ['a'] , [[2]]))
