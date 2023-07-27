# V-RegX
V-RegX is a web application that allows users to upload an image/video and get detect the vehicalas well as the number plate of the veicla and using the detections, it analyses the number plate to extract the characters of the number plate. It is an application that allows users to perfom object detection on their image and get the vehical details with just one click and th data is save in a tabular format for users' convience to use the data later.

## Features

- **User Registration** Users can upload their image and video using a simple button 
- **Number Plate Detection** This model can detect vehical as well its number plate. They can customize various settings for the poll, such as allowing multiple selections and setting an expiration date.
- **Saving the detected images** This model saves the detection images locally where users can view the image(s).
- **OCR** This model alsos performs OCR on the detected numberplate prediting the text o fthe detected number plates.
- **Save the predictions** Model after the OCR saves the predictions ina a seperate folder in a tabular format in an Excel Sheet for the users.

## Technologies Used

- **Back-end:** Flask Framework
- **Front-end:** React.js, HTML, CSS, JavaScript
- **Programming Language** Python, Tkinter
- **Object Detction** Pytorch, Python, OpenCV
- **Other Libraries and Tools:** Ultralytics, EasyOCR, YOLO

## Contribution

This project is open to contributions from anyone. If you would like to contribute, please follow the steps below:

1. Fork the repository
2. Clone the repository to your local machine
3. Create a new branch
4. Make your changes
5. Commit and push your changes to the remote repository
6. Create a pull request

## Installation

#### 1. Clone the Repository

Clone the repository from GitHub to your local machine.

```
git clone https://github.com/Rishit605/license-plate-detection-with-ocr.git
cd license-plate-detection-with-ocr
```

#### 2. Install the Required packages and dpendencies.

Make sure you install the Required packages and dependencies using:

```
pip install -r requirements.txt
```

#### 3. Call the app.py and Run.

Open up your terminal nad type this command to run the application in local host:

```
python app.py
```

This command will run the app.py file which will create a local hosting serve

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/Rishit605/license-plate-detection-with-ocr/blob/main/LICENSE)

## Contact

If you have any questions or suggestions, please feel free to contact me at [rishit.sisodia2001@gmail.com](mailto:rishit.sisodia2001@gmail.com)

## Acknowledgements

- [React.js](https://reactjs.org/)
- [Ultralytics](https://ultralytics.com/)
- [YOLOv8](https://docs.ultralytics.com/models/yolov8/)
- [Flask](https://flask.palletsprojects.com/en/2.3.x/)
- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)

## Authors

- [Rishit Sisodia](https://github.com/Rishit605)

## Support

If you like this project, please consider giving it a ⭐.
