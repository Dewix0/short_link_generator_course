from fastapi import FastAPI, Response , Path , HTTPException
import uvicorn
from pydantic import BaseModel
from services.short_link_service import ShortLinkService


# 1)Добавить проверку корректности введеной ссылки - регулярные выражения

# 2)описание методов в свагере

# 3)автоматическую подстановку https:// если в начале поданной ссылки нет этого протакола

app=FastAPI(title='Сервис генерации коротких ссылок', 
            description="Простенький тестовы  й сервис для создания коротких ссылок"\
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

@app.put("/link")
def put_link(long_link:PutLink) -> PutLink:
    """ 
    Метод создания короткой ссылки по длмнной
    """
    
    
    short_link=short_link_service.put_link(long_link.link)
    
    return PutLink(link=f'http://localhost:8000/short/{short_link}')


@app.get("/short/{short_link}")
def get_link(short_link:str=Path(...)) -> Response:
    """ 
    Метод переадресации с короткой ссылки на длинную
    """
    
    long_link = short_link_service.get_link(short_link)
    
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



