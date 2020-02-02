from blinkparse import *

args = parse(
    args=[
        Argument('save', 's', description='Save the program output'),
    ],
    commands=[
        Command('hello', [
            CommandArgument('person'),
            CommandArgument('gender', required=False, options=['male', 'female', 'other'])
        ]),
        Command('bye', [
            CommandArgument('person')
        ])
    ],
    description='''
hello.py
A simple demo of blinkparse
    '''
)
