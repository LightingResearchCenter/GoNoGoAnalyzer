# -*- coding: utf-8 -*-
"""
Created on Wed Mar 05 09:23:42 2014

@author: kundlj
"""

from os import listdir
from os.path import join, isdir
import shutil

subjects = {
            'A1' : '1',
            'A2' : '2',
            'A3' : '3',
            'A4' : '4',
            'A5' : '5',
            'A6' : '6',
            'B3' : '7',
            'B5' : '8',
            'B6' : '9',
            'B7' : '10',
            'B8' : '11'
}

trials = {
            '0800' : '1',
            '1200' : '2',
            '1600' : '3',
            '2000' : '4',
            'Day 2 0800' : '5',
            '0800 Day 2' : '5'
}

def collect_data(dirname, outdir):
    """ This is a "single use" file for reorganizing and renaming Navy GNG files. """
    
    dirnames = [x for x in listdir(dirname) if isdir(join(dirname, x))]
    for cur_dir in dirnames:
        new_filename = 'GONOGO_Subject '
        sub_dir = join(dirname, cur_dir)
        if sub_dir[-11:-9] in subjects.keys():
            new_filename += subjects[sub_dir[-11:-9]]
        else:
            continue
        new_filename += '_Session 1_Trial '
        sub_fname = new_filename
        for time_dir in listdir(sub_dir):
            new_filename = sub_fname
            if time_dir in trials.keys():
                new_filename += trials[time_dir]
            else:
                continue
            new_filename += '.txt'
            gonogo_dir = join(join(sub_dir, time_dir), 'GoNoGo')
            for filename in listdir(gonogo_dir):
                if filename[:6] == 'GONOGO':
                    shutil.copy(join(gonogo_dir, filename), join(outdir, new_filename))
    