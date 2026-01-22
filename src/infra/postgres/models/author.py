from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import UUID as PGUUID, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.postgres.models.base import Base

if TYPE_CHECKING:
    from src.infra.postgres.models.book import Book


class Author(Base):
    __tablename__ = 'authors'

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    name: Mapped[str]

    books: Mapped[list["Book"]] = relationship(
        secondary="book_author_association", back_populates="authors", lazy="joined"
    )
