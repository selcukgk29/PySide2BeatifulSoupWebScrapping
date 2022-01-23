import sys
import requests
from datetime import datetime,timedelta
from PySide2 import QtCore
from PySide2.QtGui import (QPixmap)
from PySide2.QtWidgets import *
from bs4 import BeautifulSoup
from ui_weather import Ui_MainWindow
import datetime

class WeatherWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.sehir = "istanbul"
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton_2.clicked.connect(lambda :self.showMinimized())
        self.ui.pushButton.clicked.connect(lambda :QApplication.quit())

        self.ui.pushButton_3.clicked.connect(self.click)
        self.req()
        self.submenupic()
        self.show()

    def click(self):
        self.ui.pushButton_3.setGeometry(590,480,80,51)
        self.sehir=self.ui.lineEdit.text()
        self.req()
        self.submenupic()

    def req(self):
        self.date=datetime.datetime.now()
        self.ui.day_label.setText(self.date.strftime("%A"))
        self.ui.day_dmy.setText(self.date.strftime("%d %B %Y"))
        url1="https://www.timeanddate.com/weather/turkey/"+self.sehir
        response = requests.get(url1)
        html=response.content
        soup=BeautifulSoup(html,"html.parser")
        location=soup.find("h1",{"class":"headline-banner__title"})
        self.ui.day_dmy_2.setText((location.text)[11:].strip(","))
        temp=soup.find("div",{"class":"h2"})
        self.string_temp=soup.find("p")
        hum_filter=soup.findAll("td")
        hum=(str(hum_filter[5]).strip("<td>").strip("</"))

        wind=soup.findAll("p")
        wind=str(wind[1]).strip()


        self.ui.temp_label.setText(temp.text)
        self.ui.temp_sttring.setText(self.string_temp.text)
        self.ui.wind_label_2.setText(hum)
        self.ui.wind_label.setText(wind[117:125])

        subtemp = soup.findAll("p")
        submenutemp = list()
        for i in subtemp:
            if str(i).startswith("<p>") and "°C" in str(i):
                submenutemp.append(i)

        self.ui.lowtemp.setText(str(submenutemp[2]))
        future_date_after_1day=str(self.date+timedelta(days=1))
        datetimeNew=future_date_after_1day[:10].split("-")
        da=datetime.datetime(int(datetimeNew[0]),int(datetimeNew[1]),int(datetimeNew[2]))
        self.ui.submenu_day_1.setText(da.strftime("%a"))
        self.ui.submenu_temp_1.setText(str(submenutemp[3]))

        future_date_after_2day=str(da+timedelta(days=1))
        datetimeNew2=future_date_after_2day[:10].split("-")
        da2=datetime.datetime(int(datetimeNew2[0]),int(datetimeNew2[1]),int(datetimeNew2[2]))
        self.ui.submenu_day_2.setText(da2.strftime("%a"))
        self.ui.submenu_temp_2.setText(str(submenutemp[4]))


        future_date_after_3day=str(da2+timedelta(days=1))
        datetimeNew3 = future_date_after_3day[:10].split("-")
        da3 = datetime.datetime(int(datetimeNew3[0]), int(datetimeNew3[1]), int(datetimeNew3[2]))
        self.ui.submenu_day_3.setText(da3.strftime("%a"))
        self.ui.submenu_temp_3.setText(str(submenutemp[5]))


        future_date_after_4day = str(da3 + timedelta(days=1))
        datetimeNew4 = future_date_after_4day[:10].split("-")
        da4 = datetime.datetime(int(datetimeNew4[0]), int(datetimeNew4[1]), int(datetimeNew4[2]))
        self.ui.submenu_day_5.setText(da4.strftime("%a"))
        self.ui.submenu_temp_7.setText(str(submenutemp[6]))


    def submenupic(self):

            url2 = "https://www.timeanddate.com/weather/turkey/"+self.sehir+"/ext"
            Forecastresponse = requests.get(url2)
            html = Forecastresponse.content
            soup1 = BeautifulSoup(html, "html.parser")
            state = soup1.findAll("td", {"class": "small"})
            imageState = list()
            for i in state:
                imageState.append(i)

            if str(state[0].text) == "Light mixture of precip. Breaks of sun late." or "Mixture of precip. Mostly cloudy." or "Light mixture of precip. Mostly cloudy.":
                self.ui.icon_label.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\230.png"))

            elif str(state[0].text) == "Light snow. Breaks of sun late." or "Light snow. Broken clouds.":
                self.ui.icon_label.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\179.png"))

            elif str(state[0].text) == "Sunny.":
                self.ui.icon_label.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\113.png"))

            elif str(state[0].text) == "Cloudy.":
                self.ui.icon_label.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\122.png"))

            elif str(state[0].text) == "Morning clouds.":
                self.ui.icon_label.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\116.png"))

            elif str(state[0].text) == " Snow.Cloudy.":
                self.ui.icon_label.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\338.png"))

            elif str(state[0].text) == " Mixture of precip. Mostly cloudy.":
                self.ui.icon_label.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\317.png"))

            elif str(state[0].text) == "Light snow late. Partly cloudy.":
                self.ui.icon_label.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\335.png"))

            elif str(state[0].text) == "Isolated storms late.Overcast.":
                self.ui.icon_label.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\386.png"))



            if str(state[1].text) == "Light mixture of precip. Breaks of sun late." or "Mixture of precip. Mostly cloudy." or "Light mixture of precip. Mostly cloudy.":
                self.ui.submenuicon1_1.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\230.png"))
            elif str(state[1].text) == "Light snow. Breaks of sun late." or "Light snow. Broken clouds.":
                self.ui.submenuicon1_1.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\179.png"))
            elif str(state[1].text) == "Sunny.":
                self.ui.submenuicon1_1.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\113.png"))
            elif str(state[1].text) == "Cloudy.":
                self.ui.submenuicon1_1.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\122.png"))
            elif str(state[1].text) == "Morning clouds.":
                self.ui.submenuicon1_1.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\116.png"))
            elif str(state[1].text) == " Snow.Cloudy.":
                self.ui.submenuicon1_1.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\338.png"))
            elif str(state[1].text) == " Mixture of precip. Mostly cloudy.":
                self.ui.submenuicon1_1.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\317.png"))
            elif str(state[1].text) == "Light snow late. Partly cloudy.":
                self.ui.submenuicon1_1.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\335.png"))
            elif str(state[1].text) == "Isolated storms late.Overcast.":
                self.ui.submenuicon1_1.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\386.png"))


            if str(state[2].text) == "Light mixture of precip. Breaks of sun late." or "Mixture of precip. Mostly cloudy." or "Light mixture of precip. Mostly cloudy.":
                self.ui.submenuicon1_2.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\230.png"))
            if str(state[2].text) =="Light snow. Broken clouds." or"Light snow. Breaks of sun late." or "Light snow. Broken clouds.":
                print("burda")
                self.ui.submenuicon1_2.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\179.png"))
            if str(state[2].text) == "Sunny.":
                self.ui.submenuicon1_2.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\113.png"))
            if str(state[2].text) == "Cloudy.":
                self.ui.submenuicon1_2.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\122.png"))
            if str(state[2].text) == "Morning clouds.":
                self.ui.submenuicon1_2.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\116.png"))
            if str(state[2].text) == " Snow.Cloudy.":
                self.ui.submenuicon1_2.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\338.png"))
            if str(state[2].text) == " Mixture of precip. Mostly cloudy.":
                self.ui.submenuicon1_2.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\317.png"))
            if str(state[2].text) == "Light snow. Broken clouds.":
                self.ui.submenuicon1_2.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\335.png"))
            if str(state[2].text) == "Isolated storms late.Overcast.":
                self.ui.submenuicon1_2.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\386.png"))

            if str(state[3].text) == "Light mixture of precip. Breaks of sun late." or "Mixture of precip. Mostly cloudy." or "Light mixture of precip. Mostly cloudy."or "Snow. Increasing cloudiness.":
                self.ui.submenuicon1_3.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\230.png"))
            if str(state[3].text) == "Light snow. Broken clouds." or "Light snow. Overcast.":
                print("2burda")
                self.ui.submenuicon1_3.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\179.png"))
            if str(state[3].text) == "Sunny.":
                self.ui.submenuicon1_3.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\113.png"))
            if str(state[3].text) == "Cloudy.":
                self.ui.submenuicon1_3.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\122.png"))
            if str(state[3].text) == "Morning clouds.":
                self.ui.submenuicon1_3.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\116.png"))
            if str(state[3].text) == " Snow.Cloudy.":
                self.ui.submenuicon1_3.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\338.png"))
            if str(state[3].text) == " Mixture of precip. Mostly cloudy.":
                self.ui.submenuicon1_3.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\317.png"))
            if str(state[3].text) == "Light snow late. Partly cloudy.":
                self.ui.submenuicon1_3.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\335.png"))
            if str(state[3].text) == "Isolated storms late.Overcast.":
                self.ui.submenuicon1_3.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\386.png"))
            if str(state[4].text) == "Light mixture of precip. Breaks of sun late." or "Mixture of precip. Mostly cloudy." or "Light mixture of precip. Mostly cloudy.":
                self.ui.submenuicon1_4.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\230.png"))
            if str(state[4].text) == "Light snow. Breaks of sun late." or "Light snow. Broken clouds.":
                self.ui.submenuicon1_4.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\179.png"))
            if str(state[4].text) == "Sunny.":
                self.ui.submenuicon1_4.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\113.png"))
            if str(state[4].text) == "Cloudy.":
                self.ui.submenuicon1_4.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\122.png"))
            if str(state[4].text) == "Morning clouds.":
                self.ui.submenuicon1_4.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\116.png"))
            if str(state[4].text) == " Snow.Cloudy."or"Snow. Increasing cloudiness.":
                self.ui.submenuicon1_4.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\338.png"))
            if str(state[4].text) == " Mixture of precip. Mostly cloudy.":
                self.ui.submenuicon1_4.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\317.png"))
            if str(state[4].text) == "Light snow late. Partly cloudy.":
                self.ui.submenuicon1_4.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\335.png"))
            if str(state[4].text) == "Isolated storms late.Overcast.":
                self.ui.submenuicon1_4.setPixmap(QPixmap(
                    "\\havadurumu\\picdir\\weather\\64x64\\day\\386.png"))



app=QApplication(sys.argv)
weather=WeatherWindow()
sys.exit(app.exec_())