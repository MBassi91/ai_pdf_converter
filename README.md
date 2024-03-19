
# AI-to-PDF Converter

A simple Python script for converting Adobe Illustrator (AI) files to PDF format. It's designed to process all AI files in a specified input directory and save the converted PDF files to an output directory.

## Installation

Before running the script, you must install the required Python packages. You can do this by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Usage

1. Place your AI files in the \`input_ai_files\` directory.
2. Run \`main.py\` script from the terminal:

```bash
python src/main.py
```

3. Find the converted PDF files in the \`output_pdf_files\` directory.

## Structure

- `src/converter.py`: Contains the logic for converting AI files to PDF.
- `src/main.py`: The entry point of the script, which calls the converter for all AI files in the specified input folder.
- `requirements.txt`: Lists all the necessary Python packages.
- `README.md`: This file, which provides an overview and instructions.

## Requirements

- Python 3.x
- PyMuPDF

Make sure you have Python installed on your machine and all dependencies listed in \`requirements.txt\` installed.

## Contributing

Feel free to fork the repository and submit pull requests.

---

Project created with ❤️ by Matteo
