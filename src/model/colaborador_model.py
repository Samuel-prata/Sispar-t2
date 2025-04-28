from src.model import db # Instância do ORM
from sqlalchemy.schema import Column # Vai transformar atributos em colunas
from sqlalchemy.types import String, DECIMAL, Integer #Vou setar os tipos de dados para as colunas

class Colaborador(db.Model): # Mapeia ai e cria a entidade
    
#----------------------------- ATRIBUTOS -------------------------
#    id INT AUTO_INCREMENT PRIMARY KEY
    id = Column(Integer, primary_key=True, autoincrement=True)
    # nome VARCHAR(100)
    nome = Column(String(100))
    email = Column(String(100))
    senha = Column(String(50))
    cargo = Column(String(100))
    salario = Column(DECIMAL(10,2))
#-------------------------------------------------------------------
    
    # Construtor
    def __init__(self, nome, email, senha, cargo, salario):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo
        self.salario = salario
# ---------------------------------------------------------------------

    def to_dict(self) -> dict:
        return {
            'email': self.email,
            'senha': self.senha
        }
        
    def all_data(self) -> dict:
        return {
            'id': self.id,
            'nome': self.nome,
            'cargo': self.cargo,
            'salario': self.salario
        }
    
    