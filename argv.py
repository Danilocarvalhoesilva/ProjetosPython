#!/bin/env/python
import sys

#print ('Number of arguments:',len(sys.argv))
print('Number of arguments: '+str(len(sys.argv)))

# Arguments are printed as a list
print ('Arguments:', str(sys.argv).split(':'))
console_input = ' '.join(sys.argv[4:]).strip()
print('Combined: '+console_input)
#print(sys.argv[3][4]) #will print main.py


print('Number of arguments: {}'.format(len(sys.argv)))
print('Argument(s) passed: {}'.format(str(sys.argv[4-5])))

