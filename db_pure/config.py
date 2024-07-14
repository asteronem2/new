from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    model_config = SettingsConfigDict(env_file='.env')

    def config_dict(self):
        config = {
            'DB_HOST': self.DB_HOST,
            'DB_PORT': self.DB_PORT,
            'DB_USER': self.DB_USER,
            'DB_PASS': self.DB_PASS,
            'DB_NAME': self.DB_NAME,
        }
        return config
