# -*- coding: utf-8 -*-
"""
Created on Wed Mar 05 09:23:42 2014

@author: kundlj
"""

from os import listdir
from os.path import join, isdir
import shutil

def collect_data(dirname, outdir):
    """ This is a "single use" file for reorganizing and renaming Navy GNG files. """
    
    dirnames = [x for x in listdir(dirname) if isdir(join(dirname, x))]
    for cur_dir in dirnames:
        new_filename = 'GONOGO_Subject '
        sub_dir = join(dirname, cur_dir)
        if sub_dir[-2:] == 'A1':
            new_filename += '1'
        elif sub_dir[-2:] == 'A2':
            new_filename += '2'
        elif sub_dir[-2:] == 'A3':
            new_filename += '3'
        elif sub_dir[-2:] == 'A4':
            new_filename += '4'
        elif sub_dir[-2:] == 'A5':
            new_filename += '5'
        elif sub_dir[-2:] == 'A6':
            new_filename += '6'
        elif sub_dir[-2:] == 'B3':
            new_filename += '7'
        elif sub_dir[-2:] == 'B5':
            new_filename += '8'
        elif sub_dir[-2:] == 'B6':
            new_filename += '9'
        elif sub_dir[-2:] == 'B7':
            new_filename += '10'
        elif sub_dir[-2:] == 'B8':
            new_filename += '11'  
        new_filename += '_Session 1_Trial '
        sub_fname = new_filename
        for time_dir in listdir(sub_dir):
            new_filename = sub_fname
            if time_dir == 'Tuesday 500pm':
                new_filename += '1'
            elif time_dir == 'Tuesday 900pm':
                new_filename += '2'
            elif time_dir == 'Wednesday 100am':
                new_filename += '3'
            elif time_dir == 'Wednesday 500am':
                new_filename += '4'
            elif time_dir == 'Wednesday 900am':
                new_filename += '5'
            elif time_dir == 'Wednesday 100pm':
                new_filename += '6'
            elif time_dir == 'Wednesday 500pm':
                new_filename += '7'
            elif time_dir == 'Wednesday 900pm':
                new_filename += '8'
            elif time_dir == 'Thursday 100am':
                new_filename += '9'
            elif time_dir == 'Thursday 500am':
                new_filename += '10'
            elif time_dir == 'Thursday 900am':
                new_filename += '11'
            elif time_dir == 'Thursday 100pm':
                new_filename += '12'
            elif time_dir == 'Thurs 500 PM' or time_dir == 'Thursday 500pm':
                new_filename += '13'
            elif time_dir == 'Thurs 900 PM' or time_dir == 'Thursday 900pm':
                new_filename += '14'
            elif time_dir == 'Friday 100 AM' or time_dir == 'Friday 100am':
                new_filename += '15'
            elif time_dir == 'Friday 500 AM'  or time_dir == 'Friday 500am':
                new_filename += '16'
            elif time_dir == 'Friday 900 AM'  or time_dir == 'Friday 900am':
                new_filename += '17'
            elif time_dir == 'Friday 100 PM' or time_dir == 'Friday 100pm':
                new_filename += '18'
            elif time_dir == 'Friday 500 PM'  or time_dir == 'Friday 500pm':
                new_filename += '19'
            elif time_dir == 'Friday 900 PM' or time_dir == 'Friday 900pm':
                new_filename += '20'
            elif time_dir == 'Sat 100 AM' or time_dir == 'Saturday 100am':
                new_filename += '21'
            elif time_dir == 'Sat 500 AM' or time_dir == 'Saturday 500am':
                new_filename += '22'
            elif time_dir == 'Sat 900 AM' or time_dir == 'Saturday 900am':
                new_filename += '23'
            elif time_dir == 'Sat 100 PM' or time_dir == 'Saturday 100pm':
                new_filename += '24'
            elif time_dir == 'Sat 500 PM' or time_dir == 'Saturday 500pm':
                new_filename += '25'
            new_filename += '.txt'
            gonogo_dir = join(join(sub_dir, time_dir), 'Go No Go')
            for filename in listdir(gonogo_dir):
                if filename[:6] == 'GONOGO':
                    shutil.copy(join(gonogo_dir, filename), join(outdir, new_filename))
    