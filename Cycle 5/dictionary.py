import csv

field_names = ['No','Company','Car Model']

cars = [
{'No': 1, 'Company': 'Ferrari', 'Car Model': '488 GTB'},
{'No': 2, 'Company': 'Porsche', 'Car Model': '918 Spyder'},
{'No': 3, 'Company': 'Bugatti', 'Car Model': 'La Voiture Noire'},
{'No': 4, 'Company': 'Rolls Royce', 'Car Model': 'Phantom'},
{'No': 5, 'Company': 'BMW', 'Car Model': 'BMW X7'},
]

with open('Cars.csv','w') as dictionary:
    writer = csv.DictWriter(dictionary,fieldnames = field_names)
    writer.writeheader()
    writer.writerows(cars)

dictionary.close()

with open('Cars.csv','r') as File:
    next(File)
    print([x.strip() for x in File.readlines()])

# import csv

# field_names = ['No', 'Company', 'Car Model']

# cars = [
# {'No': 1, 'Company': 'Ferrari', 'Car Model': '488 GTB'},
# {'No': 2, 'Company': 'Porsche', 'Car Model': '918 Spyder'},
# {'No': 3, 'Company': 'Bugatti', 'Car Model': 'La Voiture Noire'},
# {'No': 4, 'Company': 'Rolls Royce', 'Car Model': 'Phantom'},
# {'No': 5, 'Company': 'BMW', 'Car Model': 'BMW X7'},
# ]

# with open('Names.csv', 'w') as csvfile:
# 	writer = csv.DictWriter(csvfile, fieldnames = field_names)
# 	writer.writeheader()
# 	writer.writerows(cars)
