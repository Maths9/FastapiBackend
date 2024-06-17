from sqlalchemy import Column, Integer, String, Float, Boolean
from src.infra.sqlalchemy.config.database import Base, engine
class Produto(Base):
    
    __tablename__ = 'produtos' 
    
    id = Column(Integer, primary_key=True, index=True, autoincrement = True)
    nome = Column(String(100))
    detalhes = Column(String(200))
    preco = Column(Float)
    disponivel = Column(Boolean)
    tamanhos = Column(String(30))
    
class Usuario(Base):
    
    __tablename__ = 'usuarios' 
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), index = True)
    telefone = Column(String(15), index = True)
    
class Mensagem(Base):
    
    __tablename__ = 'mensagens' 
    id = Column(Integer, primary_key=True, index=True)
    mensagem = Column(String(120), index = True)
   

