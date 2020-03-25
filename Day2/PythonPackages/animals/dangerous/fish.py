class Fish:

    def __init__(self):
        self.members = ['Shark', 'Rockfish']

    def printMembers(self):
        print('These are the known animals of the Fish class that are dangerous:')
        for member in self.members:
            print('\t%s' % member)
