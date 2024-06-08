from sqlalchemy import Column, Integer, String, Float, Boolean
from src.infra.sqlalchemy.config.database import Base
class Produto(Base):
    
    __tablename__ = 'produtos' 
    
    id = Column(Integer, primary_key=True, index=True, autoincrement = True)
    nome = Column(String)
    detalhes = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
    
class Usuario(Base):
    
    __tablename__ = 'usuarios' 
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index = True)
    telefone = Column(String, index = True)