from expression.unaryexpression.unaryexpression import UnaryExpression


class Factorial(UnaryExpression):

    def __init__(self, baseexpression):
        UnaryExpression.__init__(self, baseexpression)

    def __str__(self):
        return '%s!' % self.baseExpression

    def evaluate(self, store):
        value = 1
        for i in range(1, self.baseExpression.evaluate(store)+1):
            print(value)
            value = value * i
        return value

    def optimize(self):
        return self.baseExpression.optimize()
