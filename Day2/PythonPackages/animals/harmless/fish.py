class Fish:

    def __init__(self):
        self.members = ['Herring', 'Cod']

    def printMembers(self):
        print('These are the known animals of the Fish class that are harmless:')
        for member in self.members:
            print('\t%s' % member)
