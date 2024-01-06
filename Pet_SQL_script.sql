DROP SCHEMA IF EXISTS human_friends;
CREATE SCHEMA human_friends;

USE human_friends;

DROP TABLE IF EXISTS dogs;
CREATE TABLE dogs (
  id_dogs SERIAL PRIMARY KEY,
  name_pet VARCHAR(20) NOT NULL,
  birthday DATE NOT NULL,
  commands TEXT NULL);

INSERT INTO dogs (name_pet, birthday, commands) VALUES
('Люси', '2012-10-12', 'ко мне, лежать'),
('Дружок', '2000-01-04', 'фу, вон'),
('Дорн', '2000-01-04', 'скули, кувырок, гавкай'),
('Саймон', '2001-11-13', 'фас, держать, назад');

SELECT * from dogs;

DROP TABLE IF EXISTS cats;
CREATE TABLE cats (
  id_cats SERIAL PRIMARY KEY,
  name_pet VARCHAR(20) NOT NULL,
  birthday DATE NOT NULL,
  commands TEXT NULL);

INSERT INTO cats (name_pet, birthday, commands) VALUES
('Буханка', '2020-08-04', 'голос, просить'),
('Перчик', '2021-11-22', 'кушать, спать'),
('Снежок', '2000-04-16', 'ко мне');

SELECT * from cats;

DROP TABLE IF EXISTS hamsters;
CREATE TABLE hamsters (
  id_hamsters SERIAL PRIMARY KEY,
  name_pet VARCHAR(20) NOT NULL,
  birthday DATE NOT NULL,
  commands TEXT NULL);
  
INSERT INTO hamsters (name_pet, birthday, commands) VALUES 
('Малыш', '2000-12-10', 'спать, бегать, прыжок'),
('Расул', '2021-08-15', 'сидеть, кувырок, грызть'),
('Скрепыш', '2023-10-01', 'пыхтеть, лежать, толчок'),
('Жмых', '2020-05-10', 'атака, служить, пищать');

SELECT * from hamsters;

DROP TABLE IF EXISTS horses;
CREATE TABLE horses (
  id_horses SERIAL PRIMARY KEY,
  name_pet VARCHAR(20) NOT NULL,
  birthday DATE NOT NULL,
  commands TEXT NULL);

INSERT INTO horses (name_pet, birthday, commands) VALUES
('Кондрат', '2003-03-01', 'гоп, шагом, тише'),
('Заблот', '2019-03-02', 'к ноге, сидеть, рысь'),
('Черныш', '2000-10-10', 'прыжок, лежать, поворот'),
('Гарсон', '2017-04-06', 'блюсти, ржать, поворот');

SELECT * from horses;

DROP TABLE IF EXISTS сamels;
CREATE TABLE сamels (
  id_сamels SERIAL PRIMARY KEY,
  name_pet VARCHAR(20) NOT NULL,
  birthday DATE NOT NULL,
  commands TEXT NULL);

INSERT INTO сamels (name_pet, birthday, commands) VALUES
('Сезон', '2023-08-11', 'удар горбом, кувырок, плевок'),
('Бархан', '2009-10-03', 'беги, стой, сиди');

SELECT * from сamels;

DROP TABLE IF EXISTS donkeys;
CREATE TABLE donkeys (
  id_donkeys SERIAL PRIMARY KEY,
  name_pet VARCHAR(20) NOT NULL,
  birthday DATE NOT NULL,
  commands TEXT NULL);

INSERT INTO donkeys (name_pet, birthday, commands) VALUES
('Сизиф', '2011-04-25', 'кушать, сидеть, спать, моргай'),
('Макар', '2017-08-12', 'пей, крутись, прыгай');

SELECT * from donkeys;

DROP TABLE IF EXISTS сamels;

DROP TABLE IF EXISTS pack_animals;
CREATE TABLE pack_animals (
  id_pack_animals SERIAL PRIMARY KEY,
  name_pet VARCHAR(20) NOT NULL,
  birthday DATE NOT NULL,
  commands TEXT NULL,
  table_name VARCHAR(20) NOT NULL,
  id_source_table VARCHAR(20) NOT NULL);

INSERT INTO pack_animals (name_pet, birthday, commands, table_name, id_source_table)
SELECT name_pet, birthday, commands, 'horses' as table_name, id_horses FROM horses 
UNION ALL
SELECT name_pet, birthday, commands, 'donkeys' as table_name, id_donkeys FROM donkeys;

SELECT * from pack_animals;

DROP TABLE IF EXISTS young_animals;
CREATE TABLE young_animals (
  id_young_animals SERIAL PRIMARY KEY,
  name_pet VARCHAR(20) NOT NULL,
  birthday DATE NOT NULL,
  commands TEXT NULL,  
  table_name VARCHAR(20) NOT NULL,
  month INT NOT NULL);
  
INSERT INTO young_animals (name_pet, birthday, commands, table_name, month)
SELECT name_pet, birthday, commands, table_name, TIMESTAMPDIFF(MONTH, birthday, NOW()) as month
FROM 
	(SELECT name_pet, birthday, commands, 'dogs' as table_name FROM dogs 
	UNION ALL
	SELECT name_pet, birthday, commands, 'cats' as table_name FROM cats 
	UNION ALL
	SELECT name_pet, birthday, commands, 'hamsters' FROM hamsters 
	UNION ALL
	SELECT name_pet, birthday, commands, 'horses' as table_name FROM horses 
	UNION ALL
	SELECT name_pet, birthday, commands, 'donkeys' as table_name FROM donkeys) as human_friends
WHERE TIMESTAMPDIFF(YEAR, birthday, NOW()) BETWEEN 1 AND 3;

SELECT * from young_animals;

DROP TABLE IF EXISTS human_friends;
CREATE TABLE human_friends (
  id_human_friends SERIAL PRIMARY KEY,
  name_pet VARCHAR(20) NOT NULL,
  birthday DATE NOT NULL,
  commands TEXT NULL,  
  table_name VARCHAR(20) NOT NULL,
  id_source_table VARCHAR(20) NOT NULL);
  
INSERT INTO human_friends (name_pet, birthday, commands, table_name, id_source_table)
SELECT name_pet, birthday, commands, 'dogs' as table_name, id_dogs FROM dogs 
UNION ALL
SELECT name_pet, birthday, commands, 'cats' as table_name, id_cats FROM cats 
UNION ALL
SELECT name_pet, birthday, commands, 'hamsters' as table_name, id_hamsters FROM hamsters 
UNION ALL
SELECT name_pet, birthday, commands, 'horses' as table_name, id_horses FROM horses 
UNION ALL
SELECT name_pet, birthday, commands, 'donkeys' as table_name, id_donkeys FROM donkeys;

SELECT * from human_friends;

DROP TABLE IF EXISTS human_another_friends;
CREATE TABLE human_another_friends (
  id_human_friends SERIAL PRIMARY KEY,
  name_pet VARCHAR(20) NOT NULL,
  birthday DATE NOT NULL,
  commands TEXT NULL,  
  table_name VARCHAR(20) NOT NULL,
  id_source_table VARCHAR(20) NOT NULL);
  
INSERT INTO human_another_friends (name_pet, birthday, commands, table_name, id_source_table)
SELECT name_pet, birthday, commands, 'dogs' as table_name, id_dogs FROM dogs 
UNION ALL
SELECT name_pet, birthday, commands, 'cats' as table_name, id_cats FROM cats 
UNION ALL
SELECT name_pet, birthday, commands, 'hamsters' as table_name, id_hamsters FROM hamsters 
UNION ALL
SELECT name_pet, birthday, commands, 'pack_animals' as table_name, id_pack_animals FROM pack_animals;

SELECT * from human_another_friends







