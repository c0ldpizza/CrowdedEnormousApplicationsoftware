class Land:
    def __init__(self, name, type, identity):
        self.name = name
        self.type = type
        self.identity = identity

    def isWithinIdentity(self, colors=[]):

        if self.type == "dual":
            if self.identity[0] in colors and self.identity[1] in colors:
                return True

        if self.type == "fetch":
            if self.identity[0] in colors or self.identity[1] in colors:
                return True

        if self.type == "5c":
            if len(colors) > 1:
                return True
