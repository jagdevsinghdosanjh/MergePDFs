from pypdf import PdfReader, PdfWriter
from io import BytesIO

def merge_pdfs(files):
    writer = PdfWriter()

    for file in files:
        if not file.filename.endswith('.pdf') or file.content_length == 0:
            raise ValueError(f"Invalid or empty file: {file.filename}")

        reader = PdfReader(file.stream)  # ✅ Use .stream here
        for page in reader.pages:
            writer.add_page(page)

    output_stream = BytesIO()
    writer.write(output_stream)
    output_stream.seek(0)
    return output_stream

# from pypdf import PdfReader, PdfWriter
# from io import BytesIO

# def merge_pdfs(files):
#     writer = PdfWriter()

#     for file in files:
#         reader = PdfReader(file)
#         for page in reader.pages:
#             writer.add_page(page)

#     output_stream = BytesIO()
#     writer.write(output_stream)
#     output_stream.seek(0)
#     return output_stream
