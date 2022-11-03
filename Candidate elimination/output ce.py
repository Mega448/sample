Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: C:/Users/cse/Desktop/candidate elimination.py ===========

Instances are:
 [['sunny' 'warm' 'normal' 'warm']
 ['rainy' 'cold' 'high' 'cool']
 ['sunny' 'warm' 'high' 'warm']
 ['sunny' 'warm' 'normal' 'cool']]

Target Values are:  ['yes' 'no' 'no' 'yes']

Initialization of specific_h and general_h

Specific Boundary:  ['sunny' 'warm' 'normal' 'warm']

Generic Boundary:  [['?', '?', '?', '?'], ['?', '?', '?', '?'], ['?', '?', '?', '?'], ['?', '?', '?', '?']]

Instance 1 is  ['sunny' 'warm' 'normal' 'warm']

Instance 2 is  ['rainy' 'cold' 'high' 'cool']

Instance 3 is  ['sunny' 'warm' 'high' 'warm']

Instance 4 is  ['sunny' 'warm' 'normal' 'cool']
Instance is Positive 
Specific Boundary after  4 Instance is  ['sunny' 'warm' 'normal' '?']
Generic Boundary after  4 Instance is  [['?', '?', '?', '?'], ['?', '?', '?', '?'], ['?', '?', '?', '?'], ['?', '?', '?', '?']]


Final Specific_h: 
['sunny' 'warm' 'normal' '?']
Final General_h: 
[['?', '?', '?', '?'], ['?', '?', '?', '?'], ['?', '?', '?', '?'], ['?', '?', '?', '?']]
>>> 
