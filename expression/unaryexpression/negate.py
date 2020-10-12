from expression.unaryexpression.unaryexpression import UnaryExpression


class Negate(UnaryExpression):

    def __init__(self, baseexpression):
        UnaryExpression.__init__(self, baseexpression)

    def __str__(self):
        return '-%s' % self.baseExpression

    def evaluate(self, store):
        return (-1) * self.baseExpression.evaluate(store)

    def optimize(self):
        pass
