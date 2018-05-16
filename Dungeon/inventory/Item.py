class Item:

    def __init__(self, name):
        self.name = name

    def print_name(self):
        self.print_name('.')

    def print_name(self, end_statement):
        print(" -> A", self.name + end_statement)
