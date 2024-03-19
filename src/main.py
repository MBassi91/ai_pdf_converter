import os
from converter import convert_ai_to_pdf

if __name__ == "__main__":
    input_folder = "input_ai_files"
    output_folder = "output_pdf_files"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.ai'):
            input_path = os.path.join(input_folder, filename)
            convert_ai_to_pdf(input_path, output_folder)