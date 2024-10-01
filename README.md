# postgres and containers playground

- Instanciates a PostgreSQL instance with ad database from an example schema for a dvdrental shop.
  - User: my_user
  - password: very_secret_password
- Instanciates pgadmin4 on port 8080
  - user: my_user@gmail.com
  - password: very_secret_password
- A simple python app to query the public.actor table

The database schema is taken from [here](https://www.postgresqltutorial.com/wp-content/uploads/2019/05/dvdrental.zip) and edited to make it work for this particular example

A docker-compose up should get you setup