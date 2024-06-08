from pydantic import BaseModel # type: ignore
from typing import Optional
class Usuario(BaseModel):
    id: int
    nome: str
    telefone: str
    
class Produto(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    
class Config:
    orm_mode = True
    
class Pedido(BaseModel):
    id: Optional[str] = None
    quantidade: int
    entrega: bool = False
    endereco:str
    
    