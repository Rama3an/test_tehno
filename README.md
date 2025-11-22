### Сервис по общему расчету стоимости изделий
#
### Развертывание происходит с помощью docker-compose
### Деплой сервиса:
1. docker-compose up --build
2. alembic revision --autogenerate -m "auto"
3. alembic upgrade head

Так же
нужно добавть .env файл в корень проекта и прописать два пути к бд async и sync
DATABASE_URL=postgresql+asyncpg://user:pass@db:5432/calc_db
DATABASE_URL_ALEMBIC=postgresql+psycopg2://user:pass@db:5432/calc_db


# 
Api сервиса:
1. /api/v1/calc - расччет суммы всех изделий
2. /api/v1/sort_materials - последние 10 расетов
3. /api/v1/health - чек, который проеряет работоспособность бд

#

<img width="612" height="100" alt="Снимок экрана 2025-11-22 в 18 04 30" src="https://github.com/user-attachments/assets/471aebad-6d12-4422-a2e2-fc049c5416c3" />
<img width="561" height="35" alt="Снимок экрана 2025-11-22 в 18 06 27" src="https://github.com/user-attachments/assets/30853780-e427-4537-bd97-e31f90343bd5" />

<img width="1297" height="78" alt="Снимок экрана 2025-11-22 в 18 09 35" src="https://github.com/user-attachments/assets/0bd9422a-1823-4054-92c6-8e96fc1c30d6" />
