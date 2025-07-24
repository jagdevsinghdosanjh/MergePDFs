from pypdf import PdfReader, PdfWriter
from io import BytesIO

def merge_pdfs(files):
    writer = PdfWriter()

    for file in files:
        reader = PdfReader(file)
        for page in reader.pages:
            writer.add_page(page)

    output_stream = BytesIO()
    writer.write(output_stream)
    output_stream.seek(0)
    return output_stream
