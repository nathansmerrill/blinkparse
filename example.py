from blinkparse import *

args = Parser(
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
    ''',
    commandRequired=True
).parse()

if args.command == 'hello':
    output = 'Hello ' + args.commandArgs['person']
    if 'gender' in args.commandArgs:
        output += ', you are ' + args.commandArgs['gender']

if args.command == 'bye':
    output = 'Bye ' + args.commandArgs['person']

if 'save' in args.args:
    with open('hello.txt', 'w') as outputFile:
        outputFile.write(output)
else:
    print(output)
