import csv
from statistics import mean

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
                change_amounts = []
            else:
                if count_2 == budget_column:
                    budget_total = budget_total + int(column)

                    change_amounts.append(int(column))

            count_2 = count_2 + 1

        count_1 = count_1 + 1
        
    total_months = count_1 - 1

    average_change = mean(change_amounts)

    count_3 = 0

    change_deltas = []

    for item in change_amounts:
        if count_3 == 0:
            pass
        else:
            change_deltas.append(change_amounts[count_3] - change_amounts[count_3 - 1])

        count_3 = count_3 + 1

    average_change = round(mean(change_deltas), 2)

    print(total_months)
    print(budget_total)
    print(average_change)