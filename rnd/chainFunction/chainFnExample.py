class math():
    def __init__(self, variable):
        self.variable = variable

    def __call__(self, variable=None):
        return math(variable=variable)

    def sum(self,arg):
        return self(variable=self.variable + arg)

    def sub(self,arg):
        return self(variable=self.variable - arg)

    def mul(self,arg):
        return self(variable=self.variable * arg)

    def square(self):
        return self(variable=self.variable * self.variable)

    def my_print(self):
        print(self.variable)

a = math(2)
a.sum(3).sub(3).mul(2).square().my_print()

