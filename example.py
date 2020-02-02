from blinkparse import *

args = parse(
    args=[
        Argument('save', 's', description='Save the program output'),
        Argument('bruh', 'b', takesValue=True, description='Bruh')
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
# print('args')
# print(args.args)
# print('operands')
# print(args.operands)
# print('command')
# print(args.command.name)
# print('command name')
# print(args.commandArgs)