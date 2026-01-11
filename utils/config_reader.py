import configparser
import os

class ConfigReader:
    _config = None

    @classmethod
    def load_config(cls):
        if cls._config is None:
            cls._config = configparser.ConfigParser()
            config_path = os.path.join(
                os.path.dirname(__file__),
                "..",
                "config",
                "credentials.ini"
            )
            cls._config.read(config_path)

    @classmethod
    def get_password(cls, username):
        cls.load_config()
        return cls._config.get("login", username)
