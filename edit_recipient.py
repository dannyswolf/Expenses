# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_recipientXrhxWf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QCoreApplication, QSize, Qt, QMetaObject
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QLineEdit, QLabel, QPushButton, QSizePolicy, QWidget, QGridLayout, QMessageBox

from sql import Session, Recipients

import sys

from settings import root_logger
sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info


class Edit_recipient_window(object):
    def __init__(self, parent=None):
        super(Edit_recipient_window, self).__init__()

        self.recipient_id = None

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(504, 440)
        MainWindow.setStyleSheet(u"background-color: rgb(55, 88, 120);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.recipient_address_label = QLabel(self.centralwidget)
        self.recipient_address_label.setObjectName(u"recipient_address_label")
        self.recipient_address_label.setMinimumSize(QSize(0, 31))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recipient_address_label.setFont(font)
        self.recipient_address_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.recipient_address_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.recipient_address_label, 3, 0, 1, 1)

        self.recipient_phone_label = QLabel(self.centralwidget)
        self.recipient_phone_label.setObjectName(u"recipient_phone_label")
        self.recipient_phone_label.setMinimumSize(QSize(0, 31))
        self.recipient_phone_label.setFont(font)
        self.recipient_phone_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.recipient_phone_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.recipient_phone_label, 2, 0, 1, 1)

        self.recipient_address_edit = QLineEdit(self.centralwidget)
        self.recipient_address_edit.setObjectName(u"recipient_address_edit")
        self.recipient_address_edit.setMinimumSize(QSize(0, 31))
        self.recipient_address_edit.setMaximumSize(QSize(16777215, 16777215))
        self.recipient_address_edit.setFont(font)
        self.recipient_address_edit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.recipient_address_edit, 3, 1, 1, 1)

        self.save_recipient_btn = QPushButton(self.centralwidget)
        self.save_recipient_btn.setObjectName(u"save_recipient_btn")
        self.save_recipient_btn.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_recipient_btn.sizePolicy().hasHeightForWidth())
        self.save_recipient_btn.setSizePolicy(sizePolicy)
        self.save_recipient_btn.setMinimumSize(QSize(0, 60))
        self.save_recipient_btn.setFont(font)
        self.save_recipient_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(92, 184, 78);")
        self.save_recipient_btn.clicked.connect(lambda: self.save())
        self.save_recipient_btn.clicked.connect(MainWindow.close)

        self.gridLayout.addWidget(self.save_recipient_btn, 4, 1, 1, 1)

        self.delete_recipient_btn = QPushButton(self.centralwidget)
        self.delete_recipient_btn.setObjectName(u"delete_recipient_btn")
        self.delete_recipient_btn.setEnabled(True)
        sizePolicy.setHeightForWidth(self.delete_recipient_btn.sizePolicy().hasHeightForWidth())
        self.delete_recipient_btn.setSizePolicy(sizePolicy)
        self.delete_recipient_btn.setMinimumSize(QSize(0, 60))
        self.delete_recipient_btn.setFont(font)
        self.delete_recipient_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);")
        self.delete_recipient_btn.clicked.connect(lambda: self.delete())
        self.delete_recipient_btn.clicked.connect(MainWindow.close)
        self.gridLayout.addWidget(self.delete_recipient_btn, 4, 0, 1, 1)

        self.recipient_name_edit = QLineEdit(self.centralwidget)
        self.recipient_name_edit.setObjectName(u"recipient_name_edit")
        self.recipient_name_edit.setMinimumSize(QSize(0, 31))
        self.recipient_name_edit.setMaximumSize(QSize(16777215, 16777215))
        self.recipient_name_edit.setFont(font)
        self.recipient_name_edit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.recipient_name_edit, 1, 1, 1, 1)

        self.top_recipient_label = QLabel(self.centralwidget)
        self.top_recipient_label.setObjectName(u"top_recipient_label")
        self.top_recipient_label.setMinimumSize(QSize(0, 0))
        self.top_recipient_label.setMaximumSize(QSize(16777215, 51))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.top_recipient_label.setFont(font1)
        self.top_recipient_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(222, 148, 0);")
        self.top_recipient_label.setText(u"Επεξεργασία παραλήπτη")
        self.top_recipient_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.top_recipient_label, 0, 0, 1, 2)

        self.recipient_name_label = QLabel(self.centralwidget)
        self.recipient_name_label.setObjectName(u"recipient_name_label")
        self.recipient_name_label.setMinimumSize(QSize(0, 31))
        self.recipient_name_label.setFont(font)
        self.recipient_name_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.recipient_name_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.recipient_name_label, 1, 0, 1, 1)

        self.recipient_phone_edit = QLineEdit(self.centralwidget)
        self.recipient_phone_edit.setObjectName(u"recipient_phone_edit")
        self.recipient_phone_edit.setMinimumSize(QSize(0, 31))
        self.recipient_phone_edit.setMaximumSize(QSize(16777215, 16777215))
        self.recipient_phone_edit.setFont(font)
        self.recipient_phone_edit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.recipient_phone_edit, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.save_recipient_btn.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Επεξεργασία παραλήπτη", None))
        self.recipient_address_label.setText(QCoreApplication.translate("MainWindow", u"Διεύθυνση", None))
        self.recipient_phone_label.setText(QCoreApplication.translate("MainWindow", u"Τηλέφωνο", None))
        self.save_recipient_btn.setText(QCoreApplication.translate("MainWindow", u"Αποθήκευση", None))
        self.delete_recipient_btn.setText(QCoreApplication.translate("MainWindow", u"Διαγραφή", None))
        self.recipient_name_label.setText(QCoreApplication.translate("MainWindow", u"Ονοματεπώνυμο", None))
    # retranslateUi

    def save(self):
        recipient = Session.query(Recipients).get(self.recipient_id)
        recipient.name = self.recipient_name_edit.text()
        recipient.phone = self.recipient_phone_edit.text()
        recipient.address = self.recipient_address_edit.text()
        Session.add(recipient)
        Session.commit()
        msgBox = QMessageBox.information(None, "Πληροφορία", f"Οι αλλαγές στον {recipient.name} αποθηκεύτηκαν.")
        self.recipient_id = None

    def delete(self):
        recipient_to_delete = Session.query(Recipients).get(self.recipient_id)
        msgbox = QMessageBox(QMessageBox.Question, "Επιβεβαίωση διαγραφής", f"Είστε σήγουρος για την διαγραφή του παραλήπτη "
                                                          f"{recipient_to_delete.name};")
        msgbox.addButton(QMessageBox.Yes)
        msgbox.addButton(QMessageBox.No)
        msgbox.setDefaultButton(QMessageBox.No)
        reply = msgbox.exec()

        if reply == QMessageBox.Yes:
            Session.delete(recipient_to_delete)
            Session.commit()
            msgBox = QMessageBox.information(None, "Πληροφορία", f"Ο παραλήπτης {recipient_to_delete.name} Διαγράφτηκε.")

        else:
            return
