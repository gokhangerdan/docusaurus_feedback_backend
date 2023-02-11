from datetime import datetime
from pydantic import BaseModel


class Url(BaseModel):
    url: str


class NoteBaseSchema(BaseModel):
    id: str = None
    ip: str = None
    url: str
    feedback: int
    createdAt: datetime = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
