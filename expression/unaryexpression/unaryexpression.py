from expression.baseexpression import BaseExpression


class UnaryExpression(BaseExpression):

    def __init__(self, baseexpression):
        self.baseExpression = baseexpression
