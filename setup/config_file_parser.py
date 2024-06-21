import re

class ConfigFileParser:

    def __init__(self, file):
        self.fileName = file
    
    def readFile(self):
        return open(self.fileName, 'r').read()

    def writeFile(self, content):
        file = open(self.fileName, 'w')
        return file.write(content)
    
    def updateFileContent(self, pattern, content, file):
        return re.sub(pattern, content, file)