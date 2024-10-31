from utils.utils_random import random_alfnum
from repositories.db.link_repository import LinkRepository

class ShortLinkService:
    def __init__(self):
        self.link_repository = LinkRepository()  
    
    
    
    async def put_link(self,long_link:str)->str:
        
        long_link = long_link.strip()
        if not long_link.startswith(('http://', 'https://')): ## Проверка ссылки на наличие протокола
            long_link = 'https://' + long_link
        
        self.link_repository.put_link(short_link,long_link)

        short_link=random_alfnum(n=5)
        self.our_link_to_real_link[short_link]=long_link
        
        return short_link
    
    async def get_long_link(self,short_link:str) -> str | None :
        
        return await self.link_repository.get_long_link(short_link)
    
    
