from math import floor
import os
from PyPDF2 import PdfWriter, PdfReader
def split_pdf(input_path, output_path, max_page):
    '''splits pdf files to smaller documents
    arguments:
        input_path (str): path to original pdf file
        output_path (str): path to folder where devided pdf end up
        max_page (int): max amount of pages split pdf can have
    raises:
        FileNotFoundError: raises when input path wasnt found
        TypeError: raises when wrong file extension was inputed
    returns:
        None
    '''
    if __name__=="__main__":
        if not os.path.exists(input_path):
            raise FileNotFoundError("this path doesnt exist")
        if os.path.splitext(input_path)[1] != ".pdf":
            raise TypeError("wrong file extention on inputed path")
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        pdf_input = PdfReader(open(input_path, "rb"))
        total_pages = len(pdf_input.pages)
        for i in range(floor(total_pages/max_page)+1): #ilość plików
            pdf_output = PdfWriter()
            start_page= i*max_page
            end_page = min((i+1) * max_page, total_pages)
            output_pdf_path = os.path.join(output_path, f"document_{start_page + 1}-{end_page}.pdf")
            for page_num in range(start_page, end_page):
                pdf_output.add_page(pdf_input.pages[page_num])
            with open(output_pdf_path, "wb") as final_pdf:
                pdf_output.write(final_pdf)
split_pdf(r"E:\277477\programowanie\sem 2\lista 2\10_pages.pdf", r"E:\277477\programowanie\sem 2\lista 2", 3)