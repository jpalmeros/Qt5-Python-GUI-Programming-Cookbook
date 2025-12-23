import sys

from PyQt5.QtWidgets import QDialog, QApplication
from reservehotel import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.roomtypes = ['Suite', 'Super Luxury', 'Super Deluxe', 'Ordinary']
        self.addcontent()
        self.ui.pushButton.clicked.connect(self.computeRoomRent)
        self.show()
    
    def addcontent(self):
        for i in self.roomtypes:
            self.ui.comboBox.addItem(i)
    
    def computeRoomRent(self):
        dateselected = self.ui.calendarWidget.selectedDate()
        dateinstring = str(dateselected.toPyDate())
        noOfDays = self.ui.spinBox.value()
        choosenRoomType = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
        self.ui.EneteredInfo.setText('Date of reservation: ' +
                                     dateinstring +
                                     ', Number of days: ' +
                                     str(noOfDays) +
                                     '\nand Room type selected: ' +
                                     choosenRoomType
                                     )
        roomRent = 0
        if choosenRoomType == "Suite":
            roomRent = 40
        if choosenRoomType == "Super Luxury":
            roomRent = 30
        if choosenRoomType == "Super Deluxe":
            roomRent = 20
        if choosenRoomType == "Ordinary":
            roomRent = 10
        total = roomRent * noOfDays
        self.ui.RoomRentInfo.setText('Room Rent for single day for ' +
                                     choosenRoomType +
                                     ' type is $ ' +
                                     str(roomRent) +
                                     '\nTotal room rent is $ ' +
                                     str(total))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
