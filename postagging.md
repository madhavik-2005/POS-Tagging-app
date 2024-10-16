
# POS Tagger

A Part-of-Speech (POS) tagger is a natural language processing tool that assigns grammatical categories, or "tags," to each word in a sentence, such as nouns, verbs, adjectives, and adverbs. By analyzing the syntax of sentences, a POS tagger helps in understanding the structure and meaning of text, making it essential for various applications like machine translation, information extraction, and sentiment analysis. Modern POS taggers often utilize machine learning models to consider the context of words, allowing for more accurate tagging based on their usage. Overall, POS tagging is a crucial step in text processing that enhances the ability to analyze and interpret language effectively.


## Features

- Allows for multiple input types, such as images, PDFs, text files, and manual text.
- POS Tagging: Will process input text and assign POS tags along with definitions based on a pre-defined dictionary.
- Efficient Processing: It uses multiprocessing to process greater texts and multiple requests simultaneously.
- Execution Time Display: Shows the time taken to process the input, enhancing user experience.

## Technologies Applied
1. Streamlit: A framework to develop web applications.
2. Pillow: A library for image processing.
3. pytesseract: A tool that performs optical character recognition of an image.
4. pdfplumber: A library for extracting text from PDF files.
5. multiprocess: package with multiprocess capabilities.

## Installation
1. git clone <repository-url>
cd <repository_directory>

2. Install necessary packages: pip install -r requirements.txt

3. Running the Streamlit App 
        : streamlit run app.py

## Usage

Open the app in your web browser. Select the input type from the available options (Image, PDF, Text File, Manual Input). Provide the necessary input (image, PDF, text file, or manual text). Click the Submit button to view the POS tagging results and execution time.

## Customization 
To modify the POS tagging behavior, edit the pos_dictionary.txt file, which contains words and their corresponding POS tags. Each line should follow the 

format: word tag 

example: dog NN

## License
 This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowlegement 
 Special thanks to all the contributors and libraries which made this project possible.

## Notes for Customization:
 Repository URL: Use the actual URL of your GitHub repository and the name of the directory for <repository_url> and <repository_directory>, respectively. 
 
 License: Make sure that the license matches your project's terms. You should change the license section if you're using a different license. 
 
Additional Information: Feel free to add any other relevant sections or information to suit your needs. It will give clarity and a professional look to any individual using or contributing towards your app. Let me know if you want anything else changed!