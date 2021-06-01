# Programowanie I R
# Graficzny interfejs użytkownika: PyQt - przykład

#***********************************************************************************
# Importujemy niezbędne moduły
#***********************************************************************************

# Moduł sys: do obsługi argumentów wywołania
import sys

# Pakiet PyQt: podstawowa funkcjonalność
from PyQt5.QtWidgets import *


#***********************************************************************************
# Tworzymy obiekt reprezentujący aplikację Qt
#***********************************************************************************

app = QApplication(sys.argv)


#***********************************************************************************
# Projektujemy główne okno aplikacji
#***********************************************************************************

MainForm = QWidget()
MainForm.setWindowTitle("PyQt - przykład")

lblHello = QLabel("Witaj!")

btnClickMe = QPushButton("Kliknij mnie!")

def msgButtonClick(e):
    print("Kliknięty przycisk:", e.text())

def btnClickMe_Clicked():
    msgbox = QMessageBox()
    msgbox.setText("Przycisk został kliknięty!")
    msgbox.setWindowTitle("PyQt - przykład")
    msgbox.setIcon(QMessageBox.Information)
    msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msgbox.buttonClicked.connect(msgButtonClick)
    msgbox.exec()

btnClickMe.clicked.connect(btnClickMe_Clicked)

hbox = QHBoxLayout(MainForm)
hbox.addWidget(lblHello)
hbox.addWidget(btnClickMe)

MainForm.show()


#***********************************************************************************
# Przekazujemy "sterowanie" aplikacją do biblioteki Qt
#***********************************************************************************

sys.exit(app.exec())