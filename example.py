from blinkparse import *

args = parse(
    [
        Argument('save', 's', description='Save the program output'),
        Argument('bruh', 'b', takesValue=True, description='Bruh')
    ],
    [
        Command('hello', [
            CommandArgument('person'),
            CommandArgument('gender', required=False, options=['male', 'female', 'other'])
        ]),
        Command('bye', [
            CommandArgument('person')
        ])
    ]
)
print('args')
print(args.args)
print('operands')
print(args.operands)
print('command')
print(args.command.name)
print('command name')
print(args.commandArgs)