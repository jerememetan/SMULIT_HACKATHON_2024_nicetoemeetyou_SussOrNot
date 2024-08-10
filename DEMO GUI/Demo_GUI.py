from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QTextEdit, QGridLayout, QLabel, QFileDialog, QGraphicsOpacityEffect, QSpacerItem, QCheckBox, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStackedWidget
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()


model1 = tf.keras.models.load_model('/Users/celia/Downloads/counterfeit_model.h5')

pkl_filename = "/Users/celia/Downloads/phishing_classifier.pkl"
with open(pkl_filename, 'rb') as file:
    model2 = pickle.load(file)

vectorizer_filename = "/Users/celia/Downloads/phishing_vectorizer.pkl"
with open(vectorizer_filename, 'rb') as file:
    vectorizer = pickle.load(file)

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Sus Or Not?'
        self.resize(360,640)
        self.setStyleSheet("background-color: white;")  # Set background color to white
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.homePage()
        self.scam_or_nah()
        self.phish_or_nah()

    def homePage(self):
        self.setWindowTitle(self.title)
        self.home_page_layout = QVBoxLayout()

        self.label = QLabel(self)
        self.label.setText("Sus Or Not?")
        self.label.setStyleSheet("color: black; font-size: 30px;")  # Set text color to black and font size to 30px
        self.label.setAlignment(Qt.AlignCenter)
        self.home_page_layout.addWidget(self.label)

        self.button1 = QPushButton('Scam or Nah', self)
        self.button1.setStyleSheet("background-color: grey; color: white; border-radius: 25px; font-weight: bold")  # Set button color to grey and text color to white
        self.button1.setFixedHeight(100)  # Increase button height
        self.button1.clicked.connect(self.show_scam_or_nah)
        self.home_page_layout.addWidget(self.button1)

        self.label1 = QLabel("Use this to see how likely a product is counterfeit")
        self.label1.setStyleSheet("color: black;")
        self.label1.setAlignment(Qt.AlignCenter)
        self.home_page_layout.addWidget(self.label1)

        self.button2 = QPushButton('Phish or Nah', self)
        self.button2.setFixedHeight(100)  # Increase button height
        self.button2.setStyleSheet("background-color: grey; color: white; border-radius: 25px; font-weight: bold")  # Set button color to grey and text color to white
        self.button2.clicked.connect(self.show_phish_or_nah)
        self.home_page_layout.addWidget(self.button2)

        self.label2 = QLabel("Use this to see how likely a website is a phishing website")
        self.label2.setStyleSheet("color: black;")
        self.label2.setAlignment(Qt.AlignCenter)
        self.home_page_layout.addWidget(self.label2)

        container = QWidget()
        container.setLayout(self.home_page_layout)
        self.stacked_widget.addWidget(container)
        
    def scam_or_nah(self):

        self.scam_or_nah_layout = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText("Scam or Nah")
        self.label.setStyleSheet("color: black; font-size: 30px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.scam_or_nah_layout.addWidget(self.label)

        self.instruction_text = QLabel()
        self.instruction_text.setAlignment(Qt.AlignCenter)
        self.instruction_text.setText("Upload an image of a product listing to see how likely it is counterfeit")
        self.label.setFixedHeight(70)
        self.instruction_text.setWordWrap(True)
        self.instruction_text.setStyleSheet("color: black; font-size: 15px;")
        self.scam_or_nah_layout.addWidget(self.instruction_text)

        self.upload_button = QPushButton("Upload Image")
        self.upload_button.setStyleSheet("background-color: grey; color: white; border-radius: 25px; font-weight: bold")
        self.upload_button.setFixedHeight(100)
        self.upload_button.clicked.connect(self.openFileNameDialog)
        self.scam_or_nah_layout.addWidget(self.upload_button)

        self.upload_label = QLabel(self)
        self.upload_label.setText("No file chosen")
        self.upload_label.setStyleSheet("color: red; font-size: 15px; border: 0px")
        self.upload_label.setAlignment(Qt.AlignCenter)
        self.scam_or_nah_layout.addWidget(self.upload_label)

        self.scam_assess_button = QPushButton("Assess")
        self.scam_assess_button.setStyleSheet("background-color: grey; color: white; border-radius: 25px; font-weight: bold")
        self.scam_assess_button.setFixedHeight(100)
        self.scam_assess_button.clicked.connect(self.assess_scam)  # Connect the button to the assess_scam method
        self.scam_assess_button.setEnabled(False)  # Initially disable the button
        self.scam_or_nah_layout.addWidget(self.scam_assess_button)
        
        self.scam_score = QLineEdit()
        self.scam_score.setAlignment(Qt.AlignCenter)
        self.scam_score.setFixedHeight(70)
        self.scam_score.setText("N/A")
        self.scam_score.setStyleSheet("color: black; font-weight: bold; font-size: 15px;")
        self.scam_score.setReadOnly(True)
        self.scam_or_nah_layout.addWidget(self.scam_score)

        self.back_button = QPushButton("Back")
        self.back_button.setStyleSheet("background-color: grey; color: white; border-radius: 25px; font-weight: bold")
        self.back_button.setFixedHeight(30)
        self.back_button.clicked.connect(self.show_home_page)
        self.scam_or_nah_layout.addWidget(self.back_button)

        container = QWidget()
        container.setLayout(self.scam_or_nah_layout)
        self.stacked_widget.addWidget(container)
    
    def phish_or_nah(self):

        self.phish_or_nah_layout = QVBoxLayout()
        self.label2 = QLabel(self)
        self.label2.setText("Phish or Nah")
        self.label2.setStyleSheet("color: black; font-size: 30px;")
        self.label2.setAlignment(Qt.AlignCenter)
        self.phish_or_nah_layout.addWidget(self.label2)

        self.instruction2_text = QLabel()
        self.instruction2_text.setAlignment(Qt.AlignCenter)
        self.instruction2_text.setText("Paste a URL to see how likely it is a phishing website")
        self.label2.setFixedHeight(70)
        self.instruction2_text.setWordWrap(True)
        self.instruction2_text.setStyleSheet("color: black; font-size: 15px;")
        self.phish_or_nah_layout.addWidget(self.instruction2_text)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter URL here")
        self.url_input.setStyleSheet("color: black; font-size: 15px;")
        self.phish_or_nah_layout.addWidget(self.url_input)

        self.phish_assess_button = QPushButton("Assess")
        self.phish_assess_button.setStyleSheet("background-color: grey; color: white; border-radius: 25px; font-weight: bold")
        self.phish_assess_button.setFixedHeight(100)
        self.phish_assess_button.clicked.connect(self.assess_phish)  # Connect the button to the assess_scam method
        self.phish_or_nah_layout.addWidget(self.phish_assess_button)

        self.phish_score = QLineEdit()
        self.phish_score.setAlignment(Qt.AlignCenter)
        self.phish_score.setFixedHeight(70)
        self.phish_score.setText("N/A")
        self.phish_score.setStyleSheet("color: black; font-weight: bold; font-size: 15px;")
        self.phish_score.setReadOnly(True)
        self.phish_or_nah_layout.addWidget(self.phish_score)

        self.back_button = QPushButton("Back")
        self.back_button.setStyleSheet("background-color: grey; color: white; border-radius: 25px; font-weight: bold")
        self.back_button.setFixedHeight(30)
        self.back_button.clicked.connect(self.show_home_page)
        self.phish_or_nah_layout.addWidget(self.back_button)

        container = QWidget()
        container.setLayout(self.phish_or_nah_layout)
        self.stacked_widget.addWidget(container)

    def show_home_page(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_scam_or_nah(self):
        self.stacked_widget.setCurrentIndex(1)
    
    def show_phish_or_nah(self):
        self.stacked_widget.setCurrentIndex(2)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        self.fileName, _ = QFileDialog.getOpenFileName(None,"Choose File", "","All Files (*)", options=options)
        if self.fileName:
            self.upload_label.setText(f"Selected file: {self.fileName}")
            self.upload_label.setStyleSheet("color: red; font-size: 15px; border: 0px")
            self.upload_label.setFixedHeight(70)
            self.upload_label.setAlignment(Qt.AlignCenter)
            self.upload_label.setWordWrap(True)
            self.scam_assess_button.setEnabled(True)
    
    def assess_scam(self):
        sample_img = self.fileName
        sample_image = image.load_img(sample_img, target_size=(1028, 1028))
        sample_image = image.img_to_array(sample_image)
        sample_image = np.expand_dims(sample_image, axis=0)
        sample_image = sample_image / 255.0

        # Make predictions
        predictions = model1.predict(sample_image)
        predicted_class = np.argmax(predictions)

        if predictions[0][0] > 0.5:
            predicted_class = 1
            confidence_level = predictions[0][0] * 100
            self.scam_score.setText(f"Product is counterfeit. Probability: {round(confidence_level,2)}%")
        else:
            predicted_class = 0
            confidence_level = (1 - predictions[0][0]) * 100
            self.scam_score.setText(f"Product is authentic. Probability: {round(confidence_level,2)}%")
    
    def assess_phish(self):
        url = self.url_input.text()
        sample_url = [url]
        sample_vector = vectorizer.transform(sample_url)
        pred = model2.predict(sample_vector)
        pred_proba = model2.predict_proba(sample_vector)
        if pred[0] == 0:
            prob = pred_proba[0][0]
            self.phish_score.setText(f"Not a phishing website. Probability: {round(prob,2)} ")
        
        elif pred[0] == 1:
            prob = pred_proba[0][1]
            self.phish_score.setText(f"Phishing website. Probability: {round(prob,2)} ")
        


app = QApplication([])
ex = HomePage()
ex.show()
app.exec_()