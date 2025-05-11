import psycopg


def get_db():
    return psycopg.connect(

        dbname="fsad", user="postgres", password="admin", host="localhost", port=5432
    )
