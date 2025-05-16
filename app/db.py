import psycopg


def get_db():
    return psycopg.connect(
        dbname="fsad", user="postgres", password="admin", host="fsad_db", port=5432
    )
