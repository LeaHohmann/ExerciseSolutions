class Mammals:

    def __init__(self):
        self.members = ['Tiger', 'Rhino', 'Wolf']

    def printMembers(self):
        print('These are the known animals of the mammals class that are dangerous:')
        for member in self.members:
            print('\t%s' % member)
