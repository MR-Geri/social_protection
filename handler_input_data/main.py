import pdfquery


if __name__ == '__main__':
    pdf = pdfquery.PDFQuery("../input_data/zarpMO(6).pdf")
    pdf.load()
    print(pdf.pq('LTTextLineHorizontal:contains("46471.6")'))
    print(pdf.pq('LTTextLineHorizontal:contains("33062.0")'))
    print(pdf.pq('LTTextBoxHorizontal:overlaps_bbox("274, 656.088, 315, 400")'))
