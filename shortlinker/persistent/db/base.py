from sqlalchemy.orm import declarative_base
import uuid
from sqlalchemy import Column , Text , DateTime
from datetime import datetime , timezone

Base=declarative_base()

def _uuid4_as_str() -> str:
    return str(uuid.uuid4())

class WithID:
    __abstract__ = True
    
    id = Column(Text,default=_uuid4_as_str,primary_key=True)


class WithCreatedAt:   
    __abstract__ = True
    
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow , nullable=False)
    
class WithUpdatedAt:   
    __abstract__ = True
    
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow ,onupdate=datetime.utcnow, nullable=True)