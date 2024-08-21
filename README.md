# LexicomTest

**Версия Python:** 3.10.*

## Task 1:

* **Авторизация:** Добавлена авторизация через апи ключ.

### Setup Task 1

1. Скопировать .env файл:
   ```bash
   cp .env.example .env

2. Собрать и запустить докер контейнер:
   ```bash
   docker-compose up --build -d

## Task 2:

* **Sql:** Sql скрипты в task2/sql.
* **Solve:** Скрипт для генерации и записи данных в бд.

### Setup Task 2
1. Скопировать .env файл:
   ```bash
   cp .env.example .env

2. Собрать и запустить докер контейнер:
   ```bash
   docker-compose up --build -d

3. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Запуск скрипта
   ```bash
   python main.py