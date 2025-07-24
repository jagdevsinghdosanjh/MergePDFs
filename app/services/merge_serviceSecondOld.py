from pypdf import PdfReader, PdfWriter
import os

def merge_pdfs(files):
    temp_dir = 'temp_uploads'
    os.makedirs(temp_dir, exist_ok=True)
    writer = PdfWriter()

    for file in files:
        path = os.path.join(temp_dir, file.filename)
        file.save(path)
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)

    output_path = os.path.join(temp_dir, 'merged.pdf')
    with open(output_path, 'wb') as f:
        writer.write(f)

    return output_path
