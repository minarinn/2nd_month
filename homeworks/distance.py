class Distance:
    def __init__(self, value, measure):
        self.value = value
        self.measure = measure

    def __str__(self):
        return f"{self.value} {self.measure}"

    def __add__(self, other):
        return Distance(self.value + other.value, self.measure)

    def __sub__(self, other):
        return Distance(self.value - other.value, self.measure)
