from sqlalchemy.orm import Session
from src.schemas import schemas
from src.models import models
from sqlalchemy import delete
from src.models.models import Base, engine
from sqlalchemy import delete
from src.infra.repositorios import repositorio_mensagem

class RepositorioMensagem():
    def __init__(self, db: Session):
        self.db = db
        
    def criar(self, mensagem: schemas.Mensagem):
        db_mensagem = models.Mensagem(id = mensagem.id, mensagem = mensagem.mensagem)
        self.db.add(db_mensagem)
        self.db.commit()
        self.db.refresh(db_mensagem)
        return db_mensagem
    
    def listar(self):
        mensagem = self.db.query(models.Mensagem).all()
        return mensagem
    
    def listar_id(self, id:int):
        mensagem = self.db.query(models.Mensagem).filter(models.Mensagem.id == id).first()
        return mensagem
    
    def remover(self, id:int):
        delete_mensagem = delete(models.Mensagem).where(models.Mensagem.id == id)
        self.db.execute(delete_mensagem)
        self.db.commit()