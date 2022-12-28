from PyPDF2 import PdfReader, PdfWriter

def extract_info(pdf_path):
    with open(pdf_path,'rb') as f:
        pdf_reader=PdfReader(f)
        print(len(pdf_reader.pages))

        pageone=pdf_reader.pages[0]
        print(pageone)

        text=pageone.extract_text()
        print(text)
        
        f.close()

if __name__ == '__main__':
    path = 'fitabasedatadictionary102320.pdf'
    extract_info(path)



f = open('dummy.pdf','rb')
pdf_reader= PdfReader(f)
first_page=pdf_reader.pages[0]

pdf_writer= PdfWriter()
pdf_writer.add_page(first_page)

pdf_output=open('new.pdf','wb')
pdf_writer.write(pdf_output)

f.close()
pdf_output.close()

