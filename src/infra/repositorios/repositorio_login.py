from sqlalchemy.orm import Session
from src.schemas import schemas
from src.models import models
from sqlalchemy import delete
from src.models.models import Base, engine
from sqlalchemy import delete
from src.infra.repositorios import repositorio_login

class RepositorioLogin():
    def __init__(self, db: Session):
        self.db = db
        
    def criar(self, login: schemas.Login):
        db_login = models.Login(id = login.id, nome = login.nome,  senha = login.senha )
        self.db.add(db_login)
        self.db.commit()
        self.db.refresh(db_login)
        return db_login
    
    def listar(self):
        login = self.db.query(models.Login).all()
        return login
    
    def listar_id(self, id:int):
        login = self.db.query(models.Login).filter(models.Login.id == id).first()
        return login
    
    def remover(self, id:int):
        delete_login = delete(models.Login).where(models.Login.id == id)
        self.db.execute(delete_login)
        self.db.commit()