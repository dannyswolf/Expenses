# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_paymentAGZzkI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QCoreApplication, QSize, Qt, QMetaObject, QDateTime, QDate, QTime
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QLabel, QPushButton, QSizePolicy, QWidget, QGridLayout, QSpinBox, QMessageBox, \
    QComboBox, QDateEdit, QAbstractSpinBox, QDateTimeEdit

from sql import Session, Suppliers, Payments

import sys

from settings import root_logger

sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info


class Edit_Payment_Window(object):
    def __init__(self, parent=None):
        super(Edit_Payment_Window, self).__init__()
        self.payment_id = None

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(648, 458)
        MainWindow.setStyleSheet(u"background-color: rgb(55, 88, 120);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.top_payment_label = QLabel(self.centralwidget)
        self.top_payment_label.setObjectName(u"top_payment_label")
        self.top_payment_label.setMinimumSize(QSize(0, 51))
        self.top_payment_label.setMaximumSize(QSize(16777215, 51))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.top_payment_label.setFont(font)
        self.top_payment_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(222, 148, 0);")
        self.top_payment_label.setText(u"Επεξεργασία πληρωμής")
        self.top_payment_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.top_payment_label, 0, 0, 1, 3)

        self.supplier_name_label = QLabel(self.centralwidget)
        self.supplier_name_label.setObjectName(u"supplier_name_label")
        self.supplier_name_label.setMinimumSize(QSize(0, 31))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.supplier_name_label.setFont(font1)
        self.supplier_name_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.supplier_name_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.supplier_name_label, 1, 0, 1, 1)

        self.amount_QSpinBox = QSpinBox(self.centralwidget)
        self.amount_QSpinBox.setObjectName(u"amount_QSpinBox")
        self.amount_QSpinBox.setMinimumSize(QSize(0, 31))
        self.amount_QSpinBox.setFont(font1)
        self.amount_QSpinBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.amount_QSpinBox.setMaximum(999999)
        self.gridLayout.addWidget(self.amount_QSpinBox, 2, 1, 1, 1)

        self.date_edit = QDateEdit(self.centralwidget)
        self.date_edit.setObjectName(u"date_edit")
        self.date_edit.setMinimumSize(QSize(0, 31))
        self.date_edit.setFont(font1)
        self.date_edit.setAcceptDrops(True)
#if QT_CONFIG(statustip)
        self.date_edit.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.date_edit.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.date_edit.setAutoFillBackground(True)
        self.date_edit.setStyleSheet(u"color: rgb(145, 145, 0);" 'font: 905 12pt "Calibri";')
        self.date_edit.setInputMethodHints(Qt.ImhDate)
        self.date_edit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.date_edit.setSpecialValueText(u"")
        self.date_edit.setDateTime(QDateTime(QDate(2021, 1, 1), QTime(0, 0, 0)))
        self.date_edit.setCurrentSection(QDateTimeEdit.DaySection)
        self.date_edit.setDisplayFormat(u"d/M/yy")
        self.date_edit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.date_edit, 3, 1, 1, 1)

        self.supplier_qcompobox = QComboBox(self.centralwidget)
        self.supplier_qcompobox.setObjectName(u"supplier_qcompobox")
        self.supplier_qcompobox.setEnabled(True)
        self.supplier_qcompobox.setMinimumSize(QSize(0, 31))
        self.supplier_qcompobox.setFont(font1)
        self.supplier_qcompobox.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.supplier_qcompobox, 1, 1, 1, 2)

        self.date_label = QLabel(self.centralwidget)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setMinimumSize(QSize(0, 31))
        self.date_label.setFont(font1)
        self.date_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.date_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.date_label, 3, 0, 1, 1)

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
        self.delete_btn.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(170, 0, 0);")
        self.delete_btn.clicked.connect(lambda: self.delete())
        self.delete_btn.clicked.connect(MainWindow.close)
        self.gridLayout.addWidget(self.delete_btn, 4, 0, 1, 1)

        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setEnabled(True)
        sizePolicy.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy)
        self.save_btn.setMinimumSize(QSize(0, 60))
        self.save_btn.setFont(font1)
        self.save_btn.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(92, 184, 78);")
        self.save_btn.clicked.connect(lambda: self.save())
        self.save_btn.clicked.connect(MainWindow.close)
        self.gridLayout.addWidget(self.save_btn, 4, 1, 1, 2)

        self.amount_label = QLabel(self.centralwidget)
        self.amount_label.setObjectName(u"amount_label")
        self.amount_label.setMinimumSize(QSize(0, 31))
        self.amount_label.setFont(font1)
        self.amount_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.amount_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.amount_label, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.save_btn.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Επεξεργασία πληρωμής", None))
        self.supplier_name_label.setText(QCoreApplication.translate("MainWindow", u"\u03a0\u03c1\u03bf\u03bc\u03b7\u03b8\u03b5\u03c5\u03c4\u03ae\u03c2", None))
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"\u0397\u03bc\u03b5\u03c1\u03bf\u03bc\u03b7\u03bd\u03af\u03b1", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"\u0394\u03b9\u03b1\u03b3\u03c1\u03b1\u03c6\u03ae", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"\u0391\u03c0\u03bf\u03b8\u03ae\u03ba\u03b5\u03c5\u03c3\u03b7", None))
        self.amount_label.setText(QCoreApplication.translate("MainWindow", u"\u03a0\u03bf\u03c3\u03cc", None))
    # retranslateUi

# Αποθήκευση
    def save(self):
        payment = Session.query(Payments).get(self.payment_id)
        old_amount = int(payment.amount)
        old_date = payment.date
        payment.amount = int(self.amount_QSpinBox.text())
        # Αλλαγή Υπολοίπου του προμηθευτή
        supplier = Session.query(Suppliers).get(payment.supplier_id)
        old_balance = int(supplier.balance)
        # Πρόσθεση προηγούμενης πληρωμής στο υπόλοιπο
        supplier.balance += old_amount
        # Αφέρεση απο το υπόλοιπο της νέας πληρωμής
        supplier.balance -= int(payment.amount)
        Session.add(supplier)
        Session.commit()

        payment.date = self.date_edit.date().toPython().strftime("%#d/%#m/%Y")

        Session.add(payment)
        Session.commit()
        print("*" * 40, "Επεξεργασία Πληρωμής", "*" * 40)
        print(f"Προμηθευτής '{payment.supplier}'  Παλιά τιμή '{old_amount}' Παλιά ημερομηνία '{old_date}'")
        print(f"Προμηθευτής '{payment.supplier}'  Νέα τιμή '{payment.amount}' Νέα ημερομηνία '{payment.date}'")

        print("Ενημέρωση υπολοίπου προμηθευτή")
        print(f"Παλίο υπόλοιπο προμηθευτή '{old_balance}' Νεό υπόλειπο προμηθευτή '{supplier.balance}'")
        print("*" * 40, "Επεξεργασία Πληρωμής ολοκληρώθηκε", "*" * 40)

        msgBox = QMessageBox.information(None, "Πληροφορία", f"Οι αλλαγές στον {payment.supplier} αποθηκεύτηκαν.")
        self.payment_id = None

    # Διαγραφή
    def delete(self):
        payment_to_delete = Session.query(Payments).get(self.payment_id)
        msgbox = QMessageBox(QMessageBox.Question, "Επιβεβαίωση διαγραφής",
                             f"Είστε σήγουρος για την διαγραφή της πληρωμής του προμηθευτή "
                             f"{payment_to_delete.supplier};")
        msgbox.addButton(QMessageBox.Yes)
        msgbox.addButton(QMessageBox.No)
        msgbox.setDefaultButton(QMessageBox.No)
        reply = msgbox.exec()

        if reply == QMessageBox.Yes:
            # Ενημέρωση υπολοίπου προμηθευτή
            supplier_id = payment_to_delete.supplier_id
            supplier = Session.query(Suppliers).get(supplier_id)
            old_balance = supplier.balance
            # Προσθήκη ποσου πληρωμής στο υπόλοιπο του προμηθευτή
            supplier.balance += int(payment_to_delete.amount)
            Session.add(supplier)
            Session.commit()
            # Διαγραφή
            Session.delete(payment_to_delete)
            Session.commit()
            print("*" * 40, "Διαγραφή πληρωμής", "*" * 40)
            print(f"Προμηθευτής '{payment_to_delete.supplier}' Τιμή '{payment_to_delete.amount}' "
                  f" Hμερομηνία '{payment_to_delete.date}'")

            print("Ενημέρωση υπολοίπου προμηθευτή")
            print(f"Παλίο υπόλοιπο προμηθευτή '{old_balance}' Νεό υπόλειπο προμηθευτή '{supplier.balance}'")
            print("*" * 40, "Διαγραφή πληρωμής ολοκληρώθηκε", "*" * 40)

            msgBox = QMessageBox.information(None, "Πληροφορία", f"Η πληρωμή του προμηθευτή  {payment_to_delete.supplier} διαγράφτηκε.")

        else:
            return