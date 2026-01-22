from uuid import UUID

from pydantic import BaseModel, ConfigDict, field_validator


class BookBase(BaseModel):
    
    
    title: str
    authors: list[UUID]
    publication_year: int
    pages: int
    genre: str

    model_config = ConfigDict(from_attributes=True)

class BookCreateRequest(BookBase):
    ...

class BookResponse(BookBase):
    id: UUID
    
    @field_validator("authors", mode="before")
    @classmethod
    def convert_authors_to_uuids(cls, value):

        if isinstance(value, list):
            return [author.id for author in value]
        return value
