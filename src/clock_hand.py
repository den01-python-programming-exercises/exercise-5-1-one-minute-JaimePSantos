class ClockHand:

    def __init__(self,limit):
        self.limit = limit
        self.value = 0

    def advance(self):
        self.value = self.value + 1

        if (self.value >= self.limit):
            self.value = 0

    def get_value(self):
        return self.value

    def __str__(self):
        if (self.value < 10):
            return "0" + str(self.value)

        return "" + str(self.value)
