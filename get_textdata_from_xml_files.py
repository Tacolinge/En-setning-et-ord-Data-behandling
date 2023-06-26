import os
import xml.etree.ElementTree as ET
import time

folder_path = r'C:\Users\fortn\Desktop\Programmerings prosjekter\En Setning Et Ord\data-behandling\Frekvens_tekster\2019'
new_text_file = "text_to_check_frequency.txt"
# tegn = string.punctuation


def extract_text_from_xml_files(folder_path):
    text_data = []  # Liste for å lagre ren tekst fra filene

    # Gå gjennom hver fil og mappe i hovedmappen
    for root_folder, subfolders, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.xml'):
                file_path = os.path.join(root_folder, filename)

            # Åpne XML-filen og parse innholdet
            tree = ET.parse(file_path)
            root = tree.getroot()

            # Finn alle <p> og <div> tagger og hent ut ren tekst
            for element in root.iter('p'):
                if element.text:
                    text_data.append(element.text.strip())

            for element in root.iter('div'):
                if element.text:
                    text_data.append(element.text.strip())

    return text_data


def write_to_txt_file(text, new_file):
    with open(new_file, "a", encoding="utf-8") as f:
        for t in text:
            f.write(t)


def run(folder_path):
    start_timer = time.time()
    texts = extract_text_from_xml_files(folder_path)
    write_to_txt_file(texts, new_text_file)
    end_timer = time.time()
    print("completed in: ", end_timer - start_timer)


run(folder_path)
