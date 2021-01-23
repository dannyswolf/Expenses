# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_supplierzTKkYh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QCoreApplication, QSize, Qt, QMetaObject
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QLineEdit, QLabel, QPushButton, QSizePolicy, QWidget, QGridLayout, QSpinBox, QMessageBox

from sql import Session, Suppliers, MultipleResultsFound

import sys

from settings import root_logger
sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info


class Edit_supplier_window(object):
    def __init__(self, parent=None):
        super(Edit_supplier_window, self).__init__()

        self.supplier_id = None

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(504, 440)
        MainWindow.setStyleSheet(u"background-color: rgb(55, 88, 120);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.top_supplier_label = QLabel(self.centralwidget)
        self.top_supplier_label.setObjectName(u"top_supplier_label")
        self.top_supplier_label.setMinimumSize(QSize(0, 0))
        self.top_supplier_label.setMaximumSize(QSize(16777215, 51))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.top_supplier_label.setFont(font)
        self.top_supplier_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(222, 148, 0);")
        self.top_supplier_label.setText(u"\u0395\u03c0\u03b5\u03be\u03b5\u03c1\u03b3\u03b1\u03c3\u03af\u03b1 \u03c0\u03c1\u03bf\u03bc\u03b7\u03b8\u03b5\u03c5\u03c4\u03ae")
        self.top_supplier_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.top_supplier_label, 0, 0, 1, 2)

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

        self.supplier_name_edit = QLineEdit(self.centralwidget)
        self.supplier_name_edit.setObjectName(u"supplier_name_edit")
        self.supplier_name_edit.setMinimumSize(QSize(0, 31))
        self.supplier_name_edit.setMaximumSize(QSize(16777215, 16777215))
        self.supplier_name_edit.setFont(font1)
        self.supplier_name_edit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.supplier_name_edit, 1, 1, 1, 1)

        self.vat_nr_label = QLabel(self.centralwidget)
        self.vat_nr_label.setObjectName(u"vat_nr_label")
        self.vat_nr_label.setMinimumSize(QSize(0, 31))
        self.vat_nr_label.setFont(font1)
        self.vat_nr_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.vat_nr_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.vat_nr_label, 2, 0, 1, 1)

        self.vat_nr_edit = QLineEdit(self.centralwidget)
        self.vat_nr_edit.setObjectName(u"vat_nr_edit")
        self.vat_nr_edit.setMinimumSize(QSize(0, 31))
        self.vat_nr_edit.setMaximumSize(QSize(16777215, 16777215))
        self.vat_nr_edit.setFont(font1)
        self.vat_nr_edit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.vat_nr_edit, 2, 1, 1, 1)

        self.supplier_phone_label = QLabel(self.centralwidget)
        self.supplier_phone_label.setObjectName(u"supplier_phone_label")
        self.supplier_phone_label.setMinimumSize(QSize(0, 31))
        self.supplier_phone_label.setFont(font1)
        self.supplier_phone_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.supplier_phone_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.supplier_phone_label, 3, 0, 1, 1)

        self.supplier_phone_edit = QLineEdit(self.centralwidget)
        self.supplier_phone_edit.setObjectName(u"supplier_phone_edit")
        self.supplier_phone_edit.setMinimumSize(QSize(0, 31))
        self.supplier_phone_edit.setMaximumSize(QSize(16777215, 16777215))
        self.supplier_phone_edit.setFont(font1)
        self.supplier_phone_edit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.supplier_phone_edit, 3, 1, 1, 1)

        self.supplier_address_label = QLabel(self.centralwidget)
        self.supplier_address_label.setObjectName(u"supplier_address_label")
        self.supplier_address_label.setMinimumSize(QSize(0, 31))
        self.supplier_address_label.setFont(font1)
        self.supplier_address_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.supplier_address_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.supplier_address_label, 4, 0, 1, 1)

        self.supplier_address_edit = QLineEdit(self.centralwidget)
        self.supplier_address_edit.setObjectName(u"supplier_address_edit")
        self.supplier_address_edit.setMinimumSize(QSize(0, 31))
        self.supplier_address_edit.setMaximumSize(QSize(16777215, 16777215))
        self.supplier_address_edit.setFont(font1)
        self.supplier_address_edit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.supplier_address_edit, 4, 1, 1, 1)

        self.supplier_balance_label = QLabel(self.centralwidget)
        self.supplier_balance_label.setObjectName(u"supplier_balance_label")
        self.supplier_balance_label.setMinimumSize(QSize(0, 31))
        self.supplier_balance_label.setFont(font1)
        self.supplier_balance_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.supplier_balance_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.supplier_balance_label, 5, 0, 1, 1)

        self.supplier_balance_QSpinBox = QSpinBox(self.centralwidget)
        self.supplier_balance_QSpinBox.setObjectName(u"supplier_balance_QSpinBox")
        self.supplier_balance_QSpinBox.setMinimumSize(QSize(0, 31))
        self.supplier_balance_QSpinBox.setFont(font1)
        self.supplier_balance_QSpinBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.supplier_balance_QSpinBox.setMaximum(9999999)

        self.gridLayout.addWidget(self.supplier_balance_QSpinBox, 5, 1, 1, 1)

        self.delete_supplier_btn = QPushButton(self.centralwidget)
        self.delete_supplier_btn.setObjectName(u"delete_supplier_btn")
        self.delete_supplier_btn.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_supplier_btn.sizePolicy().hasHeightForWidth())
        self.delete_supplier_btn.setSizePolicy(sizePolicy)
        self.delete_supplier_btn.setMinimumSize(QSize(0, 60))
        self.delete_supplier_btn.setFont(font1)
        self.delete_supplier_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);")
        self.delete_supplier_btn.clicked.connect(lambda: self.delete())
        self.delete_supplier_btn.clicked.connect(MainWindow.close)

        self.gridLayout.addWidget(self.delete_supplier_btn, 6, 0, 1, 1)

        self.save_supplier_btn = QPushButton(self.centralwidget)
        self.save_supplier_btn.setObjectName(u"save_supplier_btn")
        self.save_supplier_btn.setEnabled(True)
        sizePolicy.setHeightForWidth(self.save_supplier_btn.sizePolicy().hasHeightForWidth())
        self.save_supplier_btn.setSizePolicy(sizePolicy)
        self.save_supplier_btn.setMinimumSize(QSize(0, 60))
        self.save_supplier_btn.setFont(font1)
        self.save_supplier_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(92, 184, 78);")

        self.gridLayout.addWidget(self.save_supplier_btn, 6, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.save_supplier_btn.clicked.connect(lambda: self.save())
        self.save_supplier_btn.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Επεξεργασία προμηθευτή", None))
        self.supplier_name_label.setText(QCoreApplication.translate("MainWindow", u"\u039f\u03bd\u03bf\u03bc\u03b1\u03c4\u03b5\u03c0\u03ce\u03bd\u03c5\u03bc\u03bf", None))
        self.vat_nr_label.setText(QCoreApplication.translate("MainWindow", u"\u0391.\u03a6.\u039c.", None))
        self.supplier_phone_label.setText(QCoreApplication.translate("MainWindow", u"\u03a4\u03b7\u03bb\u03ad\u03c6\u03c9\u03bd\u03bf", None))
        self.supplier_address_label.setText(QCoreApplication.translate("MainWindow", u"\u0394\u03b9\u03b5\u03cd\u03b8\u03c5\u03bd\u03c3\u03b7", None))
        self.supplier_balance_label.setText(QCoreApplication.translate("MainWindow", u"\u03a5\u03c0\u03cc\u03bb\u03bf\u03b9\u03c0\u03bf", None))
#if QT_CONFIG(tooltip)
        self.supplier_balance_QSpinBox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.delete_supplier_btn.setText(QCoreApplication.translate("MainWindow", u"\u0394\u03b9\u03b1\u03b3\u03c1\u03b1\u03c6\u03ae", None))
        self.save_supplier_btn.setText(QCoreApplication.translate("MainWindow", u"\u0391\u03c0\u03bf\u03b8\u03ae\u03ba\u03b5\u03c5\u03c3\u03b7", None))
    # retranslateUi

    # Αποθήκευση
    def save(self):
        supplier = Session.query(Suppliers).get(self.supplier_id)
        new_name = self.supplier_name_edit.text()
        new_vat_nr = self.vat_nr_edit.text()
        new_phone = self.supplier_phone_edit.text()
        new_address = self.supplier_address_edit.text()
        new_balance = self.supplier_balance_QSpinBox.text()
        # Ελεγχος ΑΦΜ
        if not new_vat_nr.isdigit():
            msgBox = QMessageBox.critical(None, "Σφάλμα", f"Το Α.Φ.Μ. πρέπει να είναι αριθμός")
            return
        elif len(new_vat_nr) != 9:
            msgBox = QMessageBox.critical(None, "Σφάλμα", f"Το Α.Φ.Μ. πρέπει να είναι αριθμός με 9 ψηφία!")
            return

        # Ελεγχος αν υπάρχει το ΑΦΜ
        try:
            existing_supplier = Session.query(Suppliers).filter_by(vat_nr=new_vat_nr).one_or_none()
            if existing_supplier.id != supplier.id:
                msgBox = QMessageBox.critical(None, "Σφάλμα", f"Το Α.Φ.Μ. {supplier.vat_nr} υπάρχει στον προμηθευτή {existing_supplier.name}!")
                return
        except MultipleResultsFound:
            msgBox = QMessageBox.critical(None, "Σφάλμα", f"Το Α.Φ.Μ. υπάρχει πολλές φορές!")
            return
        supplier.name = new_name
        supplier.vat_nr = new_vat_nr
        supplier.phone = new_phone
        supplier.address = new_address
        supplier.balance = new_balance
        Session.add(supplier)
        Session.commit()
        msgBox = QMessageBox.information(None, "Πληροφορία", f"Οι αλλαγές στον {supplier.name} αποθηκεύτηκαν.")
        self.supplier_id = None

    # Διαγραφή
    def delete(self):
        supplier_to_delete = Session.query(Suppliers).get(self.supplier_id)
        msgbox = QMessageBox(QMessageBox.Question, "Επιβεβαίωση διαγραφής", f"Είστε σήγουρος για την διαγραφή του προμηθευτή "
                                                          f"{supplier_to_delete.name};")
        msgbox.addButton(QMessageBox.Yes)
        msgbox.addButton(QMessageBox.No)
        msgbox.setDefaultButton(QMessageBox.No)
        reply = msgbox.exec()

        if reply == QMessageBox.Yes:
            Session.delete(supplier_to_delete)
            Session.commit()
            msgBox = QMessageBox.information(None, "Πληροφορία", f"Ο προμηθευτής {supplier_to_delete.name} Διαγράφτηκε.")

        else:
            return