import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore

from evaluation import main

#from evaluation import main

class App(QWidget):

   def __init__(self):
      super().__init__()
      self.title = 'Art Style Recognition'
      self.left = 10
      self.top = 10
      self.width = 900
      self.height = 800
      self.pathToImage = ''
      self.image = QLabel(self)
      self.initUI()

   def initUI(self):
      self.setWindowTitle(self.title)
      self.setGeometry(self.left, self.top, self.width, self.height)

      # Create widget
      #image = QLabel(self)
      self.label = QLabel(self)
      pathLine = QLineEdit(self)
      pathLine.textChanged[str].connect(self.inputPathToImage)
      button = QPushButton('Get Art Style.', self)
      button.move(self.left + 730, 700)
      button.clicked.connect(self.buttonClicked)

      self.label.setGeometry(self.left, 650, self.width, 50)
      pathLine.setGeometry(self.left, 700, 700, 50)



      self.show()

   def inputPathToImage(self, text):
      self.pathToImage = str(text)


   def buttonClicked(self):
      check_load_img = False
      koef = 0.0
      new_width = 0
      new_height = 0
      try:
         pixmap = QPixmap(self.pathToImage)
         if (pixmap.width() > pixmap.height()):
            koef = 600.0 / float(pixmap.width())
            new_width = 600
            new_height = float(pixmap.height()) * koef
         else:
            koef = 600.0 / float(pixmap.height())
            new_width = float(pixmap.width()) * koef
            new_height = 600
         check_load_img = True
      except ZeroDivisionError:
         print("Bad Image Path")
      if(check_load_img):
         pixmap1 = pixmap.scaled(new_width, new_height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
         self.image.setPixmap(pixmap1)
         self.image.setGeometry(self.left, self.top, pixmap1.width(), pixmap1.height())
         self.image.show()
         answer = main("pred", self.pathToImage)
         self.label.setText(str(answer[0]))


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = App()
   sys.exit(app.exec_())
