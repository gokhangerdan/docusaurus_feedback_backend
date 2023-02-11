from .database import Base
from sqlalchemy import TIMESTAMP, Column, String, Integer
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE


class Note(Base):
    __tablename__ = 'notes'
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    ip = Column(String, nullable=False)
    url = Column(String, nullable=False)
    feedback = Column(Integer, nullable=False)
    createdAt = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
