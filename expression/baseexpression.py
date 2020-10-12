class BaseExpression:

    def __init__(self):
        self._constant = float

    def __str__(self):
        return 'BaseExpr{' + '}'

    def evaluate(self, store):
        return self.evaluate(store)

    def optimize(self):
        pass

    def get_constant(self):
        return self._constant
