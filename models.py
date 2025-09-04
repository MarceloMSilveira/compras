from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from config_db import db

class Produto(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50))
    quantidade: Mapped[int] = mapped_column(Integer)