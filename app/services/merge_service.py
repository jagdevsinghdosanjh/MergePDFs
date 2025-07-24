from pypdf import PdfMerger
import os

def merge_pdfs(files):
    temp_dir = 'temp_uploads'
    os.makedirs(temp_dir, exist_ok=True)
    merger = PdfMerger()

    for file in files:
        path = os.path.join(temp_dir, file.filename)
        file.save(path)
        merger.append(path)

    output_path = os.path.join(temp_dir, 'merged.pdf')
    merger.write(output_path)
    merger.close()
    return output_path

# from pypdf import PdfReader, PdfWriter
# from io import BytesIO

# def merge_pdfs(files):
#     writer = PdfWriter()

#     for file in files:
#         if not file.filename.endswith('.pdf') or file.content_length == 0:
#             raise ValueError(f"Invalid or empty file: {file.filename}")
        
#         try:
#             reader = PdfReader(file.stream)
#             for page in reader.pages:
#                 writer.add_page(page)
#         except Exception as e:
#             raise ValueError(f"Failed to read PDF: {file.filename} — {str(e)}")

#     output_stream = BytesIO()
#     writer.write(output_stream)
#     output_stream.seek(0)
#     return output_stream
