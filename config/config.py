import os

BASE_URL = os.getenv("BASE_URL", "https://the-internet.herokuapp.com")
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10"))
HEADLESS = os.getenv("HEADLESS", "True").lower() == "true"
BROWSER = os.getenv("BROWSER", "chrome")

# BASE_URL = "https://the-internet.herokuapp.com"

# DEFAULT_TIMEOUT = 10

# HEADLESS = True