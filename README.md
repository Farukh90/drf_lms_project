# Проект "ЛМС"

## Описание:
Проект для продаж курсов

### проверка селери бит на виндовс:
celery -A config beat --loglevel=info

### проверка селери воркер чере пул соло(только так получилось запустить) на виндовс:
celery -A config worker --pool=solo --loglevel=info

## Документация:
http://127.0.0.1:8000/redoc
http://127.0.0.1:8000/swagger


## Создание и запуск контейнеров
docker-compose up -d --build
