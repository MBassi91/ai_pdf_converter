import os
import fitz

def convert_ai_to_pdf(input_path, output_folder):
    filename = os.path.basename(input_path)
    pdf_filename = filename.replace('.ai', '.pdf')
    pdf_filepath = os.path.join(output_folder, pdf_filename)

    try:
        doc = fitz.open(input_path)
        doc.save(pdf_filepath)
        print(f"Converted '{filename}' to PDF.")
    except Exception as e:
        print(f"Error converting '{filename}': {e}")
    finally:
        if doc:
            doc.close()