def first_last (input_obj):
    first_element = input_obj[:1]
    last_element = input_obj[-1:]
    return f'fist: {first_element + last_element}'

#slices are better, keeping original type of the object 
tuple = (1,34,'asd', 4)
list = [1,34,'asd']
string  = 'asda8345'
for obj_type in [tuple, list, string]:
    print (first_last(obj_type))