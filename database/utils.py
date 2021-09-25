import sqlite3
from contextlib import contextmanager
from typing import Union

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


def get_user_by_login(login: str) -> Union[None, list]:
    with get_base('database/base.sqlite') as base:
        req = base.execute("""SELECT * FROM Users WHERE login = ?;""", (login, )).fetchall()
        if req:
            return req[0]
        return
