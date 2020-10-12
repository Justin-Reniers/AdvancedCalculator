from expression.noargexpression.noargexpression import NoArgExpression


class Constant(NoArgExpression):

    def __init__(self, constant: float):
        self.constant = constant

    def __str__(self):
        return '%f' % self.constant

    def evaluate(self, store):
        return self.constant

    def optimize(self):
        return self
