# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_supplierpWkYFH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QCoreApplication, QSize, Qt, QRect, QMetaObject
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QLineEdit, QLabel, QMainWindow, QPushButton, QSizePolicy, QWidget, QGridLayout, QSpinBox, \
    QMessageBox

from sql import Session, Suppliers, Recipients

import sys

from settings import root_logger
sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info


class Edit_window(QMainWindow):
    def __init__(self, parent=None):
        super(Edit_window, self).__init__(parent)

        self.supplier_id = None
        self.recipient_id = None

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(504, 438)
        MainWindow.setStyleSheet(u"background-color: rgb(55, 88, 120);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.edit_label = QLabel(self.centralwidget)
        self.edit_label.setObjectName(u"edit_label")
        self.edit_label.setMinimumSize(QSize(0, 0))
        self.edit_label.setMaximumSize(QSize(16777215, 51))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.edit_label.setFont(font)
        self.edit_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(222, 148, 0);")
        # self.edit_label.setText(u"\u0395\u03c0\u03b5\u03be\u03b5\u03c1\u03b3\u03b1\u03c3\u03af\u03b1 \u03c0\u03c1\u03bf\u03bc\u03b7\u03b8\u03b5\u03c5\u03c4\u03ae")
        self.edit_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.edit_label, 0, 0, 1, 2)

        self.name_label = QLabel(self.centralwidget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setMinimumSize(QSize(0, 31))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.name_label.setFont(font1)
        self.name_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.name_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.name_label, 1, 0, 1, 1)

        self.name_edit = QLineEdit(self.centralwidget)
        self.name_edit.setObjectName(u"name_edit")
        self.name_edit.setMinimumSize(QSize(0, 31))
        self.name_edit.setMaximumSize(QSize(16777215, 16777215))
        self.name_edit.setFont(font1)
        self.name_edit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.name_edit, 1, 1, 1, 1)

        self.vat_nr_label = QLabel(self.centralwidget)
        self.vat_nr_label.setObjectName(u"vat_nr_label")
        self.vat_nr_label.setMinimumSize(QSize(0, 31))
        self.vat_nr_label.setFont(font1)
        self.vat_nr_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.vat_nr_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.vat_nr_label, 2, 0, 1, 1)

        self.vat_nr_edit = QLineEdit(self.centralwidget)
        self.vat_nr_edit.setObjectName(u"edit_vat_nr_edit")
        self.vat_nr_edit.setMinimumSize(QSize(0, 31))
        self.vat_nr_edit.setMaximumSize(QSize(16777215, 16777215))
        self.vat_nr_edit.setFont(font1)
        self.vat_nr_edit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.vat_nr_edit, 2, 1, 1, 1)

        self.phone_label = QLabel(self.centralwidget)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setMinimumSize(QSize(0, 31))
        self.phone_label.setFont(font1)
        self.phone_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.phone_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.phone_label, 3, 0, 1, 1)

        self.phone_edit = QLineEdit(self.centralwidget)
        self.phone_edit.setObjectName(u"phone_edit")
        self.phone_edit.setMinimumSize(QSize(0, 31))
        self.phone_edit.setMaximumSize(QSize(16777215, 16777215))
        self.phone_edit.setFont(font1)
        self.phone_edit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.phone_edit, 3, 1, 1, 1)

        self.address_label = QLabel(self.centralwidget)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setMinimumSize(QSize(0, 31))
        self.address_label.setFont(font1)
        self.address_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.address_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.address_label, 4, 0, 1, 1)

        self.address_edit = QLineEdit(self.centralwidget)
        self.address_edit.setObjectName(u"address_edit")
        self.address_edit.setMinimumSize(QSize(0, 31))
        self.address_edit.setMaximumSize(QSize(16777215, 16777215))
        self.address_edit.setFont(font1)
        self.address_edit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.address_edit, 4, 1, 1, 1)

        self.balance_label = QLabel(self.centralwidget)
        self.balance_label.setObjectName(u"balance_label")
        self.balance_label.setMinimumSize(QSize(0, 31))
        self.balance_label.setFont(font1)
        self.balance_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.balance_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.balance_label, 5, 0, 1, 1)

        self.balance_edit = QSpinBox(self.centralwidget)
        self.balance_edit.setObjectName(u"balance_edit")
        self.balance_edit.setMinimumSize(QSize(0, 31))
        self.balance_edit.setMaximum(9999999)
        self.balance_edit.setFont(font1)
        self.balance_edit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.balance_edit, 5, 1, 1, 1)

        self.delete_btn = QPushButton(self.centralwidget)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_btn.sizePolicy().hasHeightForWidth())
        self.delete_btn.setSizePolicy(sizePolicy)
        self.delete_btn.setMinimumSize(QSize(0, 60))
        self.delete_btn.setFont(font1)
        self.delete_btn.setStyleSheet("color: rgb(255, 255, 255);" "background-color: rgb(170, 0, 0);")

        self.gridLayout.addWidget(self.delete_btn, 6, 0, 1, 1)

        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setEnabled(True)
        sizePolicy.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy)
        self.save_btn.setMinimumSize(QSize(0, 60))
        self.save_btn.setFont(font1)
        self.save_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(92, 184, 78);")
        self.save_btn.clicked.connect(lambda: self.save())
        self.gridLayout.addWidget(self.save_btn, 6, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QMenuBar(MainWindow)
        # self.menubar.setObjectName(u"menubar")
        # self.menubar.setGeometry(QRect(0, 0, 504, 21))
        # MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"Ονοματεπώνυμο", None))

        self.phone_label.setText(QCoreApplication.translate("MainWindow", u"\u03a4\u03b7\u03bb\u03ad\u03c6\u03c9\u03bd\u03bf", None))
        self.address_label.setText(QCoreApplication.translate("MainWindow", u"\u0394\u03b9\u03b5\u03cd\u03b8\u03c5\u03bd\u03c3\u03b7", None))

        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"\u0394\u03b9\u03b1\u03b3\u03c1\u03b1\u03c6\u03ae", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"\u0391\u03c0\u03bf\u03b8\u03ae\u03ba\u03b5\u03c5\u03c3\u03b7", None))
    # retranslateUi

    def save(self):
        if self.supplier_id:

            supplier = Session.query(Suppliers).get(self.supplier_id)
            supplier.name = self.name_edit.text()
            supplier.vat_nr = self.vat_nr_edit.text()
            supplier.phone = self.phone_edit.text()
            supplier.address = self.address_edit.text()
            supplier.balance = self.balance_edit.text()
            Session.add(supplier)
            Session.commit()
            msgBox = QMessageBox.information(None, "Πληροφορία", f"Οι αλλαγές στον {supplier.name} αποθηκεύτηκαν.")


        else:
            print("recipient_id", self.recipient_id)
            recipient = Session.query(Recipients).get(self.recipient_id)
            recipient.name = self.name_edit.text()
            recipient.phone = self.phone_edit.text()
            recipient.address = self.address_edit.text()
            Session.add(recipient)
            Session.commit()
            msgBox = QMessageBox.information(None, "Πληροφορία", f"Οι αλλαγές στον {recipient.name} αποθηκεύτηκαν.")

        self.supplier_id = None
        self.recipient_id = None



