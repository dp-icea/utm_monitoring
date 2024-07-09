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
current_path = os.getcwd()

os.chdir(current_path + QUALIFIER_DIR_PATH + QUALIFIER_ENV_CONFIG_PATH)

# enviroment container config
docker_container_config_parser = ConfigFileParser(ENV_CONTAINER_CONFIG_FILE)
file_content_str = docker_container_config_parser.read_file()

env_config_str = docker_container_config_parser.update_file_content(DSS_BASE_URL_PATTERN, DSS_URL, file_content_str)
env_config_str = docker_container_config_parser.update_file_content(USS_BASE_URL_PATTERN, USS_PROVIDER_URL, env_config_str)

docker_container_config_parser.write_file(env_config_str)

#authorization service config
os.chdir(current_path + QUALIFIER_DIR_PATH)

uss_qualifier_run_script_parser = ConfigFileParser(USS_QUALIFIFER_SCRIPT_FILE)
uss_qualifier_script_str = uss_qualifier_run_script_parser.read_file()
updated_script_str = uss_qualifier_run_script_parser.update_file_content(AUTH_BASE_URL,AUTH_SERVICE_URL, uss_qualifier_script_str)

uss_qualifier_run_script_parser.write_file(updated_script_str)