from expression.binaryexpression.binaryexpression import BinaryExpression
from expression.noargexpression.constant import Constant


class Multiplication(BinaryExpression):

    def __init__(self, baseexpressionl, baseepxressionr):
        BinaryExpression.__init__(self, baseexpressionl, baseepxressionr)

    def __str__(self):
        return '(%s * %s)' % (self.baseExpressionL, self.baseExpressionR)

    def evaluate(self, store):
        return self.baseExpressionL.evaluate(store) * self.baseExpressionR.evaluate(store)

    def optimize(self):
        left = self.baseExpressionL.optimize()
        right = self.baseExpressionR.optimize()
        if (isinstance(left, Constant) and left.get_constant() == 0) or \
                (isinstance(right, Constant) and right.get_constant() == 0):
            return Constant(0)
        if isinstance(left, Constant) and left.get_constant() == 1:
            return right
        if isinstance(right, Constant) and right.get_constant() == 1:
            return left
        return self
