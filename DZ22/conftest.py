from dotenv import load_dotenv

load_dotenv()

pytest_plugins = ["DZ22.fixtures.page", "DZ22.fixtures.user_auth"]
