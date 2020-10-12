from expression.baseexpression import BaseExpression


class Store:

    def __init__(self):
        self.database = dict()

    def store_value(self, var: str, val: BaseExpression):
        self.database[var] = val

    def get_value(self, var):
        return self.database[var]
