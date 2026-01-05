import sqlite3
import pathlib
import typing


def db_create(name_db: str)-> None:
    db: sqlite3.Connection = sqlite3.connect(name_db)


def table_create(name_db: str, query: str)-> None:
    db: sqlite3.Connection = sqlite3.connect(name_db)
    with db as data:
        data.execute(query)


def insert_data(name_db: str, query: list[str], placeholders: list[list[int | str]]):
    db: sqlite3.Connection = sqlite3.connect(name_db)
    with db as data:
        for value, place in zip(query, placeholders):
            data.execute(value, place)


def queries(name_db: str, query: str):
    db: sqlite3.Connection = sqlite3.connect(name_db)
    with db as data:
        return data.execute(query).fetchall()
    

def test(result: list[tuple[typing.Any]])-> None:
    data: list[tuple[int, str, int]] 
    data = [(0, 'store1', 95), (0, 'store2', 100),
            (0, 'store3', 105), (1, 'store1', 70),
            (1, 'store3', 80)]
    print(f"{'ok' if (result == data) else('fail')}")
    print(result)


def built(name_db: str)-> None:
    db_create(name_db)

    create_query: str= """CREATE TABLE Products(product_id INTEGER PRIMARY KEY,
    store1 INTEGER, store2 INTEGER, store3 INTEGER);"""
    table_create(name_db, create_query)
    
    placeholders_insert: list[list[int | str]] = [[0, 95, 100, 105], [1, 70, 80]]
    cache1: str = "INSERT INTO Products(product_id, store1, store2, store3) VALUES (?, ?, ?, ?);"
    cache2: str = "INSERT INTO Products(product_id, store1, store2, store3) VALUES (?, ?, null, ?);"
    insert_query: list[str] = [cache1, cache2]
    insert_data(name_db, insert_query, placeholders_insert)
    

def database_controller():
    name_db: str = "automatic.db"
    built(name_db)
    query: str = query_builder()
    result: list[tuple[typing.Any]] = queries(name_db, query)
    test(result)


def query_builder()-> str:
    path: str = str(pathlib.Path(__file__))[:-3] + ".sql"
    with open(path, "r") as file:
        query: str = file.read()
    return query


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        database_controller()
        __import__("atexit").register(lambda: __import__("os").remove("automatic.db"))
    else:
        built("manual.db")


    # Problem: 1795. Rearrange Products Table
    # Date: 2026-01-03
    # Link: https://leetcode.com/problems/rearrange-products-table/solutions/7461187/1795_e_postgresql-by-sharrrkkk-9rky/
    # Notes: