# Пет-проект на Python - Генератор коротких ссылок
##


__Используя FastApi написан генератор кортких ссылок__

1) В main.py прописан только запуск всей программы
2) Все используемые библиотеки прописаны в requirements.txt . Для их удобной загрузки можнно использовать средства виртуального окружения Python - venv.
Комманды:

__Инициальзация venv__
```
python -m venv venv
```
__Активация__
```
.\venv\scripts\activate
```

__Скачивание всех библиотек__

```
pip install requiremets.txt
```

3) Чтобы удобнее было редактировать код, а так же его просматривать , все зависимости прописаны в отдлеьных файлах


__Completed Implementations__

 1) Добавить проверку корректности введеной ссылки - регулярные выражения - DONE (app.py)

 2) описание методов в свагере - DONE (app.py)

 3) автоматическую подстановку https:// если в начале поданной ссылки нет этого протакола - DONE (short_link_service.py)

 4) Работа с базой данных sqlalchemy - DONE (persistent/db ) ( repositories)

 
