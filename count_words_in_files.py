#How to count words in a PDF file
import PyPDF2
file_reader_object=open('../Downloads/Functional_Programming_in_Scala.pdf', 'r')
pdf_file_object=PyPDF2.PdfFileReader(file_reader_object)
number_of_pages=pdf_file_object.getNumPages()
print(number_of_pages)
first_page=pdf_file_object.getPage(50)
page_content=first_page.extractText()
print(page_content)
file_reader_object.close()

