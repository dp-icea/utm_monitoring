import os
import sys
from dotenv import load_dotenv
from setup.constant import * 
from setup.execute_subprocess import execute

load_dotenv()

DSS_URL = os.getenv('DSS_URL')
TEST_PLAN = os.getenv('TEST_PLAN')

current_path = os.getcwd()

os.chdir(current_path + SCRIPT_SETUP_PATH) 
execute([PYTHON3_COMMAND_LINE, ENV_COMPOSE_CONFIG_SCRIPT])
execute([PYTHON3_COMMAND_LINE, TEST_PLAN_COMPOSE_CONFIG_SCRIPT])

os.chdir(current_path + QUALIFIER_DIR_PATH)
execute([BASH_COMMAND_LINE, USS_QUALIFIFER_SCRIPT_FILE,  TEST_PLAN])

sys.exit() 
