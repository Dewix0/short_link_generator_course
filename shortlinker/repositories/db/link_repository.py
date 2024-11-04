from persistent.db.link import Link
from infrastructure.sqlite.connect import sqlite_connection
from sqlalchemy import insert , select


class LinkRepository:
    def __init__(self)  -> None:
        self._sessionmaker = sqlite_connection()

    async def put_link(self , short_link:str , long_link:str) -> None:      
        """
        INSERT INTO link(short_link, long_link) values((short_link), (long_link))
        """
        stmp= insert(Link).values({"short_link": short_link , "long_link":long_link})

        async with self._sessionmaker() as session:
            await session.execute(stmp)
            await session.commit()

    async def get_real_link(self , short_link:str) -> str | None:
        """
        SELECT long_link FROM link WHERE short_link ={short_link} LIMIT 1

        """
        stmp=select(Link.long_link).where(Link.short_link == short_link).limit(1)

        async with self._sessionmaker() as session:
            resp = await session.execute(stmp)

        row=resp.fetchone()
        if row is None:
            return None
        
        return row[0]


