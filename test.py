import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

print(os.getenv('DATABASE_NAME'))  # This should print the value of DATABASE_NAME
