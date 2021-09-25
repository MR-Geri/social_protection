from typing import List

import pdfquery
from pdfquery.cache import FileCache


class NotSmallBusiness:
    """
    Среднемесячная начисленная заработная плата работников организаций, не относящихся к субъектам
    малого предпринимательства, средняя численность работников которых превышает 15 человек,
    по городским округам и муниципальным районам Удмуртской Республики за январь – июнь 2021 года, рублей
    :return:
    """
    def __init__(self):
        self.pdf = pdfquery.PDFQuery("../input_data/zarpMO(4).pdf")
        self.pdf.load()
        #
        self.title = self.pdf.pq('LTTextBoxHorizontal:overlaps_bbox("47.906, 656.118, 205.134, 300")')[0][1:]
        self.reporting_month = self.pdf.pq('LTTextBoxHorizontal:overlaps_bbox("274, 656.088, 315, 300")')[0]
        self.period_from_beginning_reporting_year = self.pdf.pq(
            'LTTextBoxHorizontal:overlaps_bbox("339.704, 656.118, 378.326, 300")'
        )[0]
        self.last_moth = self.pdf.pq('LTTextBoxHorizontal:overlaps_bbox("400.11, 656.118, 427.731, 300")')[0]
        self.last_year = self.pdf.pq('LTTextBoxHorizontal:overlaps_bbox("471.09, 656.118, 498.622, 666.011")')[0]
        self.beginning_reporting_period_previous_year = self.pdf.pq(
            f'LTTextBoxHorizontal:overlaps_bbox("543.713, 656.118, 571.245, 300")'
        )[0]

    def get_base(self) -> List[dict]:
        data = []
        for i in range(len(self.title)):
            data.append(
                {
                    'Название': self.title[i],
                    'Отчетный месяц': self.reporting_month[i],
                    'Период с начала отчетного года': self.period_from_beginning_reporting_year[i],
                    'Темпы роста (снижения), в % отчетного месяца к предыдущему месяцу':
                        self.last_moth[i],
                    'Темпы роста (снижения), в % отчетного месяца соответствующему месяцу предыдущего года':
                        self.last_year[i],
                    'Темпы роста (снижения), в % '
                    'периода с начала отчетного года к соответствующему периоду предыдущего года':
                        self.beginning_reporting_period_previous_year[i]
                }
            )
        return data

    def print(self):
        for i in range(len(self.title)):
            print(self.title[i].text,
                  self.reporting_month[i].text,
                  self.period_from_beginning_reporting_year[i].text,
                  self.last_moth[i].text,
                  self.last_year[i].text,
                  self.beginning_reporting_period_previous_year[i].text)


class ValueSubsistenceMinimum:
    def __init__(self):
        self.pdf = pdfquery.PDFQuery("../input_data/Величина прожиточного минимума УР в 2001- 2020.pdf",
                                     parse_tree_cacher=FileCache("/tmp/"))
        self.pdf.load()
        #

    def print(self) -> None:
        print(self.pdf.pq('LTTextLineHorizontal:contains("1115")'))
        print(self.pdf.pq('LTTextBoxHorizontal:overlaps_bbox("190.1, 714.469, 212.66, 100")'))
        for i in self.pdf.pq('LTTextBoxHorizontal:overlaps_bbox("190.1, 714.469, 212.66, 724.429")'):
            for el in i:
                print(el.text)
        # print(self.pdf.pq(':overlaps_bbox("183.98, 790.023, 218.3, 798.063")'))


if __name__ == '__main__':
    ValueSubsistenceMinimum().print()
