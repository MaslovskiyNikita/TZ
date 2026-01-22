from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import joinedload
from src.infra.postgres.models import Book
from src.infra.postgres.models.author import Author
from src.infra.postgres.storage.base_storage import PostgresStorage
from src.modules.books.schemas import BookBase, BookResponse


class BookStorage(PostgresStorage[Book]):
    async def create_book(self, book: BookBase) -> Book:
        
        authors_db = []
        
        
        if book.authors:
            stmt = select(Author).where(Author.id.in_(book.authors))
            result = await self._db.execute(stmt)
            authors_db = result.scalars().unique().all()
            if len(authors_db) != len(book.authors):
                print("Some authors not found")
        
        
        book_model = Book(
            title=book.title,
            publication_year=book.publication_year,
            pages=book.pages,
            genre=book.genre,
            authors=authors_db,
        )

        self._db.add(book_model)
        await self._db.flush()
        await self._db.refresh(book_model) 
        return book_model
    

    async def read_books(self) -> Sequence[Book]:
        stmt = select(Book).options(joinedload(Book.authors))
        result = await self._db.execute(stmt)
        return result.scalars().unique().all()
