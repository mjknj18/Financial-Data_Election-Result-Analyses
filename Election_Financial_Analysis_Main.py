import os
import csv
from statistics import mean

current_path = os.getcwd()
current_directory = os.listdir()

for item in current_directory:
    if item.lower().find('election') >= 0:
        print(x = 1)
    elif item.lower().find('election') >= 0:
        print(x = 2)

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
                change_dates = []
            else:
                if count_2 == budget_column:
                    budget_total = budget_total + int(column)

                    change_amounts.append(int(column))
                else:
                    change_dates.append(column)

            count_2 = count_2 + 1

        count_1 = count_1 + 1
        
    total_months = count_1 - 1

    average_change = mean(change_amounts)

    count_3 = 0

    change_deltas = []
    net_change = []

    for item in change_amounts:
        if count_3 == 0:
            pass
        else:
            change_deltas.append(change_amounts[count_3] - change_amounts[count_3 - 1])

            if change_amounts[count_3] > 0 and change_amounts[count_3 - 1] > 0:
                net_change.append(abs(change_amounts[count_3]) - abs(change_amounts[count_3 - 1]))
            elif change_amounts[count_3] > 0 and change_amounts[count_3 - 1] < 0:
                net_change.append(abs(change_amounts[count_3]) + abs(change_amounts[count_3 - 1]))
            elif change_amounts[count_3] < 0 and change_amounts[count_3 - 1] > 0:
                net_change.append(-1 * (abs(change_amounts[count_3]) + abs(change_amounts[count_3 - 1])))
            elif change_amounts[count_3] < 0 and change_amounts[count_3 - 1] < 0:
                if change_amounts[count_3] > change_amounts[count_3 - 1]:
                    net_change.append(-1 * (abs(change_amounts[count_3]) - abs(change_amounts[count_3 - 1])))
                else:
                    net_change.append(abs(change_amounts[count_3]) - abs(change_amounts[count_3 - 1]))
            else:
                net_change.append(0)

        count_3 = count_3 + 1

    average_change = round(mean(change_deltas), 2)
    greatest_increase = max(net_change)
    greatest_decrease = min(net_change)

    print(total_months)
    print(budget_total)
    print(average_change)
    print(greatest_increase)
    print(greatest_decrease)