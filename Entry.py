class Entry:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def get_key(self):
        return self.key

    def get_val(self):
        return self.val

    def set_val(self, val):
        self.val = val

    def __str__(self):
        return "(" + str(self.key) + ": " + str(self.val) + ")"