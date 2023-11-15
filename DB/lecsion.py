# PostgreSQL - Система упр БД
# Это ряд програм и инструментов позволяюший создавать БД, управлять ею и манипулировать данными внутри(CRUD)
# Postgres - сама БД объектна реалиционная то есть данные хранятся в виде таблиц имеют связ между собой

# SQL - декларативный язык структивных запосов он применяется для создание и получение данных

# =====================================================================================================

# команда для входа в БД через юзера postgres:
# sudo -u postgres psql

# команда для входа в своего юзера
# psql

# команда для выхода
# \q
# exit

# создание SUPERUSER 
# CREATE ROLE 'username' SUPERUSER LOGIN PASSWORD '1';

# изменение пароля
# ALTER USER 'username' WITHPASSWORD '1';

# создани БД

# CREATE DATABASE 'name'


# \l - список всех бд

# \du - все юзеры

# \dt - все таблицы (нужно подключиться к бд заранее)

# \d 'name' - подорбная инфа про таблицвы (нужно подключиться к бд заранее)

# \c 'name' команда для подключение к бд

# ---------------------------------------------------

# Типы полей в Postgresql

# Numeric Types(числовые типы)
    # 1. smallint(2 bytes) -> -32767 to 32767
    # 2. integer(4 bytes) -> -2.147... to 2.147...
    # 3. bigint(8 bytes) -> ...
    # 4.real (4 bytes) -> числа с плаваюшей точкой, вешественное
    # 5. double precision(8 bytes) -> real но только двойная точность
    # 6. serial(4 bytes) -> int, auto-increment 

# Character types(Символьные типы(строки))
    # 1. varchar(кол-во символов) -> если мы укажем 50 символов а заполним только 10 то остальные будут свободны, макс 255
    # 2. char(кол-во символов) -> если мы укажем 50 символов а заполним только 10 то остальные будут свободны, макс 255
    # 3. text() -> неогр кол-во символов

# Boolean Type
    # 1. boolean(1 byte) - True/False

# date -> календарная дата (год.месяц.день)

# location -> координатная точка (x, y) - (245, -12)

# enumerate types:
    # ('a', 'b', 'c')
    # CREATE TYPE <any name> AS ENUM ('Happy', 'Sad', 'Mad');

# ------------------------------------------------------------------
# Ограничение:

# 1. NOT NULL - обязателно к заполнению
# 2. UNIQUE - то что будет хранится только уникалные данные
# 3. CHECK - CHECK age > -1 Ограничение проверки на условие
# 4. PRIMARY KEY - (для установки идентификатор данных в таблице)
# 5. FOREIGN KEY - (для установки связей между таблицей)
# 6.ON DELETE - для установки поведения при удал данных котор были связ-ны



# ======================================================2-lessson=======================================================

# созд бд
# CREATE DATABASE 'name';   #recommended
# create database 'name';


# созд таблицы

# CREATE TABLE <tablename> (
#     <column> <type> [<constraint>]
#     <column> <type> [<constraint>]

# )


# CREATE TABLE films (
#     id serial,
#     code char(5),
#     title varchar(100),
#     date date,
#     genre varchar(50),
#     budget bigint,
#     country varchar(50)
# );


# DROP TABLE <name> - удаление таблицы

# Команда для добавление данных в таблицу
# INSERT INTO <tablename> (column) VALUES (data), (data);

# INSERT INTO films (code, title, genre, budget, country) VALUES 
# ('AU56', 'Game of Throns', '2015-05-31', 'Fantasy', 1000000, 'USA')
# ('het5', 'Naruto', '2005-09-15', 'Fantasy', 2000000, 'Japan')



# Комонда для обновление данных
# UPDATE <table> SET <column> = <new_value> WHERE <column> = <value>;

# UPDATE films SET genre = 'Adventure' WHERE cade='het5';



# Комнда для удаление данных
# DELETE FROM <table> WHERE <column> = <value>

# 1 элемент по id(можно по name, date...)
# DELETE FROM films WHERE id=1;

# Несколько элементов по id(можно по name, date...)
# DELETE FROM films WHERE id in (2, 4, 5);



# ORDER BY - Позволяет нам сортировать выводяшие данные по убыванию или возростанию. ASC(по возростанию) и DESC(по убыванию)
# Синтаксис: SELECT <row> FROM <tablename> ORDER BY <row> [ASC/DESC];



# WHERE: исполь для филтр по полям юудут выводить только те данные котор соответ условию оперетора WHERE 
# Синтаксис- SELECT <row> FROM <tablename> WHERE <row> = 'чему либо';



# BETWEEN: условие между
# SELECT * FROM films WHERE id BETWEEN 3 and 8




# LIKE выводит результат еотор соответс введенному шаблону для строк. Чувствителен к регистру

# ILIKE - тоже самое только не зависит от регистра

# Синтаксис - SELECT <row> FROM <tablename> WHERE  <row> LIKE/ILIKE 'чему либо';


# ==============================================3-lesson=====================================================================



# Экспорт БД
# pg_dump -U <username> -d 'dbname' > 'films.sql'

# Импорт 
# psql -U <username> -d 'dbname' > -f <filename>


# ------------------------------------EXAMPLE----------------------------------
# SELECT count(product_name), c.category_name FROM products as p, categories as c WHERE p.category_id = c.category_id GROUP BY c.category_name ;
# ------------------------------------EXAMPLE----------------------------------

# ==============================================4-lesson=====================================================================

# JOIN: выборка данных из двух таблиц, соединение таблиц

# LEFT JOIN: выборка будет содержать все строки из левой таблицы

# RIGHT JOIN: выборка будет содержать все строки из правой таблицы

# SELECT p1.title, p1.price, o1.quantity, p1.price * o1.quantity as total_sum FROM products p1, orders o1 WHERE p1.id = o1.product_id;

# Запрос сразу в два таблицы


# SELECT p1.title, p1.price, o1.quantity, p1.price * o1.quantity as total_sum FROM products p1 JOIN orders o1 WHERE p1.id = o1.product_id;



