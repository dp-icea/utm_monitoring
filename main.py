import os
import sys
from dotenv import load_dotenv
from setup.constant import * 
from setup.execute_subprocess import execute

load_dotenv()

DSS_URL = os.getenv('DSS_URL')
TEST_SUITE = os.getenv('TEST_PLAN')

currentPath = os.getcwd()

os.chdir(currentPath + '/setup') 
execute(['python3', 'test_environment_setup.py'])
    
os.chdir(currentPath + QUALIFIER_DIR_PATH) 
execute(['./' + USS_QUALIFIFER_SCRIPT_FILE, TEST_SUITE])

sys.exit() 
