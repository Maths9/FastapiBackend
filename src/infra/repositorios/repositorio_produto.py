from sqlalchemy.orm import Session
from src.schemas import schemas
from src.models import models
from sqlalchemy import delete
from src.models.models import Base, engine
from sqlalchemy import delete
<<<<<<< HEAD:src/infra/repositorios/produto.py
=======
from src.infra.repositorios import repositorio_produto
>>>>>>> 7b4c28b9ef00b3b1618b88f6b27a9577b5bb9ed7:src/infra/repositorios/repositorio_produto.py

class RepositorioProduto():
    def __init__(self, db: Session):
        self.db = db
        
    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(id=produto.id, nome=produto.nome, detalhes=produto.detalhes, preco=produto.preco, disponivel=produto.disponivel)
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto
    
    def listar(self):
        produto = self.db.query(models.Produto).all()
        return produto
    
    
    def listar_id(self, id:int):
        produto = self.db.query(models.Produto).filter(models.Produto.id == id).first()
        return produto
    
    def remover(self, id:int):
        delete_produto = delete(models.Produto).where(models.Produto.id == id)
        self.db.execute(delete_produto)
        self.db.commit()
        
        