# POS Tagging App

## Overview
The **POS Tagging App** is a web application built using **Streamlit** that enables users to perform Part-of-Speech (POS) tagging on various types of input, including images, PDFs, text files, and manual text entry. The app leverages Optical Character Recognition (OCR) to extract text from images and employs a customizable POS dictionary for tagging.

## Features
- **Multiple Input Types**: Supports input through images, PDFs, text files, and manual text.
- **POS Tagging**: Processes input text to assign POS tags and descriptions based on a predefined dictionary.
- **Efficient Processing**: Utilizes multiprocessing to handle larger texts and multiple requests simultaneously.
- **Execution Time Display**: Shows the time taken to process the input, enhancing user experience.

## Technologies Used
- [Streamlit](https://streamlit.io): A framework for building web applications.
- [Pillow](https://python-pillow.org): A library for image processing.
- [pytesseract](https://pypi.org/project/pytesseract/): An OCR tool for extracting text from images.
- [pdfplumber](https://pypi.org/project/pdfplumber/): A library for extracting text from PDF files.
- [multiprocess](https://pypi.org/project/multiprocess/): A package for multiprocessing capabilities.

## Installation
To run the app locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
2.Install Required Packages:
   pip install -r requirements.txt

3.Run the Streamlit App:
   streamlit run app.py


Usage
Open the app in your web browser.
Select the input type from the available options (Image, PDF, Text File, Manual Input).
Provide the necessary input (image, PDF, text file, or manual text).
Click the Submit button to view the POS tagging results and execution time.

Customization
To modify the POS tagging behavior, edit the pos_dictionary.txt file, which contains words and their corresponding POS tags. Each line should follow the format:
word tag
example: dog NN

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments
Special thanks to the contributors and libraries that made this project possible.

### Notes for Customization:
- **Repository URL**: Replace `<repository_url>` and `<repository_directory>` with the actual URL of your GitHub repository and the name of the directory.
- **License**: Ensure the license matches your project's terms. Adjust the license section if you are using a different license.
- **Additional Information**: Feel free to add any other relevant sections or information to suit your project needs.

This structure should provide clarity and a professional appearance for anyone using or contributing to your app. Let me know if you need any more adjustments!
