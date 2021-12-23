import csv

my_csv_file = './resources/data.csv'
products = ['appel', 'aap', 'opa', 'appel', 5, True, 5, 7, 'appel']

# writing data from products to csv
with open(my_csv_file, 'w',) as file:
    writer = csv.writer(file)
    writer.writerow(products)


# reading data from csv file into list
with open(my_csv_file) as file:
    reader = csv.reader(file)
    list_csv = list(reader)
print(list_csv)


def frequency(list_to_be_analyzed):
    analyzed_dict = {}

    for item in list_to_be_analyzed:
        if item in analyzed_dict:
            analyzed_dict[item] = analyzed_dict[item] + 1
        else:
            analyzed_dict[item] = 1

    return analyzed_dict


print(frequency(list_csv))
