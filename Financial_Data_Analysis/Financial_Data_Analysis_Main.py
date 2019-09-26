import csv

with open('Budget_Data.csv') as input_file:
    budget_data = csv.reader(input_file, delimiter = ',')

    count_1 = 0

    for row in budget_data:
        count_2 = 0

        for column in row:
            if count_1 == 0:
                if column.lower().find('date') >= 0:
                    date_column = count_2
                elif column.lower().find('profit') >= 0 or column.lower().find('losses') >= 0:
                    budget_column = count_2

                budget_total = 0
            else:
                if count_2 == budget_column:
                    budget_total = budget_total + int(column)

            count_2 = count_2 + 1

        count_1 = count_1 + 1
        
    total_months = count_1 - 1

    print(total_months)
    print(budget_total)