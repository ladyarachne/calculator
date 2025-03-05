import os
from dotenv import load_dotenv
from app import App

# loading env variables from .env file
load_dotenv()

# accessing the environment variable
ENVIRONMENT = os.getenv("ENVIRONMENT" , "production")
debug_mode = os.getenv("DEBUG_MODE", "False").lower() == "true" # convert to boolean

print(f"Environment: {ENVIRONMENT}")
if debug_mode:
    print("debug mode is on")



if __name__ == "__main__":
    app = App().start()
