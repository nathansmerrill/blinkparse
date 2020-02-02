# Author: Nathan Merrill (@nathansmerrill)

import sys

from blinkparse.arguments import Arguments
from blinkparse.argument import Argument
from blinkparse.command import Command
from blinkparse.commandArgument import CommandArgument

def parse(args, commands=None, description=None):
    args.append(Argument('help', 'h', description='Show this help page'))
    inputArgs = sys.argv[1:]

    command = None
    if commands is not None:
        try:
            inputCommand = inputArgs[0]
        except IndexError:
            raise ValueError(f'This program requires a command. The options are {list(loopCommand.name for loopCommand in commands)}')
        for command in commands:
            commandArgs = command.check(inputCommand, inputArgs)
            if commandArgs is not None:
                command = command
                break

    outputArgs = {}
    for arg in args:
        outputArgs.update(arg.check(inputArgs))

    finalArgs = Arguments(outputArgs, inputArgs, command, commandArgs)

    if 'help' in finalArgs.args:
        for arg in args:
            print(arg.name)

        sys.exit()

    return finalArgs