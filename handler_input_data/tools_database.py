from handler_input_data.pdf import NotSmallBusiness
from database.utils import get_base


def add_database_not_small_business():
    """
    Обрабатывает NotSmallBusiness и заносит в ОБЩУЮ базу данных
    :return:
    """
    pdf = NotSmallBusiness()
    with get_base(is_commit=True) as base:
        for line in pdf.get_base():
            base.execute(
                """
                INSERT INTO zarpMO (id, title, reporting_month, period_from_beginning_reporting_year, last_moth, 
                last_year, beginning_reporting_period_previous_year)
                VALUES((SELECT id FROM zarpMO ORDER BY id DESC LIMIT 1) + 1, ?, ?, ?, ?, ?, ?)
                """,
                (line['title'], line['reporting_month'], line['period_from_beginning_reporting_year'],
                 line['last_moth'], line['last_year'], line['beginning_reporting_period_previous_year'])
            )


if __name__ == '__main__':
    add_database_not_small_business()
