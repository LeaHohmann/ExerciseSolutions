class Mammals:

    def __init__(self):
        self.members = ['Rabbit', 'Hamster']

    def printMembers(self):
        print('These are the known animals of the mammals class that are harmless:')
        for member in self.members:
            print('\t%s' % member)
