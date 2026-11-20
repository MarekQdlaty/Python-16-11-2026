# baza danych - system przetwarzania i przechowywania danych
# bazy relacyjne i nierelacyjne
# sql, nosql
# mysql, postgres, MSsql, Oracle, terradata
# sqlite

import sqlite3

try:
    conn = sqlite3.connect("baza_danych.db")
    c = conn.cursor()
    print("Baza danych została podłączona")

    query = """
    CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary REAL NOT NULL);
    """

    c.execute(query)
    conn.commit()

except Exception as e:
    print("Bład:", e)
finally:
    if conn:
        conn.close()
        print("Połaczenie zostało zamknięte")

# Baza danych została podłączona
# Połaczenie zostało zamknięte
