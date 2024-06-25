from pydantic import BaseModel # type: ignore
from typing import Optional
class Usuario(BaseModel):
    id: int
    nome: str
    telefone: str
    
class Login(BaseModel):
<<<<<<< HEAD
    id: int
=======
    id: Optional[int] = None
>>>>>>> 7b4c28b9ef00b3b1618b88f6b27a9577b5bb9ed7
    nome: str
    senha: str
    
class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    
class Mensagem(BaseModel):
    id: int
    mensagem: str
    
class Config:
    orm_mode = True
    
class Pedido(BaseModel):
    id: Optional[str] = None
    quantidade: int
    entrega: bool = False
    endereco:str
    
    