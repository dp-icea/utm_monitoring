import os
from dotenv import load_dotenv
from constant import * 
from config_file_parser import ConfigFileParser

load_dotenv()

DSS_URL = os.getenv('DSS_URL')
USS_PROVIDER_URL = os.getenv('USS_PROVIDER_URL')
TEST_PLAN_NAME = os.getenv('TEST_PLAN')

os.chdir('..')
current_path = os.getcwd()

os.chdir(current_path + QUALIFIER_DIR_PATH + QUALIFIER_TEST_PLANS_CONFIG_PATH)

test_plan_name = TEST_PLAN_NAME.split('.')[-1]
test_plan_file_parser = ConfigFileParser(test_plan_name + YAML_EXTENSION_STR)
test_plan_file_str = test_plan_file_parser.read_file()

test_plan_file_str = test_plan_file_parser.update_file_content(DSS_BASE_URL_PATTERN, DSS_URL, test_plan_file_str)
test_plan_file_str = test_plan_file_parser.update_file_content(USS_BASE_URL_PATTERN, USS_PROVIDER_URL,test_plan_file_str )
updated_test_plan_file_str = test_plan_file_parser.update_file_content(USS_LOG_BASE_URL_PATTERN, USS_PROVIDER_URL, test_plan_file_str)

test_plan_file_parser.write_file(updated_test_plan_file_str)
