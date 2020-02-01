class CommandArgument:
    def __init__(self, name, options=None, required=False):
        self.name = name
        self.options = options
        self.required = required