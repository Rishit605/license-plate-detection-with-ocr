import easyocr
import os
import re
import pandas as pd

rootdir = "output\\yolov8_results\\crops\\License_Plate"


def ocr_text():
    pattern = re.compile(r"\.(jpg|png)$") # regex pattern to match file extension

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if os.path.isfile(os.path.join(subdir, file)) and pattern.search(file): # check if file is an image
                paths = os.path.join(subdir, file)
                file_paths = []
                file_names = []
                numbers = []
                
                file_paths.append(paths)
                # print(paths)
                
                init_names = os.path.split(paths)[1]
                file_names.append(file)
                
                reader = easyocr.Reader(['en'])
                text = reader.readtext(paths) ## Remeber that it takes file paths and not files.
                focused_text = text[0][1]
                numbers.append(focused_text)
            return file_paths, file_names, numbers

                
def data_tocsv():
    # Creating the Data for the Dataframe
    data = {
        "File Paths" : ocr_text()[0],
        "File Names" : ocr_text()[1],
        "Plate Number" : ocr_text()[2]
    }
    
    # Creating the Dataframe
    df = pd.DataFrame(data)
    
    # Saving the Dataframe
    df.to_csv('output/saved_csv/detection_details.csv', index=False)