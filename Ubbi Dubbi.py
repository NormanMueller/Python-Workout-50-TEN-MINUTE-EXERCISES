def ubbi_dubbi(strings):
    
    string_result = []
    
    for letter in strings :
        
        if  letter in ['a', 'e', 'o', 'u'] :
            new_letter = 'ub'+ letter 
            string_result.append(new_letter)
        else :
            string_result.append(letter)

    return ''.join(string_result)


ubbi_dubbi('elephant')
