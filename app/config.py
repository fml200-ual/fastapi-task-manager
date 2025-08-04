from turtle import Turtle
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Configuración de la base de datos
    DATABASE_URL: str =  "sqlite:///./tasks.db" # SQLite para desarrollo

    # Configuracion de JWT
    SECRET_KEY : str = "uo8te9xVUmTUx3nrszNoGaZJ7cjI4wnOWLD625U1_Vo"
    ALGORITHM : str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Configuracion de la aplicacion
    APP_NAME: str = "Sistema de Gestion de Tareas"
    DEBUG: bool = True

    class Config:
        env_file = ".env" # Carga variables desde archivo .env

# Instancia global de configuracion
settings = Settings()

