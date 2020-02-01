# Author: Nathan Merrill (@nathansmerrill)

import sys

from cliparse2.arguments import Arguments
from cliparse2.argument import Argument
from cliparse2.command import Command
from cliparse2.commandArgument import CommandArgument

def showHelpPage():
    print('help')
    sys.exit()

def parse(args, commands=None, description=None):
    inputArgs = sys.argv[1:]
    command = None
    commandArgs = None
    if commands is not None:
        for loopCommand in commands:
            if inputArgs[0] == loopCommand.name:
                command = loopCommand
                commandArgs = []
                for i, commandArg in enumerate(loopCommand.args):
                    try:
                        value = inputArgs[i + 1]
                        if commandArg.options is not None and value not in commandArg.options:
                            raise ValueError(f'{value} is not a valid argument option. The valid options are {commandArg.options}')
                        commandArgs.append(value)
                    except IndexError:
                        if commandArg.required:
                            raise ValueError(f'Argument {commandArg.name} is required')
                break
        if command is None:
            showHelpPage()
