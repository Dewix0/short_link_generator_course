from fastapi import FastAPI, Response , Path , HTTPException
from pydantic import BaseModel
#from services.short_link_service import ShortLinkService
from services.short_link_service import ShortLinkService
import re



app=FastAPI(title='Сервис генерации коротких ссылок', 
            description="Простенький тестовый сервис для создания коротких ссылок"
)
short_link_service=ShortLinkService()

@app.get("/health")
def health() -> str:
    """
    Тествоый эндпоинт
    
    """
    return "ok"


class PutLink(BaseModel):
    """
    Ссылка 
    """
    link:str
    
def _service_link_to_real(short_link: str) -> str:
    
    """ 
    возвращение ссылки уже с localhost
    """
    return f"http://localhost:8000/short/{short_link}"   

def is_valid_url(url): ## Проверка ссылки на корректность
    """ 
    Проверка ссылки на корректность
    
    """
    regex = re.compile(
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # Домен
        r'localhost|' # Локальный хост
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # IP-адрес (IPv4)
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # IP-адрес (IPv6)
        r'(?::\d+)?' # Порт
        r'(?:/?|[/?]\S+)$', re.IGNORECASE) # Путь

    return re.match(regex, url) is not None
    

@app.put("/link")
async def put_link(long_link:PutLink) -> PutLink:
    """ 
    Метод создания короткой ссылки по длинной
    """

    short_link = await short_link_service.put_link(long_link.link)
    return PutLink(link=_service_link_to_real(short_link))


@app.get("/short/{link}")
async def get_link(link:str=Path(...)) -> Response:
    """ 
    Метод переадресации с короткой ссылки на длинную
    """
    
    long_link = await short_link_service.get_long_link(link)

    if is_valid_url(long_link) is None:
        raise HTTPException(
            status_code=400,
            detail="Вы ввели некорректную ссылку , либо такого сайта не существует"
                            ) 
    
    if long_link is None:
        raise HTTPException(
            status_code=404,
            detail="Упс, мы не нашли эту ссылку"
                            )
    return Response(
        content=None, 
        headers={"Location": long_link},
        status_code=301
        )



