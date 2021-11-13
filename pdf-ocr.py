from pdf2image import convert_from_path
import pytesseract
import os

path = "./data/pdf_pages"
file_list = os.listdir(path)

for i, file in enumerate(file_list):
    if i >= 0:
        print(len(file_list)-1, i)
        file_path = path + "/" + file
        images = convert_from_path(file_path)
        result = ""
        for i in range(len(images)):
            result += pytesseract.image_to_string(images[i])
        open("./data/pdf_texts/" + file.strip(".pdf") + ".data", "w").write(result)
