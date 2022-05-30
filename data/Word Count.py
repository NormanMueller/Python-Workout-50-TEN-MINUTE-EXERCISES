def word_count(file_directory):
    with open(file_directory) as file:
        words = []
        rows = 0
        zeichen = 0
        
        for r in  file:      
            words += r.rstrip().split(' ')
            rows += 1
            zeichen += len(r)
        
        return f' Anz Wörter: {len(words)} \
                  Anz Wörter unique: {len(set(words))} \
                  Rows : {rows} \
                  Zeichen : {zeichen}'

word_count('data/wcfile.txt')