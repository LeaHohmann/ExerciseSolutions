class Birds:
    def __init__(self):
        self.members = ['Seagull', 'Sparrow', 'Chicken']

    def printMembers(self):
        print('These are the known animals of the Birds class that are harmless:')
        for member in self.members:
            print('\t%s' % member)
