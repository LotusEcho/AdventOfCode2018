#!/usr/bin/python3
import os
dirname = os.path.dirname(__file__)

filename = os.path.join(dirname, 'day1_input.txt')

file = open(filename, 'r')
frequency = 0

for line in file:
    previousFrequency = frequency
    change = int(line)
    frequency = frequency + change
    print(f'Current frequency: {previousFrequency}; Change in frequency: {change}; New Frequency: {frequency}')
