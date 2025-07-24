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
