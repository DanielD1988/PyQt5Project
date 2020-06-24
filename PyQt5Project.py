from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout, QPushButton, QMessageBox
import sys

app = QApplication(sys.argv)#Make an instance of the QApplication

window = QWidget()#make a window
window.setWindowTitle('Simple form')

clickButton = QPushButton('Submit')#button used to submit form

layout = QFormLayout()#create layout for window
layout.addRow('First Name', QLineEdit())#add a row to the form layout with a label name and text field
layout.addRow('Last Name', QLineEdit())
layout.addRow('Phone', QLineEdit())
layout.addRow('Address', QLineEdit())

window.setLayout(layout)#Set the layout form in window
layout.addWidget(clickButton)
#function to handle event
def onClick():
    message = QMessageBox()
    message.setText('Record Added')
    message.exec_()

clickButton.clicked.connect(onClick)#When button clicked go to function
window.show()
clickButton.show()#Display clicked button

sys.exit(app.exec_())#run program
