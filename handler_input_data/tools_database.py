from handler_input_data.pdf import NotSmallBusiness
from database.utils import get_base
from handler_input_data.exel import UnemployedCitizens


def add_database_not_small_business():
    """
    Обрабатывает NotSmallBusiness и заносит в ОБЩУЮ базу данных
    :return:
    """
    data = NotSmallBusiness()
    with get_base(is_commit=True) as base:
        for line in data.get_base():
            base.execute(
                """
                INSERT INTO zarpMO (id, title, reporting_month, period_from_beginning_reporting_year, last_moth, 
                last_year, beginning_reporting_period_previous_year)
                VALUES((SELECT id FROM zarpMO ORDER BY id DESC LIMIT 1) + 1, ?, ?, ?, ?, ?, ?)
                """,
                (line['title'], line['reporting_month'], line['period_from_beginning_reporting_year'],
                 line['last_moth'], line['last_year'], line['beginning_reporting_period_previous_year'])
            )


def add_database_unemployed_citizens():
    """
    Обрабатывает UnemployedCitizens и заносит в ОБЩУЮ базу данных
    :return:
    """
    data = UnemployedCitizens()
    with get_base(is_commit=True) as base:
        for line in data.get_base():
            base.execute(
                """
                INSERT INTO unemployed_citizens (id, title, size)
                VALUES((SELECT id FROM unemployed_citizens ORDER BY id DESC LIMIT 1) + 1, ?, ?)
                """, (line['title'], line['size'])
            )


if __name__ == '__main__':
    pass
