from os import environ # Acesso as variaveis de ambiente
from dotenv import load_dotenv # Recurso que vai carregar as variaveis de ambiente para o arquivo

load_dotenv() 

class Config():
    SQLALCHEMY_DATABASE_URI = environ.get('URL_DATABASE_PROD')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #Evita carregamentos desnecessários
    
