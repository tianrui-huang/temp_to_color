class ExponentialSmoother:
    def __init__(self, alpha=0.15):
        self.alpha = alpha
        self.value = None

    def update(self, new_value):
        if self.value is None:
            self.value = new_value
        else:
            self.value += (new_value - self.value) * self.alpha

        return self.value