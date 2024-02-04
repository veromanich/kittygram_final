import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = True if os.environ['DEBUG'].lower() == 'true' else False

print(DEBUG)
