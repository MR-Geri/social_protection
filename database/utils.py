import sqlite3
from contextlib import contextmanager

from settings import PATH_DATABASE


@contextmanager
def get_base(path: str = PATH_DATABASE, is_commit: bool = False):
    con = sqlite3.connect(path)
    try:
        sql = con.cursor()
        yield sql
    finally:
        if is_commit:
            con.commit()
        else:
            con.close()
