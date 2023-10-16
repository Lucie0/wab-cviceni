from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from os import environ


# environmentalni promenne
DB_USERNAME = environ('DB_USERNAME', 'postgres')
DB_PASSWORD = environ('DB_PASSWORD', 'secret')
DB_SERVER = environ('DB_SERVER', 'postgres')
DB_DATABASE = environ('DB_DATABASE', 'pets_clinic')

SQLALCHEMY_DATABSE_URL = "postgresql://user:password@db/pets_clinic"