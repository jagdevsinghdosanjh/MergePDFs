from pypdf import PdfReader, PdfWriter
import os

def merge_pdfs(files):
    temp_dir = '/tmp'  # Required for write access on Vercel
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
