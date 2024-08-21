from pydantic_settings import BaseSettings
import dotenv
import os

dotenv.load_dotenv()

class Settings(BaseSettings):
    redis_host: str = os.getenv('REDIS_HOST', '127.0.0.1')
    redis_port: str = os.getenv('REDIS_PORT', 6379)
    redis_password: str = os.getenv('REDIS_PASSWORD', 'password')
    redis_url: str = f'redis://{redis_host}:{redis_port}'

    api_key: str = os.getenv('API_KEY', 6379)


settings = Settings()