# ByteBites

Food rescue and surplus food marketplace, built with flask and mysql.

## Setup

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

1. Copy `.env.example` to `.env` and edit the values.
2. Create the mysql server with Docker for the first time. The password must match `DB_PASSWORD` in `.env`.

   ```
   docker run -d --name bytebites-db -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=bytebites -p 127.0.0.1:3306:3306 mysql:8.0
   ```

   Wait about 30 seconds for the first start. Later, start it with `docker start bytebites-db`.

   (Or you can install mysql server from https://dev.mysql.com/ and create a database named "bytebites")
3. Start the app with `flask run --debug` and open http://127.0.0.1:5000.
