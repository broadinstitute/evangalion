import yaml
# The EntryPlug is a global class that contains configuration information

class EntryPlug:
    def __init__(self, configfile):
        self.config = self.load(configfile)
        self.checkers = self.config['checks']

    def load(self, configfile):
        with open(configfile, 'r') as f:
            y = yaml.load(f)
        return y