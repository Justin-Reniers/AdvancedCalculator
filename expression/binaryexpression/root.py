from expression.binaryexpression.binaryexpression import BinaryExpression


class Root(BinaryExpression):

    def __init__(self, baseexpressionl, baseepxressionr):
        BinaryExpression.__init__(self, baseexpressionl, baseepxressionr)

    def __str__(self):
        return '%s + %s' % (self.baseExpressionL, self.baseExpressionR)

    def evaluate(self, store):
        return self.baseExpressionL.evaluate(store) ** (1 / self.baseExpressionR.evaluate(store))

    def optimize(self):
        pass

# todo print statement
