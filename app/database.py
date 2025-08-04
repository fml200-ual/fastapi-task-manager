# Configuracion de la conexion a la base de datos con SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Crear el motor de la base de datos
engine = create_engine(
    settings.DATABASE_URL,
    connect_args = {"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}

)

# Crear la sesion de base de datos
SessionLocal = sessionmaker (autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Funcion para obtener la sesion de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
