# The EntryPlug is a global class that contains configuration information

class EntryPlug:
    def __init__(self, configfile):
        self.checkers = self.load_checkers(configfile)

    def load_checkers(self, configfile):
        with open(configfile, 'r') as f:
            checkers = f.readlines()
        return [x.strip() for x in checkers]

    def load_instrumentation(self):
        # TODO
        pass