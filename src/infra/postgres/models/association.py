from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.infra.postgres.models.base import Base


class BookAuthorAssociation(Base):
    __tablename__ = "book_author_association"

    book_id: Mapped[UUID] = mapped_column(ForeignKey("books.id"), primary_key=True)
    author_id: Mapped[UUID] = mapped_column(ForeignKey("authors.id"), primary_key=True)
