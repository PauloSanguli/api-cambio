import PyPDF2
from Extrair_Tag.Formate_String import formate_string

class Scaning():
    number_pages = [14,25,31,34,38,41,43,45]
    text_pages = []

    pdf_read = r'C:/Users/Paulo Sanguli/Desktop/Web Scrap/Admin/ScanPDF/PDF/sistema_tritutario.pdf'
    PDF = PyPDF2.PdfFileReader(pdf_read)
    for pag in range(0,len(number_pages)):
        page = PDF.getPage(number_pages[pag])
        page_text = page.extract_text()
        texto = formate_string(str(page_text))
        text_pages.append(texto)

