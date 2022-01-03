def pig_latin_sentence (sentence):
    
    def pig_latin(string):

        if string[0] in 'aeiou':
            return string + 'way'
        else :
            first_letter = string[0] 
            new_string = string[1:] + first_letter + 'ay'
            return new_string

    word_list = sentence.split()
    pig_latin_sentence = []
    
    for word in word_list:
        pig_latin_sentence.append(pig_latin(word))
    
    return  ' '.join(pig_latin_sentence)

pig_latin_sentence('this is test translation')

