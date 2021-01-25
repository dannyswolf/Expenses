# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_purchaseDsyGpP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QCoreApplication, QSize, Qt, QMetaObject, QDateTime, QDate, QTime
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QLineEdit, QLabel, QPushButton, QSizePolicy, QWidget, QGridLayout, QSpinBox, QMessageBox, \
    QComboBox, QDateEdit, QAbstractSpinBox, QDateTimeEdit, QPlainTextEdit, QFileDialog

from sql import Session, Suppliers, Purchases

import datetime
import sys
import shutil
import os
import subprocess

from settings import root_logger

sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info


class Edit_Purchase_Window(object):
    def __init__(self, parent=None):
        super(Edit_Purchase_Window, self).__init__()
        self.purchase_id = None
        self.file = None

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(733, 507)
        MainWindow.setStyleSheet(u"background-color: rgb(55, 88, 120);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.top_purchase_label = QLabel(self.centralwidget)
        self.top_purchase_label.setObjectName(u"top_purchase_label")
        self.top_purchase_label.setMinimumSize(QSize(0, 51))
        self.top_purchase_label.setMaximumSize(QSize(16777215, 51))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.top_purchase_label.setFont(font)
        self.top_purchase_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                              "background-color: rgb(222, 148, 0);")
        self.top_purchase_label.setText(
            u"\u0395\u03c0\u03b5\u03be\u03b5\u03c1\u03b3\u03b1\u03c3\u03af\u03b1 \u03b1\u03b3\u03bf\u03c1\u03ac\u03c2")
        self.top_purchase_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.top_purchase_label, 0, 0, 1, 3)

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

        self.supplier_qcompobox = QComboBox(self.centralwidget)
        self.supplier_qcompobox.setObjectName(u"supplier_qcompobox")
        self.supplier_qcompobox.setEnabled(True)
        self.supplier_qcompobox.setMinimumSize(QSize(0, 31))
        self.supplier_qcompobox.setFont(font1)
        self.supplier_qcompobox.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.supplier_qcompobox, 1, 1, 1, 2)

        self.invoice_label = QLabel(self.centralwidget)
        self.invoice_label.setObjectName(u"invoice_label")
        self.invoice_label.setMinimumSize(QSize(0, 31))
        self.invoice_label.setFont(font1)
        self.invoice_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.invoice_label, 2, 0, 1, 1)

        self.price_label = QLabel(self.centralwidget)
        self.price_label.setObjectName(u"price_label")
        self.price_label.setMinimumSize(QSize(0, 31))
        self.price_label.setFont(font1)
        self.price_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.price_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.price_label, 3, 0, 1, 1)

        self.recipient_label = QLabel(self.centralwidget)
        self.recipient_label.setObjectName(u"recipient_label")
        self.recipient_label.setMinimumSize(QSize(0, 31))
        self.recipient_label.setFont(font1)
        self.recipient_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.recipient_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.recipient_label, 4, 0, 1, 1)

        self.recipient_comboBox = QComboBox(self.centralwidget)
        self.recipient_comboBox.setObjectName(u"recipient_comboBox")
        self.recipient_comboBox.setMinimumSize(QSize(0, 31))
        self.recipient_comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.recipient_comboBox.setFont(font1)
        self.recipient_comboBox.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.recipient_comboBox, 4, 1, 1, 2)

        self.date_label = QLabel(self.centralwidget)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setMinimumSize(QSize(0, 31))
        self.date_label.setFont(font1)
        self.date_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.date_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.date_label, 5, 0, 1, 1)

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
        self.delete_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(170, 0, 0);")
        self.delete_btn.clicked.connect(lambda: self.delete())
        self.delete_btn.clicked.connect(MainWindow.close)
        self.gridLayout.addWidget(self.delete_btn, 10, 0, 1, 1)

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
        self.save_btn.clicked.connect(MainWindow.close)
        self.gridLayout.addWidget(self.save_btn, 10, 1, 1, 2)

        self.invoice_edit = QLineEdit(self.centralwidget)
        self.invoice_edit.setObjectName(u"invoice_edit")
        self.invoice_edit.setMinimumSize(QSize(0, 31))
        self.invoice_edit.setMaximumSize(QSize(16777215, 16777215))
        self.invoice_edit.setFont(font1)
        self.invoice_edit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.invoice_edit, 2, 1, 1, 1)

        self.price_QSpinBox = QSpinBox(self.centralwidget)
        self.price_QSpinBox.setObjectName(u"price_QSpinBox")
        self.price_QSpinBox.setMinimumSize(QSize(0, 31))
        self.price_QSpinBox.setFont(font1)
        self.price_QSpinBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.price_QSpinBox.setMaximum(9999999)

        self.gridLayout.addWidget(self.price_QSpinBox, 3, 1, 1, 1)

        self.date_edit = QDateEdit(self.centralwidget)
        self.date_edit.setObjectName(u"date_edit")
        self.date_edit.setMinimumSize(QSize(0, 31))
        self.date_edit.setFont(font1)
        self.date_edit.setAcceptDrops(True)
        # if QT_CONFIG(statustip)
        self.date_edit.setStatusTip(u"")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(accessibility)
        self.date_edit.setAccessibleName(u"")
        # endif // QT_CONFIG(accessibility)
        self.date_edit.setAutoFillBackground(True)
        self.date_edit.setStyleSheet(u"color: rgb(145, 145, 0);" 'font: 905 12pt "Calibri";')
        self.date_edit.setInputMethodHints(Qt.ImhDate)
        self.date_edit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.date_edit.setSpecialValueText(u"")
        self.date_edit.setDateTime(QDateTime(QDate(2021, 1, 1), QTime(0, 0, 0)))
        self.date_edit.setCurrentSection(QDateTimeEdit.DaySection)
        self.date_edit.setDisplayFormat(u"d/M/yy")
        self.date_edit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.date_edit, 5, 1, 1, 1)

        self.product_description_label = QLabel(self.centralwidget)
        self.product_description_label.setObjectName(u"product_description_label")
        self.product_description_label.setMinimumSize(QSize(0, 31))
        self.product_description_label.setFont(font1)
        self.product_description_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.product_description_label, 6, 0, 1, 1)

        self.product_description_plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.product_description_plainTextEdit.setObjectName(u"product_description_plainTextEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.product_description_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.product_description_plainTextEdit.setSizePolicy(sizePolicy1)
        self.product_description_plainTextEdit.setFont(font1)
        self.product_description_plainTextEdit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.product_description_plainTextEdit, 6, 1, 2, 1)

        # Προσθήκη αρχείου
        self.add_file_btn = QPushButton(self.centralwidget)
        self.add_file_btn.setObjectName(u"add_file_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add_file_btn.sizePolicy().hasHeightForWidth())
        self.add_file_btn.setSizePolicy(sizePolicy1)
        self.add_file_btn.setMinimumSize(QSize(0, 0))
        self.add_file_btn.setFont(font1)
        self.add_file_btn.setStyleSheet(u"background-color: rgb(170, 85, 0);\n"
                                        "color: rgb(255, 255, 255);")
        self.add_file_btn.clicked.connect(lambda: self.add_file())
        self.gridLayout.addWidget(self.add_file_btn, 6, 0, 1, 1)
        # View File Btn
        self.view_file_btn = QPushButton(self.centralwidget)
        self.view_file_btn.setObjectName(u"view_file_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.view_file_btn.sizePolicy().hasHeightForWidth())
        self.view_file_btn.setSizePolicy(sizePolicy1)
        self.view_file_btn.setMinimumSize(QSize(0, 0))
        self.view_file_btn.setFont(font1)
        self.view_file_btn.setStyleSheet(u"background-color: rgb(170, 85, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.view_file_btn.hide()
        self.view_file_btn.clicked.connect(lambda: self.view_file())
        self.gridLayout.addWidget(self.view_file_btn, 7, 0, 1, 1)

        self.delete_file_btn = QPushButton(self.centralwidget)
        self.delete_file_btn.setObjectName(u"delete_file_btn")
        sizePolicy1.setHeightForWidth(self.delete_file_btn.sizePolicy().hasHeightForWidth())
        self.delete_file_btn.setSizePolicy(sizePolicy1)
        self.delete_file_btn.setMinimumSize(QSize(0, 0))
        self.delete_file_btn.setFont(font1)
        self.delete_file_btn.setStyleSheet(u"background-color: rgb(170, 0, 0);\n"
                                           "color: rgb(255, 255, 255);")
        self.delete_file_btn.hide()
        self.delete_file_btn.clicked.connect(lambda: self.delete_file())
        self.gridLayout.addWidget(self.delete_file_btn, 9, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Επεξεργασία αγοράς", None))
        self.supplier_name_label.setText(QCoreApplication.translate("MainWindow",
                                                                    u"\u03a0\u03c1\u03bf\u03bc\u03b7\u03b8\u03b5\u03c5\u03c4\u03ae\u03c2",
                                                                    None))
        self.invoice_label.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u0391\u03c1\u03b9\u03b8\u03bc\u03cc\u03c2 \u03c4\u03b9\u03bc\u03bf\u03bb\u03bf\u03b3\u03af\u03bf\u03c5",
                                                              None))
        self.price_label.setText(QCoreApplication.translate("MainWindow", u"\u03a4\u03b9\u03bc\u03ae", None))
        self.recipient_label.setText(
            QCoreApplication.translate("MainWindow", u"\u03a0\u03b1\u03c1\u03b1\u03bb\u03ae\u03c0\u03c4\u03b7\u03c2",
                                       None))
        self.date_label.setText(
            QCoreApplication.translate("MainWindow", u"\u0397\u03bc\u03b5\u03c1\u03bf\u03bc\u03b7\u03bd\u03af\u03b1",
                                       None))
        self.delete_btn.setText(
            QCoreApplication.translate("MainWindow", u"\u0394\u03b9\u03b1\u03b3\u03c1\u03b1\u03c6\u03ae", None))
        self.save_btn.setText(
            QCoreApplication.translate("MainWindow", u"\u0391\u03c0\u03bf\u03b8\u03ae\u03ba\u03b5\u03c5\u03c3\u03b7",
                                       None))
        self.product_description_label.setText(QCoreApplication.translate("MainWindow",
                                                                          u"\u03a0\u03b5\u03c1\u03b9\u03b3\u03c1\u03b1\u03c6\u03ae \u03c0\u03c1\u03bf\u03b9\u03cc\u03bd\u03c4\u03bf\u03c2",
                                                                          None))
        self.add_file_btn.setText(QCoreApplication.translate("MainWindow", u"Προσθήκη αρχείου", None))
        self.view_file_btn.setText(QCoreApplication.translate("MainWindow", u"Προβολή αρχείου", None))
        self.delete_file_btn.setText(QCoreApplication.translate("MainWindow", u"Διαγραφή αρχείου", None))

    # retranslateUi

    # Αποθήκευση
    def save(self):
        purchase = Session.query(Purchases).get(self.purchase_id)
        if self.file:
            files_path = "files" + "/" + purchase.supplier.name + "/" + str(datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")) + "/"
            # Δημηουργία φακέλου για το αρχείο
            if not os.path.exists(files_path):
                os.makedirs(files_path, exist_ok=True)
            file_to_add = os.path.abspath(shutil.copy(self.file, files_path, follow_symlinks=True))
            purchase.file = file_to_add
        old_invoice = purchase.invoice
        old_product = purchase.product
        old_price = int(purchase.price)
        old_date = purchase.date

        purchase.price = int(self.price_QSpinBox.text())
        # Αλλαγή οιπολύπου του προμηθευτή
        supplier = Session.query(Suppliers).get(purchase.supplier_id)
        old_balance = int(supplier.balance)
        # Αφέρεση προηγούμενης τιμης προιόντος
        supplier.balance -= old_price
        # Πρόσθεση νέας τιμής προιόντος
        supplier.balance += int(purchase.price)
        Session.add(supplier)
        Session.commit()

        purchase.invoice = self.invoice_edit.text()
        purchase.date = self.date_edit.date().toPython().strftime("%#d/%#m/%Y")
        purchase.product = self.product_description_plainTextEdit.toPlainText()

        Session.add(purchase)
        Session.commit()
        print("*" * 40, "Επεξεργασία αγοράς", "*" * 40)
        print(f"Προμηθευτής '{purchase.supplier}'  Παλιά τιμή '{old_price}' Παλιό τιμολόγιο '{old_invoice}' "
              f"Παραλήπτης '{purchase.recipient}΄ Παλιό προιόν '{old_product}' Παλιά ημερομηνία '{old_date}'")

        print(f"Προμηθευτής '{purchase.supplier}'  Νέα τιμή '{purchase.price}' Νέο τιμολόγιο '{purchase.invoice}' "
              f"Παραλήπτης '{purchase.recipient}΄ Νέο προιόν '{purchase.product}' Νέα ημερομηνία '{purchase.date}'")
        print("Ενημέρωση υπολοίπου προμηθευτή")
        print(f"Παλίο υπόλοιπο προμηθευτή '{old_balance}' Νεό υπόλειπο προμηθευτή '{supplier.balance}'")
        print("*" * 40, "Επεξεργασία αγοράς ολοκληρώθηκε", "*" * 40)

        msgBox = QMessageBox.information(None, "Πληροφορία", f"Οι αλλαγές στον {purchase.supplier} αποθηκεύτηκαν.")
        self.purchase_id = None

    # Διαγραφή
    def delete(self):
        purchase_to_delete = Session.query(Purchases).get(self.purchase_id)
        msgbox = QMessageBox(QMessageBox.Question, "Επιβεβαίωση διαγραφής",
                             f"Είστε σήγουρος για την διαγραφή της αγοράς του προμηθευτή "
                             f"{purchase_to_delete.supplier};")
        msgbox.addButton(QMessageBox.Yes)
        msgbox.addButton(QMessageBox.No)
        msgbox.setDefaultButton(QMessageBox.No)
        reply = msgbox.exec()

        if reply == QMessageBox.Yes:
            # Διαγραφή αρχείου
            try:
                shutil.rmtree(os.path.dirname(self.file))
            except NotADirectoryError:
                msgBox = QMessageBox.critical(None, "Σφάλμα", f"Αδυναμία διαγραφής αρχείου")
                return
            except TypeError:  # expected str, bytes or os.PathLike object, not NoneType
                pass
            # Ενημέρωση οιπολοιπου προμηθευτή
            supplier_id = purchase_to_delete.supplier_id
            supplier = Session.query(Suppliers).get(supplier_id)
            old_balance = supplier.balance
            supplier.balance -= purchase_to_delete.price
            Session.add(supplier)
            Session.commit()
            print("*" * 40, "Διαγραφή αγοράς", "*" * 40)
            print(f"Προμηθευτής '{purchase_to_delete.supplier}' Τιμή '{purchase_to_delete.price}' "
                  f"Τιμολόγιο '{purchase_to_delete.invoice}' "
                  f"Παραλήπτης '{purchase_to_delete.recipient}΄ Προιόν '{purchase_to_delete.product}'"
                  f" Hμερομηνία '{purchase_to_delete.date}'")

            print("Ενημέρωση υπολοίπου προμηθευτή")
            print(f"Παλίο υπόλοιπο προμηθευτή '{old_balance}' Νεό υπόλειπο προμηθευτή '{supplier.balance}'")
            print("*" * 40, "Διαγραφή αγοράς ολοκληρώθηκε", "*" * 40)
            # Διαγραφή
            Session.delete(purchase_to_delete)
            Session.commit()
            msgBox = QMessageBox.information(None, "Πληροφορία", f"Η αγορά απο τον προμηθευτή  {purchase_to_delete.supplier} διαγράφτηκε.")

        else:
            return

    def view_file(self):
        if sys.platform == "linux":

            file_to_open = str(self.file).replace(" ", '\\ ')
            # file_to_open = os.path.join(self.images_path + self.filenames[self.index])
            os.system(f'okular {file_to_open}')
        else:
            file_to_open = str(self.file)

            subprocess.Popen(file_to_open, shell=True)

    def delete_file(self):
        msgbox = QMessageBox(QMessageBox.Question, "Επιβεβαίωση διαγραφής",
                             f"Είστε σήγουρος για την διαγραφή τoυ αρχείου ")
        msgbox.addButton(QMessageBox.Yes)
        msgbox.addButton(QMessageBox.No)
        msgbox.setDefaultButton(QMessageBox.No)
        reply = msgbox.exec()

        if reply == QMessageBox.Yes:
            try:
                shutil.rmtree(os.path.dirname(self.file))
                self.file = None
                self.view_file_btn.hide()
                self.delete_file_btn.hide()
                self.add_file_btn.show()
                # Ενημέρωση βάσης δεδομέων για την διαγραφή αρχείου
                purchase = Session.query(Purchases).get(self.purchase_id)
                purchase.file = None
                Session.add(purchase)
                Session.commit()
                msgBox = QMessageBox.information(None, "Πληροφορία", "Η διαγραφή του αρχείου ολοκληρώθηκε")
            except NotADirectoryError:
                msgBox = QMessageBox.critical(None, "Σφάλμα", f"Αδυναμία διαγραφής αρχείου")
                return
            except FileNotFoundError:
                msgBox = QMessageBox.critical(None, "Σφάλμα", f"Δεν βρέθηκε αρχείο")
                return

    def add_file(self):
        self.file, filters = QFileDialog.getOpenFileName(None, caption='Προσθήκη αρχείου', dir='.',
                                                                 filter='*.pdf')

        self.add_file_btn.setStyleSheet(u"background-color: rgb(92, 184, 78); color: rgb(255, 255, 255);")
        self.add_file_btn.setText(QCoreApplication.translate("MainWindow", u"Αρχείο για προσθήκη", None))
        self.add_file_btn.setEnabled(False)
