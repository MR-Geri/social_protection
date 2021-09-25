import pdfquery


if __name__ == '__main__':
    pdf = pdfquery.PDFQuery("../input_data/zarpMO(4).pdf")
    pdf.load()
    print(pdf.pq('LTTextLineHorizontal:contains("46471.6")'))
    print(pdf.pq('LTTextLineHorizontal:contains("33062.0")'))
    print(pdf.pq('LTTextLineHorizontal:contains("38162.4")'))
    data = pdf.pq('LTTextBoxHorizontal:overlaps_bbox("274, 656.088, 315, 300")')
    print(data)
    print(pdf.pq('LTTextLineHorizontal:overlaps_bbox("275.69, 272.638, 314.579, 282.598")'))
    for i in data[0]:
        print(i.text)
