class Entry:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self):
        return "(" + str(self.key) + ": " + str(self.val) + ")"