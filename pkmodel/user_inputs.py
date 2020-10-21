#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:32:54 2020

@author: rebecca
"""
from model import Model

def user_inputs():
    model_list = []
    another = True
    while another is True:
        print('name your model')
        name = input()
        print('how many compartments?')
        num_compartments = input()
        model_list.append(Model(name, num_compartments))
        print("another? [y/n]")
        another_response = input()
        if another_response.lower()[0] == 'n':
            another = False
    return model_list