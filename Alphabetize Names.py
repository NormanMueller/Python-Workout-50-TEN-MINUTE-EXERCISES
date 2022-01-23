
from operator import itemgetter

people = [
{'first':'Reuven', 
'last':'Lerner',
'email':'reuven@lerner.co.il'
},
{'first':'Donald',
 'last':'Trump',
'email':'president@whitehouse.gov'
},
{'first':'Vladimir', 
'last':'Putin',
'email':'president@kremvax.ru'
}
]

def Alphabetizing_name(phone_book):
    sorted_list = []
    final_list =[]
    for entry in range(len(phone_book)):
        sorted_list.append(itemgetter(entry)(phone_book).get('first'))
    for entry in sorted_list:
        for person in range(len(phone_book)):
            if itemgetter(person)(people).get('first') == entry:
                final_list.append(itemgetter(person)(people))
            else:
                pass
    return final_list

def alphabetize_names(list_of_dicts):
    return sorted(list_of_dicts,
    key= lambda a : a.get('last'))

alphabetize_names(people)