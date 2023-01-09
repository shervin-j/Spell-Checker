from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtGui, QtWidgets, uic
from tkinter import *
import sys
import re
import nltk
from nltk.corpus import words


nltk.download("words")


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main-light.ui', self) # Load the .ui file

        self.check_button.clicked.connect(self.spell_check)
        self.dark_mode_check.stateChanged.connect(self.dark_mode)
        
        self.show() # Show the GUI
    
    def spell_check(self):
        # Get user data and split it to lines
        user_text_raw = self.text_edit.toPlainText()
        user_text_lines = self.text_edit.toPlainText().splitlines()

        # Go through data line by line
        self.text_edit.setText("")
        
        if self.dark_mode_check.isChecked(): # Dark mode
            self.text_edit.setTextColor(QtGui.QColor(255, 255, 255))
        else:   # Light mode
            self.text_edit.setTextColor(QtGui.QColor(47, 54, 64))
        
        for line in user_text_lines:
            line_splitted = line.split(" ") # Break this line to words
            for word in line_splitted:
                
                if re.sub(r"[^\w]", "", word.lower()) not in words.words(): # If word is not an actual word, write it in red color
                    self.text_edit.setTextColor(QtGui.QColor(255, 0, 0)) # red
                    self.text_edit.insertPlainText(word + " ")
                    if self.dark_mode_check.isChecked(): # Dark mode
                        self.text_edit.setTextColor(QtGui.QColor(255, 255, 255))
                    else:   # Light mode
                        self.text_edit.setTextColor(QtGui.QColor(47, 54, 64))
                    # print(word)
                
                else:   # write the right words in white color
                    if self.dark_mode_check.isChecked(): # Dark mode
                        self.text_edit.setTextColor(QtGui.QColor(255, 255, 255))
                    else:   # Light mode
                        self.text_edit.setTextColor(QtGui.QColor(47, 54, 64))
                    self.text_edit.insertPlainText(word + " ")
            
            self.text_edit.insertPlainText("\n") # new line
 
    def dark_mode(self):
        if self.dark_mode_check.isChecked(): # Dark mode
            self.setStyleSheet(u"background-color: rgb(18, 30, 42);")
            self.main_label.setStyleSheet(u"color: rgb(33, 230, 193);")
            self.text_edit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                            "background-color: rgb(25, 38, 54);\n"
                                            "border: 2px dotted rgb(33, 230, 193);\n"
                                            "padding: 10;")
            self.dark_mode_check.setStyleSheet(u"color: rgb(255, 215, 23)")
            self.check_button.setStyleSheet(u"QPushButton{\n"
                                            "	background-color: rgb(33, 230, 193);\n"
                                            "	color: rgb(22, 33, 62);\n"
                                            "	border-radius: 10%\n"
                                            "}\n"
                                            "QPushButton::pressed{\n"
                                            "	background-color: rgb(233, 69, 96);\n"
                                            "	color: rgb(0, 0, 0);\n"
                                            "}")
        else:   # Light mode
            self.setStyleSheet(u"background-color: rgb(245, 246, 250);")
            self.main_label.setStyleSheet(u"color: rgb(75, 123, 236);")
            self.text_edit.setStyleSheet(u"color: rgb(47, 54, 64);\n"
                                            "background-color: rgb(241, 242, 246);\n"
                                            "border: 2px dotted rgb(75, 123, 236);\n"
                                            "padding: 10;")
            self.dark_mode_check.setStyleSheet(u"color: rgb(235, 59, 90);")
            self.check_button.setStyleSheet(u"QPushButton{\n"
                                            "	background-color: rgb(75, 123, 236);\n"
                                            "	color: rgb(235, 235, 235);\n"
                                            "	border-radius: 10%\n"
                                            "}\n"
                                            "QPushButton::pressed{\n"
                                            "	background-color: rgb(32, 191, 107);\n"
                                            "	color: rgb(0, 0, 0);\n"
                                            "}")
        self.spell_check() # after changing theme text should be checked again for color correction


app = QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec() # Start the application