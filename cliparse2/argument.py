class Argument:
    def __init__(self, name, shortName=None, takesValue=False, required=False, description=None):
        self.name = name
        self.shortName = shortName
        self.takesValue = takesValue
        self.required = required
        self.description = description