from persistent.db.base import Base , WithID , WithCreatedAt , WithUpdatedAt
from sqlalchemy import Column , Text



"""
create table link(
    id text primary key
    
    short_link text not null uniqe
    long_link text not null 
)

"""


class Link(Base,WithID,WithCreatedAt,WithUpdatedAt):
    __tablename__ = 'link'

    short_link = Column(Text,nullable=False, unique=True)
    long_link = Column(Text,nullable=False)

  