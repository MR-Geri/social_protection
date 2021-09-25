import sqlite3
from contextlib import contextmanager
from typing import Union

from settings import PATH_DATABASE


@contextmanager
def get_base(path: str, is_commit: bool = False):
    con = sqlite3.connect(path)
    try:
        sql = con.cursor()
        yield sql
    finally:
        if is_commit:
            con.commit()
        else:
            con.close()


def get_id() -> list:
    with get_base(PATH_DATABASE) as base:
        return [i[0] for i in base.execute("""SELECT id FROM article;""").fetchall()]


def add_users_post_mailing():
    with get_base(PATH_DATABASE, True) as base:
        post_id = base.execute("""SELECT id FROM article ORDER BY id DESC LIMIT 1""").fetchall()[0][0]
        for user in base.execute("""SELECT id FROM users WHERE mailing = 1""").fetchall():
            mailing_posts = str(base.execute(
                """SELECT mailing_posts FROM users WHERE id = ?""", (user[0],)).fetchall()[0][0])
            base.execute(
                f"""UPDATE users SET mailing_posts = ?  WHERE id = ?""", (f'{mailing_posts} {post_id}', user[0]))