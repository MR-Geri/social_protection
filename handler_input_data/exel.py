import xlrd


class UnemployedCitizens:
    """
    Численность безработных граждан по МО УР на 01.01.2021г.
    :return:
    """
    def __init__(self) -> None:
        self.word_book = xlrd.open_workbook('../input_data/Безработные на 01.01.2021.xls')
        self.sheet = self.word_book.sheet_by_index(0)
        self.column_start = 2
        self.headers = [str(cell.value) for cell in self.sheet.row(1)]
        self.title = []
        self.size = []
        self._gen()

    def generator_get_line(self):
        for i in range(self.column_start, self.sheet.nrows):
            yield self.sheet.row_values(i)

    def _gen(self) -> None:
        for i, line in enumerate(self.generator_get_line()):
            try:
                id_, title, size = line
                if not title:
                    self.title.append(id_)
                    self.size.append(size)
                else:
                    self.title.append(title)
                    self.size.append(size)
            except Exception as e:
                print(e)

    def print(self) -> None:
        for i in range(len(self.title)):
            print('Название',
                  self.title[i],
                  'Численность, чел.',
                  self.size[i])

    def get_base(self):
        data = []
        for i in range(len(self.title)):
            data.append(
                {
                    'title': self.title[i],
                    'size': self.size[i]
                }
            )
        return data


if __name__ == '__main__':
    pass
