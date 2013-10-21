# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:10:04 2013

@author: kundlj
"""

from os import listdir
from os.path import isfile, join, isdir
from processfile import process_file_gonogo, process_file_audio

def build_dict(test_type, dirname):
    if test_type == 'audio':
       return build_dict_audio(dirname)
    elif test_type == 'gonogo':
        return build_dict_gonogo(dirname)

def build_dict_gonogo(dirname):
    """ Builds a dictionary with data categorized by condition, subject
        session, and trial. """

    data = {}
    dirnames = [x for x in listdir(dirname) if isdir(join(dirname, x))]
    num_subjects = num_sessions = num_trials = 0
    
    for condition in dirnames:
        filenames = [join(join(dirname, condition), x) for x in listdir(join(dirname, condition)) if isfile(join(join(dirname, condition), x))]
        data.update({condition: {}})
        
        for filename in filenames:
            info = [x.strip('.txt') for x in filename.split('_')]
            
            subject = int(info[1][8:])
            session = int(info[2][8:])
            trial = int(info[3][6:])

            if subject > num_subjects:
                num_subjects = subject
            if session > num_sessions:
                num_sessions = session
            if trial > num_trials:
                num_trials = trial
                
        for subjects in range(1, num_subjects + 1):
            data[condition].update({str(subjects): {}})
            for sessions in range(1, num_sessions + 1):
                data[condition][str(subjects)].update({str(sessions): {}})
                

        
        for current in filenames:
            processed = process_file_gonogo(current)
            
            subject = processed[0][0]
            session = processed[0][1]
            trial = processed[0][2]

            info = processed[1]
            
            data[condition][subject][session].update({trial: info})
            
    return data, [num_subjects, num_sessions, num_trials]

def build_dict_audio(dirname):
    """ Builds a dictionary with data categorized by condition, subject
        session, and trial. """

    data = {}
    dirnames = [x for x in listdir(dirname) if isdir(join(dirname, x))]
    num_subjects = num_sessions = num_trials = 0
    
    for condition in dirnames:
        filenames = [join(join(dirname, condition), x) for x in listdir(join(dirname, condition)) if isfile(join(join(dirname, condition), x))]
        data.update({condition: {}})
        
        for filename in filenames:
            info = [x.strip('.txt') for x in filename.split('_')]

            subject = int(info[1][8:])
            session = int(info[2][8:])
            trial = int(info[3][5:])

            if subject > num_subjects:
                num_subjects = subject
            if session > num_sessions:
                num_sessions = session
            if trial > num_trials:
                num_trials = trial
                
        for subjects in range(1, num_subjects + 1):
            data[condition].update({str(subjects): {}})
            for sessions in range(1, num_sessions + 1):
                data[condition][str(subjects)].update({str(sessions): {}})
                

        
        for current in filenames:
            processed = process_file_audio(current)
            
            subject = processed[0][0]
            session = processed[0][1]
            trial = processed[0][2]

            info = processed[1]
            
            data[condition][subject][session].update({trial: info})
            
    return data, [num_subjects, num_sessions, num_trials]