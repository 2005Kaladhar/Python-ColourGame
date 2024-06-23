
from PySide6.QtCore import (Qt,QPoint,QUrl)
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import (QApplication, QMainWindow,QGraphicsOpacityEffect)
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtTest import QTest
from random import choice
from time import time


from ui_colourGameUI import Ui_MainWindow as mainScreen
import sys

class MyApplication(QMainWindow):
    """Main UI screen Class """
    def __init__(self):
        super().__init__()
        self.ui = mainScreen()
        self.ui.setupUi(self)

        self.points = 0

    
        self.setFocusPolicy(Qt.StrongFocus)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.opacity_effect = QGraphicsOpacityEffect()

        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        self.player.setLoops(QMediaPlayer.Loops.Infinite)
        self.player.setSource(QUrl(r"backgroundMusic.mp3"))
        self.audioOutput.setVolume(5.00)
        self.player.play()


        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.closeButton.clicked.connect(self.closeWindow)
        self.ui.minimiseButton.clicked.connect(lambda : self.showMinimized())


        self.ui.volumeSlider.setValue(100)
        self.ui.volumeLabel.setText("100%")
        self.ui.bgmOnly.setChecked(True)

        
        self.ui.playButton.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(1))
        

        self.ui.bgmOnly.clicked.connect(self.music)
        self.ui.noBgm.clicked.connect(self.noMusic)
        self.ui.volumeSlider.valueChanged.connect(self.setVolume)
        self.ui.textArea.returnPressed.connect(self.check)
        self.ui.startButton.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.startButton.clicked.connect(lambda :  self.ui.frame.setStyleSheet(u"QFrame{\n"
        "\n"
        "	background-image: url(:/newPrefix/images/generalBackgroundImage.png);\n"
        "}\n"
        ""))
        self.ui.startButton.clicked.connect(self.gameLoop)

        self.ui.settingsButton.clicked.connect(self.loadSettings)
        self.ui.backtoHome.clicked.connect(lambda :self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.spellCheck.clicked.connect(self.spellToggle)
        self.checkSpellToggle = False

        self.ui.backtoHome.clicked.connect(lambda : self.ui.frame.setStyleSheet(u"QFrame{\n"
        "\n"
        "	background: none;border-radius:0px;\n"
        "}\n"
        ""))

        self.ui.windowButtonFrame.setGraphicsEffect(self.opacity_effect.setOpacity(1))

        self.timeout = 2 #Default timeout is 2 sec
        self.ui.timeout.setValue(self.timeout)
        self.ui.timeout.valueChanged.connect(self.changeTimeout)

        self.ui.windowFrame.mouseMoveEvent = self.moveWindow 
        self.rungameLoop = True
        self.txtcolor = 'black'

        self.show()

    def spellToggle(self,event):
        self.checkSpellToggle = event

    def changeTimeout(self,event):
        print(f"TimeOut Changed : {event}")
        self.timeout = event

    def gameLoop(self):
        self.cont  = True
        self.start = time()
        
        while self.rungameLoop:

            if self.cont == True:
                QApplication.processEvents()
                self.ui.pointsLabel.setText(f"Points : {self.points}")
           
                if (int(time() - self.start) == self.timeout) :
                    self.check()
         
                    print("DOne...")    
            else:
                print("Wrong input or Let's pause the game")
                break

    
    def spellCheck(self):
        txt = str(self.ui.textArea.text())
        if txt!="":
            if txt[0].lower() == 'w':
                return "white"
            elif txt[0].lower() == 'b':
                return "black"
            elif txt[0].lower() == 'r':
                return "red"
            elif txt[0].lower() == 'o':
                return "orange"
            elif txt[0].lower() == 'g':
                return "green"
            elif txt[0].lower() == 'p':
                return "pruple"
            else:
                return "No Correct Input"
        else:
                return "No Correct Input"
        
    def check(self):
        print("Text area text : ",str(self.ui.textArea.text()))
        if self.checkSpellToggle:
            toCompare = self.spellCheck()
        else:
            toCompare = str(self.ui.textArea.text()).lower()
        print("To compare : ",toCompare)


        if toCompare == str(self.txtcolor).lower():
            self.ui.textArea.clear()
            self.txtcolor = choice(["black","red","orange","yellow","white","green","purple"])
            self.txtlabel = choice(["Black","Red","Orange","Yellow","White","Green","Purple"])
            
            self.ui.colorLabel.setStyleSheet(f''' 

                    color:{self.txtcolor};
                    font: 50pt "Segoe UI";
                        
                    border-bottom-left-radius:40px;
                    border-top-right-radius:40px;
                    background:none;
                    

                    background-repeat:none;
                    background-position:centre;

                    ''') 
            self.ui.colorLabel.setText(self.txtlabel) 
            self.start = time()
            self.cont = True
            self.points += 1
        else:
            #IF the points are not zero then decrease by one otherwise it will go to negative
            if int(str(self.ui.pointsLabel.text()).split(":")[1])>0:
                self.points -= 1
                self.ui.pointsLabel.setText(f"Points : f{self.points}")
                print("Negative....")

            self.ui.textArea.clear()
            self.txtcolor = choice(["black","red","orange","yellow","white","green","purple"])
            self.txtlabel = choice(["Black","Red","Orange","Yellow","White","Green","Purple"])
            
            self.ui.colorLabel.setStyleSheet(f''' 

                    color:{self.txtcolor};
                    font: 50pt "Segoe UI";
                        
                    border-bottom-left-radius:40px;
                    border-top-right-radius:40px;
                    background:none;
                    

                    background-repeat:none;
                    background-position:centre;

                    ''') 
            self.ui.colorLabel.setText(self.txtlabel) 
            self.start = time()
            self.cont = True
            
        self.ui.textArea.clear()



    def closeWindow(self):
        self.player.stop()
        self.rungameLoop = False
        self.close()

    def music(self,event):
        self.player.setLoops(QMediaPlayer.Loops.Infinite)
        self.player.play()

    def noMusic(self,event):
        
        self.player.stop()
        self.player.setLoops(0)
        
        print(event)

    def setVolume(self,e):
        self.ui.volumeLabel.setText(f"{e}%")
        self.audioOutput.setVolume(e)

    def loadSettings(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.cont = False

    def mousePressEvent(self, event) -> None:
        self.oldPosition = event.globalPos()
    
    def moveWindow(self, event: QMouseEvent) -> None:
        delt = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delt.x() , self.y() + delt.y())
        self.oldPosition = event.globalPos();



if __name__ == '__main__':
    app = QApplication()
    window = MyApplication()
    sys.exit(app.exec())
