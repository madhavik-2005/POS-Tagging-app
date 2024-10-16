import streamlit as st
from PIL import Image
import pytesseract
import pdfplumber
import re
import time  
import multiprocess as mp  # Import the multiprocess library

# Function to load the POS dictionary
def load_pos_dictionary(filename):
    pos_dict = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split()
                if len(parts) != 2:
                    st.warning(f"Skipped invalid dictionary line: {line}")
                    continue
                word, tag = parts
                pos_dict[word.lower()] = tag
    except Exception as e:
        st.error(f"Error loading POS dictionary: {e}")
    return pos_dict

# Function to get POS description
def get_pos_description(tag):
    pos_descriptions = {
        "NN": "noun", "NNS": "noun, plural", "NNP": "proper noun", "NNPS": "proper noun, plural",
        "VB": "verb, base form", "VBD": "verb, past tense", "VBG": "verb, gerund/present participle",
        "VBN": "verb, past participle", "VBP": "verb, non-3rd person singular present",
        "VBZ": "verb, 3rd person singular present",
        "JJ": "adjective", "JJR": "adjective, comparative", "JJS": "adjective, superlative",
        "RB": "adverb", "RBR": "adverb, comparative", "RBS": "adverb, superlative",
        "PRP": "personal pronoun", "PRP$": "possessive pronoun",
        "DT": "determiner", "IN": "preposition/subordinating conjunction",
        "CC": "coordinating conjunction", "CD": "cardinal number",
        "UH": "interjection", "FW": "foreign word",
        "TO": "to", "MD": "modal", "EX": "existential there",
        "WDT": "wh-determiner", "WP": "wh-pronoun", "WP$": "possessive wh-pronoun", "WRB": "wh-adverb"
    }
    return pos_descriptions.get(tag, "unknown")

# Function to process each token for POS tagging
def process_token(token, pos_dictionary):
    clean_token = re.sub(r'[^\w\s]', '', token).lower()
    tag = pos_dictionary.get(clean_token, "UNK")
    description = get_pos_description(tag) if tag != "UNK" else "unknown"
    return f"{token} : {tag} ({description})"

# Function to process the uploaded image
def process_image(image):
    img = Image.open(image)
    user_input = pytesseract.image_to_string(img)
    return user_input

# Function to process the text and generate POS tags
def process_text(input_text, pos_dictionary):
    tokens = re.findall(r'\S+', input_text)  # Split on whitespace
    with mp.Pool() as pool:  # Use multiprocess Pool
        results = pool.starmap(process_token, [(token, pos_dictionary) for token in tokens])
    return results

# Main function for Streamlit app
def main():
    st.title("POS Tagging App")
    
    # Load the POS dictionary
    pos_dictionary = load_pos_dictionary('pos_dictionary.txt')

    input_type = st.radio("Choose the input type:", ("Image", "PDF", "Text File", "Manual Input"))

    user_input = ""
    if input_type == "Image":
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            user_input = process_image(uploaded_file)

    elif input_type == "PDF":
        uploaded_file = st.file_uploader("Choose a PDF...", type="pdf")
        if uploaded_file is not None:
            with pdfplumber.open(uploaded_file) as pdf:
                text = ''
                for page in pdf.pages:
                    text += page.extract_text()
                user_input = text

    elif input_type == "Text File":
        uploaded_file = st.file_uploader("Choose a text file...", type="txt")
        if uploaded_file is not None:
            user_input = uploaded_file.read().decode("utf-8")

    elif input_type == "Manual Input":
        user_input = st.text_area("Enter the text:")

    if st.button("Submit"):
        if user_input:
            start_time = time.perf_counter()
            
            pos_results = process_text(user_input, pos_dictionary)
            execution_time = time.perf_counter() - start_time  
            
            st.subheader("POS Tagging Results")
            for result in pos_results:
                st.write(result)
            st.success(f"Execution Time: {execution_time:.6f} seconds")
        else:
            st.warning("Please provide some input.")

if __name__ == "__main__":
    main()
