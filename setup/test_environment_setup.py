import os
from dotenv import load_dotenv
from constant import * 
from config_file_parser import ConfigFileParser

load_dotenv()

DEV_CONFIG_PATH = os.getenv('DEV_CONFIG_PATH')
DSS_URL = os.getenv('DSS_URL')
USS_PROVIDER_URL = os.getenv('USS_PROVIDER_URL')
AUTH_SERVICE_URL = os.getenv('AUTH_SERVICE_URL')

os.chdir('..')
currentPath = os.getcwd()

os.chdir(currentPath + QUALIFIER_DIR_PATH + QUALIFIER_ENV_CONFIG_PATH)

# enviroment container config
dockerContainerConfigParser = ConfigFileParser(ENV_CONTAINER_CONFIG_FILE)
fileContent = dockerContainerConfigParser.readFile()

updatedFileContent = dockerContainerConfigParser.updateFileContent(DSS_BASE_URL_PATTERN, DSS_URL, fileContent)
updatedFileContentussUpd = dockerContainerConfigParser.updateFileContent(USS_BASE_URL_PATTERN, USS_PROVIDER_URL, updatedFileContent)

dockerContainerConfigParser.writeFile(updatedFileContentussUpd)

#authorization service config
os.chdir(currentPath + QUALIFIER_DIR_PATH)

ussQualifierScriptParser = ConfigFileParser(USS_QUALIFIFER_SCRIPT_FILE)
ussQualifierScript = ussQualifierScriptParser.readFile()
updatedFileContent = ussQualifierScriptParser.updateFileContent(AUTH_BASE_URL,AUTH_SERVICE_URL, ussQualifierScript)

ussQualifierScriptParser.writeFile(updatedFileContent)