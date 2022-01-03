def pig_latin(string):

    if string[0] in 'aeiou':
        return string + 'way'
    else :
        first_letter = string[0] 
        new_string = string[1:] + first_letter + 'ay'
        return new_string

pig_latin('ffenlaut')


