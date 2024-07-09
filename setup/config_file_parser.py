import re

class ConfigFileParser:

    def __init__(self, file):
        self.file_name = file
    
    def read_file(self):
        return open(self.file_name, 'r').read()

    def write_file(self, content):
        file = open(self.file_name, 'w')
        return file.write(content)
    
    def update_file_content(self, pattern, content, file):
        return re.sub(pattern, content, file)