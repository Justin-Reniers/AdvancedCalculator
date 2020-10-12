from expression.unaryexpression.unaryexpression import UnaryExpression


class Tangent(UnaryExpression):

    def __init__(self, baseexpression):
        UnaryExpression.__init__(self, baseexpression)

    def __str__(self):
        return 'tan(%s)' % self.baseExpression

    def evaluate(self, store):
        return self.baseExpression.evaluate(store)

    def optimize(self):
        super().optimize()
