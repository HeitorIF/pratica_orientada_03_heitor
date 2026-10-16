from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

class Usuarios(Base):
    __tablename__ = "Usuarios"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    nome: Mapped[String] = mapped_column(String(80))
    email: Mapped[String] = mapped_column(String(80), unique=True)

    livros: Mapped[List["Livros"]] = relationship(back_populates="usuarios")


class Livros(Base):
    __tablename__ = "Livros"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    titulo: Mapped[String] = mapped_column(String(100))
    usuario_id: Mapped[int] = mapped_column(ForeignKey("Usuarios.id"))

    usuarios: Mapped["Usuarios"] = relationship(back_populates="livros")