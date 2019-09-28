#Import Modules
import os
import csv
from statistics import mean

#Define Election Data Processing Function
def Election_Analysis(election_input, election_output):

    #Open Election Data CSV File
    with open(election_input) as input_file:

        #Import Election Data from CSV File
        election_data = csv.reader(input_file, delimiter = ',')

        #Set Counter Variable for Row Number
        count_1 = 0

        #Loop Through Rows in CSV File
        for row in election_data:

            #Set Counter Variable for Column Number
            count_2 = 0

            #Loop Through Columns in Each Row
            for column in row:

                #Define Condition for Header Row
                if count_1 == 0:

                    #Find Column with Candidate Names & Assign Column Number to Vaiable
                    if column.lower().find('candidate') >= 0:
                        candidate_column = count_2

                    #Define Lists for Candidate Names and Vote Count
                    candidate_list = []
                    candidate_votes = []
                else:

                    #Define Condition for Candidate Name Column in Data Rows
                    if count_2 == candidate_column:
                        
                        #Set Counter Variable for Candidate Name Existence
                        count_3 = 0

                        #Loop Through Names in Candidate Name List
                        for name in candidate_list:
                            
                            #Set Condition for Candidate Name Already in Candidate Name List
                            if name == column and count_3 == 0:
                                #Find Index Position of Name in Candidate Name List
                                list_position = candidate_list.index(name)

                                #Add One Vote to Appropriate Current Tally of Candidate Votes in Candidate Vote List
                                candidate_votes[list_position] = candidate_votes[list_position] + 1

                                #Update Counter Variable for Candidate Name Existence
                                count_3 = 1

                        #Set Condition for Candidate Name Not Found in Candidate Name List
                        if count_3 == 0:
                            #Add Candidate Name to Candidate Name List
                            candidate_list.append(column)

                            #
                            candidate_votes.append(1)

                #Increment Column Number
                count_2 = count_2 + 1

            #Increment Row Number
            count_1 = count_1 + 1

    #Calculate Total Votes Cast
    total_votes = count_1 - 1

    #Define Array for Candidate Vote Distribution
    candidate_distribution = []

    #Loop Through Array of Candidate Votes
    for votes in candidate_votes:
        
        #Calculate Candidate Vote Distribution & Add to Candidate Vote Distribution Array
        candidate_distribution.append(round((votes / sum(candidate_votes)) * 100, 3))

    #Find Index Position of Winnin Candidate Based on Vote Distribution
    winner_index = candidate_distribution.index(max(candidate_distribution))

    #Extract Name of Winning Candidate
    winner = candidate_list[winner_index]

    #Output Election Results to Terminal
    print('\n')
    print('Election Results')
    print('------------------------------')
    print('Total Votes: ' + str(total_votes))
    print('------------------------------')
    
    for count_4 in range(len(candidate_list)):
        print(candidate_list[count_4] + ': ' + str(candidate_distribution[count_4]) + '% (' + str(candidate_votes[count_4]) + ')')

    print('------------------------------')
    print('Winner: ' + winner)

    #Create Election Results Text File
    output_file = open(election_output, 'w')

    #Output Election Results to Text File
    output_file.write('Election Results\n')
    output_file.write('------------------------------\n')
    output_file.write('Total Votes: ' + str(total_votes) + '\n')
    output_file.write('------------------------------\n')
    
    for count_5 in range(len(candidate_list)):
        output_file.write(candidate_list[count_5] + ': ' + str(candidate_distribution[count_5]) + '% (' + str(candidate_votes[count_5]) + ')\n')

    output_file.write('------------------------------\n')
    output_file.write('Winner: ' + winner + '\n')

    #Close Election Results Text File
    output_file.close()

#Define Financial Data Processing Function
def Financial_Analysis(financial_input, financial_output):
    
    #Open Budget Data CSV
    with open(financial_input) as input_file:
        
        #Import Budget Data from CSV File
        budget_data = csv.reader(input_file, delimiter = ',')

        #Set Counter Variable for Row Number
        count_1 = 0

        #Loop Through Rows in CSV File
        for row in budget_data:
            
            #Set Counter Variable for Column Number
            count_2 = 0

            #Loop Through Columns in Each Row
            for column in row:
                
                #Define Condition for Header Row
                if count_1 == 0:
                    
                    #Find Column with Profit/Loss Data & Assign Column Number to Variable
                    if column.lower().find('profit') >= 0 or column.lower().find('losses') >= 0:
                        budget_column = count_2

                    #Initialize Total Budget Variable & Define Lists for Dates and Amount of Budget Changes
                    budget_total = 0
                    change_amounts = []
                    change_dates = []
                else:

                    #Define Condition for Profit/Loss Column in Data Rows
                    if count_2 == budget_column:
                        
                        #Add Current Profit/Loss Value to Total Budget Variable
                        budget_total = budget_total + int(column)

                        #Add Current Profit/Loss Value to Budget Change Amount List
                        change_amounts.append(int(column))
                    else:
                        #Add Current Date to Budget Change Date List
                        change_dates.append(column)

                #Increment Column Number
                count_2 = count_2 + 1

            #Increment Row Number
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

    print('\n')
    print('Financial Analysis')
    print('------------------------------')
    print('Total Months: ' + str(total_months))
    print('Total: $' + str(budget_total))
    print('Average Change: $' + str(average_change))
    print('Greatest Increase in Profits: ' + increase_date + ' ($' + str(greatest_increase) + ')')
    print('Greatest Decrease in Profits: ' + decrease_date + ' ($' + str(greatest_decrease) + ')')

    output_file = open(financial_output, 'w')

    output_file.write('Financial Analysis\n')
    output_file.write('------------------------------\n')
    output_file.write('Total Months: ' + str(total_months) + '\n')
    output_file.write('Total: $' + str(budget_total) + '\n')
    output_file.write('Average Change: $' + str(average_change) + '\n')
    output_file.write('Greatest Increase in Profits: ' + increase_date + ' ($' + str(greatest_increase) + ')\n')
    output_file.write('Greatest Decrease in Profits: ' + decrease_date + ' ($' + str(greatest_decrease) + ')\n')

    output_file.close()

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