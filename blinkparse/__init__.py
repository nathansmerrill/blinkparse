# Author: Nathan Merrill (@nathansmerrill)

import sys

from blinkparse.arguments import Arguments
from blinkparse.argument import Argument
from blinkparse.command import Command
from blinkparse.commandArgument import CommandArgument

def showHelpPage():
    print('help')
    sys.exit()

def parse(args, commands=None, description=None):
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

    return Arguments(outputArgs, inputArgs, command, commandArgs)