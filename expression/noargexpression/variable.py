from expression.noargexpression.noargexpression import NoArgExpression


class Variable(NoArgExpression):

    def __init__(self, var: str):
        self.var = var

    def __str__(self):
        return '%s' % self.var

    def evaluate(self, store):
        return store.database[self.var].evaluate(store)

    def optimize(self):
        return self
