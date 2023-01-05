from pathlib import Path
import xlwings as xw
from PyPDF2 import PdfMerger, PdfReader

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]

    merger = PdfMerger()
    sheet.range("status").clear_contents()
    source_dir = sheet.range("source").value
    output_name = sheet.range("output").value + ".pdf"
    pdf_files = list(Path(source_dir).glob("*.pdf"))

    for pdf_file in pdf_files:
        merger.append(PdfReader(str(pdf_file), "rb"))

    output_path = str(Path(__file__).parent / output_name)
    merger.write(output_path)
    sheet.range("status").value = f"The file have been saved here: {output_path}"


if __name__ == "__main__":
    xw.Book("pdfmerger.xlsm").set_mock_caller()
    main()
