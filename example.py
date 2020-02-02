from blinkparse import *

args = parse(
    [
        Argument('save', 's', description='Save the program output')
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
print(args.command.name)
print(args.commandArgs)