from expression import Addition
from expression.binaryexpression.root import Root
from expression.noargexpression.constant import Constant
from expression.noargexpression.variable import Variable
from utils.store import Store
from math import pi, e


class Controller:

    def __init__(self):
        self.store = Store()
        self._standard_variables()

    def _standard_variables(self):
        self.store.store_value('pi', Constant(pi))
        self.store.store_value('e', Constant(e))
        self.store.store_value('pythagoras', Root(Constant(2), Constant(2)))
        # self.store.store_value('golden_ratio', Multiplication(Constant(2)), Sine(Constant(54)))

    def expressions(self):
        print(Addition(Constant(2), Variable('pi')).evaluate(self.store))
