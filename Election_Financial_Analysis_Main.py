import os
import csv
from statistics import mean

def Election_Analysis(election_input, election_output):
    with open(election_input) as input_file:
        election_data = csv.reader(input_file, delimiter = ',')

        count_1 = 0

        for row in election_data:
            count_2 = 0

            for column in row:
                if count_1 == 0:
                    if column.lower().find('candidate') >= 0:
                        candidate_column = count_2

                    candidate_list = []
                    candidate_votes = []
                else:
                    if count_2 == candidate_column:
                        count_3 = 0

                        for name in candidate_list:
                            if name == column and count_3 == 0:
                                list_position = candidate_list.index(name)

                                candidate_votes[list_position] = candidate_votes[list_position] + 1

                                count_3 = 1

                        if count_3 == 0:
                            candidate_list.append(column)

                            candidate_votes.append(1)

                count_2 = count_2 + 1

            count_1 = count_1 + 1

    total_votes = count_1 - 1

    candidate_distribution = []

    for votes in candidate_votes:
        candidate_distribution.append(round((votes / sum(candidate_votes)) * 100, 3))

    winner_index = candidate_distribution.index(max(candidate_distribution))

    winner = candidate_list[winner_index]

    print(total_votes)
    print(candidate_list)
    print(candidate_distribution)
    print(candidate_votes)
    print(winner)

def Financial_Analysis(financial_input, financial_output):
    with open(financial_input) as input_file:
        budget_data = csv.reader(input_file, delimiter = ',')

        count_1 = 0

        for row in budget_data:
            count_2 = 0

            for column in row:
                if count_1 == 0:
                    if column.lower().find('profit') >= 0 or column.lower().find('losses') >= 0:
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
            change_deltas.append(item - change_amounts[count_3 - 1])

            if item > 0 and change_amounts[count_3 - 1] > 0:
                net_change.append(abs(item) - abs(change_amounts[count_3 - 1]))
            elif item > 0 and change_amounts[count_3 - 1] < 0:
                net_change.append(abs(item) + abs(change_amounts[count_3 - 1]))
            elif item < 0 and change_amounts[count_3 - 1] > 0:
                net_change.append(-1 * (abs(item) + abs(change_amounts[count_3 - 1])))
            elif item < 0 and change_amounts[count_3 - 1] < 0:
                if item > change_amounts[count_3 - 1]:
                    net_change.append(-1 * (abs(item) - abs(change_amounts[count_3 - 1])))
                else:
                    net_change.append(abs(item) - abs(change_amounts[count_3 - 1]))
            else:
                net_change.append(0)

        count_3 = count_3 + 1

    average_change = round(mean(change_deltas), 2)
    greatest_increase = max(net_change)
    greatest_decrease = min(net_change)

    increase_index = net_change.index(greatest_increase)
    decrease_index = net_change.index(greatest_decrease)

    increase_date = change_dates[increase_index + 1]
    decrease_date = change_dates[decrease_index + 1]

    print('Financial Analysis')
    print('------------------------------')
    print('Total Months: ' + str(total_months))
    print('Total: $' + str(budget_total))
    print('Average Change: $' + str(average_change))
    print('Greatest Increase in Profits: ' + increase_date + ' ($' + str(greatest_increase) + ')')
    print('Greatest Decrease in Profits: ' + decrease_date + ' ($' + str(greatest_decrease) + ')')

    #Add Output File

current_path = os.getcwd()
current_directory = os.listdir()

for item in current_directory:
    if item.lower().find('election') >= 0 and item.lower().find('py') == -1:
        election_output = os.path.join(current_path, item, 'Election_Results.txt')

        for data in os.listdir(os.path.join(current_path, item)):
            if data.lower().find('election') >= 0 and data.lower().find('csv') >= 0:

                election_input = os.path.join(current_path, item, data)
    elif item.lower().find('financial') >= 0 and item.lower().find('py') == -1:
        financial_output = os.path.join(current_path, item, 'Financial_Results.txt')

        for data in os.listdir(os.path.join(current_path, item)):
            if data.lower().find('budget') >= 0 and data.lower().find('csv') >= 0:

                financial_input = os.path.join(current_path, item, data)

Election_Analysis(election_input, election_output)

Financial_Analysis(financial_input, financial_output)