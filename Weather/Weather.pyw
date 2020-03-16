import datetime
import configparser
import sys
import xml.etree.ElementTree as ET
from urllib.error import HTTPError
from datetime import date
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from urllib.request import urlopen
from PyQt5.QtWidgets import QMessageBox
from bs4 import BeautifulSoup

def get_api_key():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["openweathermap"]["api"]

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("design.ui", self)
        self.titlelbl = self.findChild(QtWidgets.QLabel, "titlelbl")
        self.imagelbl = self.findChild(QtWidgets.QLabel, "imagelbl")
        self.daylbl = self.findChild(QtWidgets.QLabel, "daylbl")
        self.weatherInfolbl = self.findChild(QtWidgets.QLabel, "weatherInfolbl")
        self.weatherInfolbl_2 = self.findChild(QtWidgets.QLabel, "weatherInfolbl_2")
        self.weatherInfolbl_3 = self.findChild(QtWidgets.QLabel, "weatherInfolbl_3")
        self.weatherInfolbl_4 = self.findChild(QtWidgets.QLabel, "weatherInfolbl_4")
        self.weatherInfolbl_5 = self.findChild(QtWidgets.QLabel, "weatherInfolbl_5")
        self.weatherInfolbl_6 = self.findChild(QtWidgets.QLabel, "weatherInfolbl_6")
        self.weatherInfolbl_7 = self.findChild(QtWidgets.QLabel, "weatherInfolbl_7")
        self.weatherInfolbl_8 = self.findChild(QtWidgets.QLabel, "weatherInfolbl_8")
        self.imagelbl = self.findChild(QtWidgets.QLabel, "imagelbl")
        self.imagelbl_2 = self.findChild(QtWidgets.QLabel, "imagelbl_2")
        self.imagelbl_3 = self.findChild(QtWidgets.QLabel, "imagelbl_3")
        self.imagelbl_4 = self.findChild(QtWidgets.QLabel, "imagelbl_4")
        self.imagelbl_5 = self.findChild(QtWidgets.QLabel, "imagelbl_5")
        self.imagelbl_6 = self.findChild(QtWidgets.QLabel, "imagelbl_6")
        self.imagelbl_7 = self.findChild(QtWidgets.QLabel, "imagelbl_7")
        self.imagelbl_8 = self.findChild(QtWidgets.QLabel, "imagelbl_8")
        self.input = self.findChild(QtWidgets.QLineEdit, "entrytxt")
        self.submitbtn = self.findChild(QtWidgets.QPushButton, "submitbtn")

        self.today = datetime.datetime.today().weekday()
        self.verifyDate = date.today()
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.daylbl.setText(f"{self.days[self.today]} - {self.days[self.today+1]}")
        self.submitbtn.clicked.connect(self.clicked)
        self.show()

    def clicked(self):
        answer = self.input.text().title()
        self.get_weather(api_key, answer)

    def get_weather(self, key, location):
        try:
            url = urlopen(f"http://api.openweathermap.org/data/2.5/forecast?q={location}&mode=xml&units=metric&appid={key}")
        except HTTPError:
            QMessageBox.about(self, "Error", "Invalid location")
            return
        self.titlelbl.setText(location)
        self.titlelbl.repaint()
        tree = ET.parse(url)
        tree = tree.getroot()
        forecast = tree.find("forecast")
        print(BeautifulSoup(ET.tostring(forecast)).prettify())
        timeFrom, timeTo, tempMax, symbolName, imgCode, humidity = ([] for i in range(6))  # assign empty value to arrays
        for item in tree.findall('.//time'):
            if len(timeFrom) == 8:
                break
            timeFrom.append(item.get('from'))
            timeTo.append(item.get('to'))
        for item in tree.findall('.//temperature'):
            if len(tempMax) == 8:
                break
            tempMax.append(item.get('max'))
        for item in tree.findall('.//symbol'):
            if len(symbolName) == 8:
                break
            symbolName.append(item.get('name'))
            imgCode.append(item.get('var'))
        for item in tree.findall('.//humidity'):
            if len(humidity) == 8:
                break
            humidity.append(item.get('value'))
        print(f"{timeFrom}\n{timeTo}\n{tempMax}\n{symbolName}\n{imgCode}\n{humidity}")

        i = 0
        while i < (len(timeFrom)):
            if "00:00:00" in timeFrom[i]:
                self.weatherInfolbl.setText(f"{symbolName[i]}\n{humidity[i]}%\n{tempMax[i]}°C")
                self.getImage(imgCode[i], 1)
            elif "03:00:00" in timeFrom[i]:
                self.weatherInfolbl_2.setText(f"{symbolName[i]}\n{humidity[i]}%\n{tempMax[i]}°C")
                self.getImage(imgCode[i], 2)
            elif "06:00:00" in timeFrom[i]:
                self.weatherInfolbl_3.setText(f"{symbolName[i]}\n{humidity[i]}%\n{tempMax[i]}°C")
                self.getImage(imgCode[i],3)
            elif "09:00:00" in timeFrom[i]:
                self.weatherInfolbl_4.setText(f"{symbolName[i]}\n{humidity[i]}%\n{tempMax[i]}°C")
                self.getImage(imgCode[i], 4)
            elif "12:00:00" in timeFrom[i]:
                self.weatherInfolbl_5.setText(f"{symbolName[i]}\n{humidity[i]}%\n{tempMax[i]}°C")
                self.getImage(imgCode[i], 5)
            elif "15:00:00" in timeFrom[i]:
                self.weatherInfolbl_6.setText(f"{symbolName[i]}\n{humidity[i]}%\n{tempMax[i]}°C")
                self.getImage(imgCode[i], 6)
            elif "18:00:00" in timeFrom[i]:
                self.weatherInfolbl_7.setText(f"{symbolName[i]}\n{humidity[i]}%\n{tempMax[i]}°C")
                self.getImage(imgCode[i], 7)
            elif "21:00:00" in timeFrom[i]:
                self.weatherInfolbl_8.setText(f"{symbolName[i]}\n{humidity[i]}%\n{tempMax[i]}°C")
                self.getImage(imgCode[i], 8)
            i += 1

    def getImage(self, imgCode, code):
        imageUrl = f"http://openweathermap.org/img/wn/{imgCode}@2x.png"
        data = urlopen(imageUrl).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        if code == 1:
            self.imagelbl = QtWidgets.QLabel(self)
            self.imagelbl.setGeometry(25, 200, 100, 100)
            self.imagelbl.setPixmap(pixmap)
            self.imagelbl.show()
        elif code == 2:
            self.imagelbl_2 = QtWidgets.QLabel(self)
            self.imagelbl_2.setGeometry(175, 200, 100, 100)
            self.imagelbl_2.setPixmap(pixmap)
            self.imagelbl_2.show()
        elif code == 3:
            self.imagelbl_3 = QtWidgets.QLabel(self)
            self.imagelbl_3.setGeometry(325, 200, 100, 100)
            self.imagelbl_3.setPixmap(pixmap)
            self.imagelbl_3.show()
        elif code == 4:
            self.imagelbl_4 = QtWidgets.QLabel(self)
            self.imagelbl_4.setGeometry(475, 200, 100, 100)
            self.imagelbl_4.setPixmap(pixmap)
            self.imagelbl_4.show()
        elif code == 5:
            self.imagelbl_5 = QtWidgets.QLabel(self)
            self.imagelbl_5.setGeometry(625, 200, 100, 100)
            self.imagelbl_5.setPixmap(pixmap)
            self.imagelbl_5.show()
        elif code == 6:
            self.imagelbl_6 = QtWidgets.QLabel(self)
            self.imagelbl_6.setGeometry(775, 200, 100, 100)
            self.imagelbl_6.setPixmap(pixmap)
            self.imagelbl_6.show()
        elif code == 7:
            self.imagelbl_7 = QtWidgets.QLabel(self)
            self.imagelbl_7.setGeometry(925, 200, 100, 100)
            self.imagelbl_7.setPixmap(pixmap)
            self.imagelbl_7.show()
        elif code == 8:
            self.imagelbl_8 = QtWidgets.QLabel(self)
            self.imagelbl_8.setGeometry(1075, 200, 100, 100)
            self.imagelbl_8.setPixmap(pixmap)
            self.imagelbl_8.show()

if __name__ == "__main__":
    api_key = get_api_key()
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
    sys.exit(app.exec_())
