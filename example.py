from blinkparse import *

args = parse(
    [
        Argument('save', 's', description='Save the program output')
    ],
    [
        Command('hello', [
            CommandArgument('person', required=True),
            CommandArgument('gender', options=['male', 'female', 'other'])
        ]),
        Command('bye', [
            CommandArgument('person', required=True)
        ])
    ]
)
print(args.command)
print(args.commandArgs)