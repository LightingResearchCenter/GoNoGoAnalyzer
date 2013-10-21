# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:10:01 2013

@author: kundlj
"""

from builddict import build_dict
from sys import exit

def makefile(test_type, savename, dirname):

    if test_type == 'audio' or test_type == 'gonogo':
        pass
    else:
        print 'Error: Usage: test-type <audio | gonogo> output-name dir-name'
        exit(1)

    savename_subject = savename[:savename.find('.')] + '-by_subject.csv'
    savename_evaluation = savename[:savename.find('.')] + '-by_evaluation.csv'
    
    data, numbers = build_dict(test_type, dirname)
    
    num_conditions = len(data.keys())
    num_subjects = numbers[0]
    num_sessions = numbers[1]
    num_trials = numbers[2]
    
    data_array = [-1] * num_conditions
    for x in range(num_conditions):
        data_array[x] = [-1] * num_subjects
        for y in range(num_subjects):
            data_array[x][y] = [-1] * num_sessions
            for z in range(num_sessions):
                data_array[x][y][z] = [-1] * num_trials

    condition_num = 0
    conditions = ['NULL'] * num_conditions
    
    for condition_key in data.keys():
        conditions[condition_num] = condition_key
        for subject_key in data[condition_key].keys():
            
            for session_key in data[condition_key][subject_key].keys():
                
                for trial_key in data[condition_key][subject_key][session_key].keys():

                    if data[condition_key][subject_key][session_key].has_key(trial_key):
                        data_array[condition_num][int(subject_key) - 1][int(session_key) - 1][int(trial_key) - 1] = \
                        data[condition_key][subject_key][session_key][trial_key]
        condition_num += 1
        
    
    if num_trials % 2 == 0:
        pre_num = num_trials / 2 - 1
        post_num = num_trials / 2
    else:
        pre_num = post_num = num_trials / 2
   
    
    with open(savename_subject, 'w') as file_pointer:
        for itr0 in range(len(data_array)):
            file_pointer.write('Condition: ' + conditions[itr0] + '\n\n')
            for itr1 in range(len(data_array[itr0]) - num_subjects, len(data_array[itr0])):
                file_pointer.write('Subject ' + str(itr1 + 1) + ':\n,')
                for itr2 in range(len(data_array[itr0][itr1])):
                    for count in range(pre_num):
                        file_pointer.write(',')
                    file_pointer.write('Session ' + str(itr2 + 1) + ',')
                    for count in range(post_num):
                        file_pointer.write(',')
                file_pointer.write('\n,')
                for itr2 in range(len(data_array[itr0][itr1])):
                    for itr3 in range(len(data_array[itr0][itr1][itr2])):
                        file_pointer.write('Trial ' + str(itr3 + 1) + ',')
                file_pointer.write('\nValid Median,')
                for itr2 in range(len(data_array[itr0][itr1])):
                    for itr3 in range(len(data_array[itr0][itr1][itr2])):
                        if type(data_array[itr0][itr1][itr2][itr3]) is list:
                            file_pointer.write(str(data_array[itr0][itr1][itr2][itr3][0]))
                        file_pointer.write(',')
                file_pointer.write('\n')
                file_pointer.write('Valid Mean,')
                for itr2 in range(len(data_array[itr0][itr1])):
                    for itr3 in range(len(data_array[itr0][itr1][itr2])):
                        if type(data_array[itr0][itr1][itr2][itr3]) is list:
                            file_pointer.write(str(data_array[itr0][itr1][itr2][itr3][1]))
                        file_pointer.write(',')
                file_pointer.write('\n')
                file_pointer.write('Percent Missed,')
                for itr2 in range(len(data_array[itr0][itr1])):
                    for itr3 in range(len(data_array[itr0][itr1][itr2])):
                        if type(data_array[itr0][itr1][itr2][itr3]) is list:
                            file_pointer.write(str(data_array[itr0][itr1][itr2][itr3][2]) + '%')
                        file_pointer.write(',')
                file_pointer.write('\n')
                file_pointer.write('Percent False,')
                for itr2 in range(len(data_array[itr0][itr1])):
                    for itr3 in range(len(data_array[itr0][itr1][itr2])):
                        if type(data_array[itr0][itr1][itr2][itr3]) is list:
                            file_pointer.write(str(data_array[itr0][itr1][itr2][itr3][3]) + '%')
                        file_pointer.write(',')
                file_pointer.write('\n')
                file_pointer.write('Error Rate,')
                for itr2 in range(len(data_array[itr0][itr1])):
                    for itr3 in range(len(data_array[itr0][itr1][itr2])):
                        if type(data_array[itr0][itr1][itr2][itr3]) is list:
                            file_pointer.write(str(data_array[itr0][itr1][itr2][itr3][4]))
                        file_pointer.write(',')
                file_pointer.write('\n')
                file_pointer.write('Worst Median,')
                for itr2 in range(len(data_array[itr0][itr1])):
                    for itr3 in range(len(data_array[itr0][itr1][itr2])):
                        if type(data_array[itr0][itr1][itr2][itr3]) is list:
                            file_pointer.write(str(data_array[itr0][itr1][itr2][itr3][5]))
                        file_pointer.write(',')
                file_pointer.write('\n')
                file_pointer.write('Worst Mean,')
                for itr2 in range(len(data_array[itr0][itr1])):
                    for itr3 in range(len(data_array[itr0][itr1][itr2])):
                        if type(data_array[itr0][itr1][itr2][itr3]) is list:
                            file_pointer.write(str(data_array[itr0][itr1][itr2][itr3][6]))
                        file_pointer.write(',')
                file_pointer.write('\n')
                file_pointer.write('Best Median,')
                for itr2 in range(len(data_array[itr0][itr1])):
                    for itr3 in range(len(data_array[itr0][itr1][itr2])):
                        if type(data_array[itr0][itr1][itr2][itr3]) is list:
                            file_pointer.write(str(data_array[itr0][itr1][itr2][itr3][7]))
                        file_pointer.write(',')
                file_pointer.write('\n')
                file_pointer.write('Best Mean,')
                for itr2 in range(len(data_array[itr0][itr1])):
                    for itr3 in range(len(data_array[itr0][itr1][itr2])):
                        if type(data_array[itr0][itr1][itr2][itr3]) is list:
                            file_pointer.write(str(data_array[itr0][itr1][itr2][itr3][8]))
                        file_pointer.write(',')
                file_pointer.write('\n')
                file_pointer.write('Worst Throughput,')
                for itr2 in range(len(data_array[itr0][itr1])):
                    for itr3 in range(len(data_array[itr0][itr1][itr2])):
                        if type(data_array[itr0][itr1][itr2][itr3]) is list:
                            file_pointer.write(str(data_array[itr0][itr1][itr2][itr3][9]))
                        file_pointer.write(',')
                file_pointer.write('\n')
                file_pointer.write('Best Throughput,')
                for itr2 in range(len(data_array[itr0][itr1])):
                    for itr3 in range(len(data_array[itr0][itr1][itr2])):
                        if type(data_array[itr0][itr1][itr2][itr3]) is list:
                            file_pointer.write(str(data_array[itr0][itr1][itr2][itr3][10]))
                        file_pointer.write(',')
                file_pointer.write('\n\n')
            file_pointer.write('\n')

    metrics = ['Valid Median', 'Valid Mean', 'Percent Missed', 'Percent False', 'Error Rate', \
                'Top Median', 'Top Mean', 'Bottom Median', 'Bottom Mean', 'Top Throughput', 'Bottom Throughput' ]
    metric_num = 0

    with open(savename_evaluation, 'w') as file_pointer:
        for itr0 in range(len(data_array)):
            file_pointer.write('Condition: ' + conditions[itr0] + '\n\n')
            for metric in metrics:
                file_pointer.write(metric + ':\n,')
                for itr1 in range(num_sessions):
                    for count in range(pre_num):
                        file_pointer.write(',')
                    file_pointer.write('Session ' + str(itr1 + 1) + ',')
                    for count in range(post_num):
                        file_pointer.write(',')
                file_pointer.write('\n,')
                for itr1 in range(num_sessions):
                    for itr2 in range(num_trials):
                        file_pointer.write('Trial ' + str(itr2 + 1) + ',')
                file_pointer.write('\n')
                for itr2 in range(len(data_array[itr0]) - num_subjects, len(data_array[itr0])):
                    file_pointer.write('Subject: ' + str(itr2 + 1) + ',')
                    session_loc = trial_loc = 0
                    for itr3 in range(num_sessions):
                        for itr4 in range(num_trials):
                            if type(data_array[itr0][itr2][session_loc][trial_loc]) is list:
                                if metric_num == 2 or metric_num == 3:
                                    file_pointer.write(str(data_array[itr0][itr2][session_loc][trial_loc][metric_num]) + '%')
                                else:
                                    file_pointer.write(str(data_array[itr0][itr2][session_loc][trial_loc][metric_num]))
                            file_pointer.write(',')
                            trial_loc += 1
                        session_loc += 1
                        trial_loc = 0
                    file_pointer.write('\n')
                metric_num += 1
                file_pointer.write('\n')
            metric_num = 0



