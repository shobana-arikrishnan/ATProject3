from yaml import load
from yaml.loader import SafeLoader


class YAML:

    def __init__(self, file_name):
        self.file = file_name

    # Method to read the YAML file
    def read(self):
        with open(self.file) as file:
            data = load(file, Loader=SafeLoader)
        return data