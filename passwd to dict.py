import csv

def passwd_to_dict(file_directory):
    with open(file_directory) as file:
        dicti = {}
        for r in  file:       
            name = r.split(':')[0]
            id = r.split(':')[2]
            dicti[name] = id
        
        print(dicti)

passwd_to_dict('data/password.txt')