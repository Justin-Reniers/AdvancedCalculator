from expression.baseexpression import BaseExpression


class BinaryExpression(BaseExpression):

    def __init__(self, baseexpressionl, baseepxressionr):
        self.baseExpressionL = baseexpressionl
        self.baseExpressionR = baseepxressionr
