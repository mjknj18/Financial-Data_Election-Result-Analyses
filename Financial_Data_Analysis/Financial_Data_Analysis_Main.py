import csv

with open('Budget_Data.csv') as input_file:
    budget_data = csv.reader(input_file, delimiter = ',')

    count_1 = 0

    for row in budget_data:
        count_2 = 0

        for column in row:
            if count_1 == 0:
                print(column)

            count_2 = count_2 + 1

        count_1 = count_1 + 1
        