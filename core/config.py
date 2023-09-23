import pathlib
import dotenv

def init_config():
    CURRENT_DIR = pathlib.Path(__file__).resolve().parent
    BASE_DIR = CURRENT_DIR.parent
    ENV_FILE_PATH = BASE_DIR / ".env"

    dotenv.read_dotenv(str(ENV_FILE_PATH))

    # print(os.environ)
