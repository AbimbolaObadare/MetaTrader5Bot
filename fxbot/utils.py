import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


fxaccount = os.getenv("fxaccount")
fxpassword = os.getenv("fxpassword")
fxserver  = os.getenv("fxserver")

