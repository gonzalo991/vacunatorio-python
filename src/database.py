import psycopg2 as bd

conexion = bd.connect(
    user= 'postgres',
    password = 35912768,
    host='127.0.0.1',
    port='5432',
    database = 'vacunatorio'
)