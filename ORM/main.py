# ORM - технология программирование благодаря которой разрабы могут исполь-ть язык прогр для взаимодействия с реляиционой базы данных (PostgreSQL, MySQL) Вместо того чтобы писать сырые запросы на операторах SQL  вы будете писать код ООП на языке прог-я. Это ускаряет разработку приложения и бд особенно на начальных этапах


from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    database='orm_db',
    user='marlen',
    password='1',
    host='localhost',
    port=5432
)

# print(db.connect())