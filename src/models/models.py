from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
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
    
    id = Column(Integer, primary_key=True, index=True, autoincrement = True)
    nome = Column(String(100), index = True)
    telefone = Column(String(15), index = True, primary_key=True)
    
class Login(Base):
    
    __tablename__ = 'logins' 
    
    id = Column(Integer, primary_key=True, index=True, autoincrement = True)
    nome = Column(String(100), index = True)
    senha = Column(String(100))
   
class Mensagem(Base):
    
    __tablename__ = 'mensagens' 
    id = Column(Integer, primary_key=True, index=True, autoincrement = True)
    mensagem = Column(String(120), index = True)
   

