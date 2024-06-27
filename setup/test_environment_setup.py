import os
from dotenv import load_dotenv
from constant import * 
from config_file_parser import ConfigFileParser

load_dotenv()

QUALIFIER_ENV_CONFIG_PATH = os.getenv('QUALIFIER_ENV_CONFIG_PATH')
DEV_CONFIG_PATH = os.getenv('DEV_CONFIG_PATH')
DSS_URL = os.getenv('DSS_URL')
AUTH_URL = os.getenv('AUTH_SERVICE_URL')

os.chdir('..')
currentPath = os.getcwd()

os.chdir(currentPath + QUALIFIER_DIR_PATH + QUALIFIER_ENV_CONFIG_PATH)

# enviroment container config
dockerContainerConfigParser = ConfigFileParser(ENV_CONTAINER_CONFIG_FILE)
fileContent = dockerContainerConfigParser.readFile()

updatedFileContent = dockerContainerConfigParser.updateFileContent(DSS_USS1_BASE_URL,DSS_URL, fileContent)
updatedFileContent = dockerContainerConfigParser.updateFileContent(DSS_USS2_BASE_URL,DSS_URL, updatedFileContent)

dockerContainerConfigParser.writeFile(updatedFileContent)

#authorization service config
os.chdir(currentPath + QUALIFIER_DIR_PATH)

ussQualifierScriptParser = ConfigFileParser(USS_QUALIFIFER_SCRIPT_FILE)
ussQualifierScript = ussQualifierScriptParser.readFile()

updatedFileContent = ussQualifierScriptParser.updateFileContent(AUTH_BASE_URL,AUTH_URL, ussQualifierScript)

ussQualifierScriptParser.writeFile(updatedFileContent)