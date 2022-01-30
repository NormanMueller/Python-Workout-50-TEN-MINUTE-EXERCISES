numbers = [1,23,2,3,4,4,2,2,5,32,1,2,4,3]    

def unique_numbers(numbers):    
    unique_numbers = set(numbers)
    return len(unique_numbers)

print(unique_numbers(numbers))