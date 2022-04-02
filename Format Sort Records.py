PEOPLE = [('Donald', 'Trump', 7.85),

('Vladimir', 'Putin', 3.626),
('Jinping', 'Xi', 10.603)]

def format_sort_records (people):
    liste = []
    for person in people:
        
        if person[0] in ('Donald', 'Vladimir')  :
            liste.append(' '.join([person[0], person[1], str(round(person[2],2)) ]))
        else :
            liste.append(' '.join([person[1], person[0], str(round(person[2],2)) ]))
    
    return '\n'.join(liste)


print(format_sort_records(PEOPLE))

