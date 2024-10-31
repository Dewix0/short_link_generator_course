from persistent.db.base import Base
from sqlalchemy import Column , Text
import uuid


"""
create table link(
    id text primary key
    
    short_link text not null uniqe
    long_link text not null 


)

"""


class Link(Base):
    __tablename__ = 'link'

    id = Column(Text,default=uuid.uuid4,primary_key=True)


    short_link = Column(Text,nullable=False, unique=True)
    long_link = Column(Text,nullable=False, unique=True)

  