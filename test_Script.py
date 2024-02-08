from dotenv import load_dotenv
import os

# Explicitly provide the path to 'keys.env'
load_dotenv(dotenv_path='./keys.env')

# Test if environment variables are loaded
print(os.getenv('INFURA_KEY'))
