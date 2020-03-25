class Birds:
    def __init__(self):
        self.members = ['Eagle']

    def printMembers(self):
        print('These are the known animals of the Birds class that are dangerous')
        for member in self.members:
            print('\t%s' % member)
