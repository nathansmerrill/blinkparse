class Command:
    def __init__(self, name, args=[]):
        self.name = name
        self.args = args

    def check(self, inputCommand, inputArgs):
        if inputCommand == self.name:
            commandArgs = []
            for i, commandArg in enumerate(self.args):
                try:
                    value = inputArgs[i + 1]
                except IndexError:
                    if commandArg.required:
                        raise ValueError(f'Argument {commandArg.name} is required')
                    else:
                        continue
                if commandArg.options is not None and value not in commandArg.options:
                    raise ValueError(f'{value} is not a valid argument option. The valid options are {commandArg.options}')
                if commandArg.required or value[0] != '-':
                    commandArgs.append(value)
            return commandArgs
        return None