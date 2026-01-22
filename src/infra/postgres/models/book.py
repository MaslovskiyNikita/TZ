from datetime import datetime
from uuid import UUID

from typing import TYPE_CHECKING

from sqlalchemy import UUID as PGUUID, text, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.postgres.models.base import Base

if TYPE_CHECKING:
    from src.infra.postgres.models.author import Author


class Book(Base):
    __tablename__ = "books"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)

    authors: Mapped[list["Author"]] = relationship(
        secondary="book_author_association", back_populates="books", lazy="joined"
    )
    publication_year: Mapped[int] = mapped_column(nullable=False)
    pages: Mapped[int] = mapped_column(nullable=False)
    genre: Mapped[str] = mapped_column(String(100), nullable=False)
