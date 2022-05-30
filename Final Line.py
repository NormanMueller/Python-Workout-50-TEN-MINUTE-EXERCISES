import csv

def get_final_line(file_directory):
    with open(file_directory) as file:
        reader=csv.reader(file)
        rows=[r for r in reader]         
        print(rows[-1])

get_final_line('data/boston_house_prices.csv')