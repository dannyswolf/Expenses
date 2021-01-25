#! /usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWTVDde.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
# -------------------------------------------------------------------------------
#                  ΕΞΟΔΑ
#                  Ντίνι Ιορδάνης
#                  2021
# V 1.1 Εισαγωγή αρχείων
# V 1.0 Επεξεργασία Πληρομών
# V 0.9 Επεξεργασία αγορών
# V 0.8 Alfa Ξεχωριστα επεξεργασίας προμηθευτή και παραλήπτη
# V 0.8 Alfa Δυνατότηα επεξεργασίας προμηθευτή και παραλήπτη
# V 0.7 Alfa Δυνατότηα προσθήκης προμηθευτή και παραλήπτη
# V 0.6 Alfa ready to add 'add_supplier_page'
# V 0.5 Alfa Παραθυρο αγορών ετοιμο
# V 0.4 Alfa autocomplete on search lines
# V 0.3 Alfa
# todo να βάλω πληροφορίες
#
# -------------------------------------------------------------------------------

from PySide2.QtCore import QCoreApplication, QLocale, QSize, Qt, QDateTime, QRect, QMetaObject, QDate
from PySide2.QtGui import QPalette, QFont, QBrush, QCursor, QColor, QIcon
from PySide2.QtWidgets import QAbstractScrollArea, QTableWidgetItem, QTableWidget, QLineEdit, QLabel, QFrame, \
    QMainWindow, QComboBox, QStackedWidget, QPushButton, QSizePolicy, QWidget, QGridLayout, QApplication, \
    QStyleFactory, QAbstractItemView, QDateEdit, QAbstractSpinBox, QDateTimeEdit, QSpinBox, QPlainTextEdit, \
    QMenu, QMenuBar, QCompleter, QFileDialog, QMessageBox, QAction

# Για εξαγωγή σε excel
import pandas as pd
# Για αποθύκευση αρχείου
import shutil

import datetime
import sys
import os

from edit_supplier import Edit_supplier_window
from edit_recipient import Edit_recipient_window
from edit_purchase import Edit_Purchase_Window
from edit_payment import Edit_Payment_Window
from settings import root_logger, version
from sql import Suppliers, Recipients, Payments, Purchases, Session, get_data, MultipleResultsFound, NoResultFound

sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info


# Αυτόματο συπλήρωμα αναζήτησης (QLineEdit)
# Πρώτα περνουμε τα δεδομένα απο τους πίνακες
# μετά τα στέλνουμε σε QCompleter
# Προμηθευτές και παραλήπτες χρειάζεται μόνο στις αγορές
def autocomplete_purchases():
    """
    :return: Προμηθευτές και παραλήπτες
    """
    supplier_data = [r for r in Session.query(Suppliers).all()]
    recipient_data = [r for r in Session.query(Recipients).all()]
    list_data = []

    for item in supplier_data:
        list_data.append(item.name)
    for item in recipient_data:
        list_data.append(item.name)
    # Για να μήν έχει δυπλότυπα βαζουμε set
    return sorted(set(list_data))


def autocomplete(table):
    """
    :return: Προμηθευτές και παραλήπτες
    """
    data = [r for r in Session.query(table).all()]
    list_data = []

    for item in data:
        list_data.append(item.name)
    # Για να μήν έχει δυπλότυπα βαζουμε set
    return sorted(set(list_data))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(860, 400)
        MainWindow.setMinimumSize(QSize(400, 400))
        MainWindow.setSizeIncrement(QSize(20, 20))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(55, 88, 120);")
        MainWindow.setLocale(QLocale(QLocale.Greek, QLocale.Greece))
        MainWindow.setWindowFilePath(u"")

        self.suppliers = get_data(Suppliers)
        self.recipients = get_data(Recipients)
        self.purchases = get_data(Purchases)
        self.payments = get_data(Payments)

        self.files_path = None
        self.filename = None

        self.font = QFont()
        self.font.setFamily(u"Calibri")
        self.font.setPointSize(12)
        self.font.setBold(True)
        self.font.setWeight(55)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        # Import Btn
        self.import_btn = QPushButton(self.centralwidget)
        self.import_btn.setObjectName(u"import_btn")
        self.import_btn.setFont(self.font)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_btn.sizePolicy().hasHeightForWidth())
        self.import_btn.setSizePolicy(sizePolicy)
        self.import_btn.setStyleSheet(u"background-color: rgb(0, 85, 0); color: rgb(255, 255, 255);")
        self.gridLayout_3.addWidget(self.import_btn,  0, 0, 1, 1)
        self.import_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.import_page))

        # Pay Btn
        self.pay_btn = QPushButton(self.centralwidget)
        self.pay_btn.setObjectName(u"pay_btn")
        sizePolicy.setHeightForWidth(self.pay_btn.sizePolicy().hasHeightForWidth())
        self.pay_btn.setSizePolicy(sizePolicy)
        self.pay_btn.setFont(self.font)
        self.pay_btn.setStyleSheet(u"background-color: rgb(0, 85, 0); color: rgb(255, 255, 255);")
        self.gridLayout_3.addWidget(self.pay_btn, 1, 0, 3, 1)
        self.pay_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pay_page))

        # Purchases Btn
        self.purchases_btn = QPushButton(self.centralwidget)
        self.purchases_btn.setObjectName(u"purchases_btn")
        self.purchases_btn.setFont(self.font)
        sizePolicy.setHeightForWidth(self.purchases_btn.sizePolicy().hasHeightForWidth())
        self.purchases_btn.setSizePolicy(sizePolicy)
        self.purchases_btn.setStyleSheet(u"background-color: rgb(0, 85, 0); color: rgb(255, 255, 255);")
        self.purchases_btn.setAutoDefault(False)
        self.purchases_btn.setFlat(False)
        self.gridLayout_3.addWidget(self.purchases_btn,  6, 0, 1, 1)
        self.purchases_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.purchases_page))
        self.purchases_btn.clicked.connect(lambda: self.update_purchases())
        # White Line
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.gridLayout_3.addWidget(self.line, 0, 1, 8, 1)

        # Suppliers Btn
        self.suppliers_btn = QPushButton(self.centralwidget)
        self.suppliers_btn.setObjectName(u"suppliers_btn")
        sizePolicy.setHeightForWidth(self.suppliers_btn.sizePolicy().hasHeightForWidth())
        self.suppliers_btn.setSizePolicy(sizePolicy)

        self.suppliers_btn.setFont(self.font)
        self.suppliers_btn.setStyleSheet(u"background-color: rgb(0, 85, 0); color: rgb(255, 255, 255);")
        self.gridLayout_3.addWidget(self.suppliers_btn, 4, 0, 1, 1)
        self.suppliers_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.suppliers_page))
        self.suppliers_btn.clicked.connect(lambda: self.update_suppliers())
        # Recipients Btn
        self.recipients_btn = QPushButton(self.centralwidget)
        self.recipients_btn.setObjectName(u"recipients_btn")
        sizePolicy.setHeightForWidth(self.recipients_btn.sizePolicy().hasHeightForWidth())
        self.recipients_btn.setSizePolicy(sizePolicy)
        self.recipients_btn.setFont(self.font)
        self.recipients_btn.setStyleSheet(u"background-color: rgb(0, 85, 0); color: rgb(255, 255, 255);")
        self.gridLayout_3.addWidget(self.recipients_btn, 5, 0, 1, 1)  # 6 0 1 1
        self.recipients_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.recipients_page))
        self.recipients_btn.clicked.connect(lambda: self.update_recipients())
        # Payments Btn
        self.payments_btn = QPushButton(self.centralwidget)
        self.payments_btn.setObjectName(u"payments_btn")
        sizePolicy.setHeightForWidth(self.payments_btn.sizePolicy().hasHeightForWidth())
        self.payments_btn.setSizePolicy(sizePolicy)
        self.payments_btn.setFont(self.font)
        self.payments_btn.setToolTipDuration(1)
        self.payments_btn.setStyleSheet(u"background-color: rgb(0, 85, 0); color: rgb(255, 255, 255);")
        self.gridLayout_3.addWidget(self.payments_btn, 7, 0, 1, 1)
        self.payments_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.payments_page))
        self.payments_btn.clicked.connect(lambda: self.update_payments())
        # Stacked Widget
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFocusPolicy(Qt.WheelFocus)
        self.stackedWidget.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget.setFrameShadow(QFrame.Sunken)

        # Purchases Page
        self.purchases_page = QWidget()
        self.purchases_page.setObjectName(u"purchases_page")
        self.purchases_page.setContextMenuPolicy(Qt.NoContextMenu)
        self.gridLayout_7 = QGridLayout(self.purchases_page)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.purchases_label = QLabel(self.purchases_page)
        self.purchases_label.setObjectName(u"purchases_label")
        self.purchases_label.setMinimumSize(QSize(0, 51))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.purchases_label.setFont(font1)
        self.purchases_label.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.purchases_label.setAlignment(Qt.AlignCenter)
        self.gridLayout_7.addWidget(self.purchases_label, 0, 0, 1, 2)
        self.export_purchases_btn = QPushButton(self.purchases_page)
        self.export_purchases_btn.setObjectName(u"export_purchases_btn")
        self.export_purchases_btn.setMinimumSize(QSize(0, 60))
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.export_purchases_btn.setFont(font2)
        self.export_purchases_btn.setStyleSheet(u"background-color: rgb(170, 85, 0);")
        self.export_purchases_btn.clicked.connect(lambda: self.extract(self.purchases_tableWidget))
        self.gridLayout_7.addWidget(self.export_purchases_btn, 3, 0, 1, 2)
        # Κουμπί αναζήτησης αγορών
        self.search_purchases_btn = QPushButton(self.purchases_page)
        self.search_purchases_btn.setObjectName(u"search_purchases_btn")
        self.search_purchases_btn.setMinimumSize(QSize(200, 31))
        self.search_purchases_btn.setSizeIncrement(QSize(1, 1))
        self.search_purchases_btn.setBaseSize(QSize(200, 200))

        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.search_purchases_btn.setFont(font3)
        self.search_purchases_btn.clicked.connect(lambda: self.update_purchases(self.search_purchases_edit.text()))

        self.gridLayout_7.addWidget(self.search_purchases_btn, 1, 1, 1, 1)
        self.search_purchases_edit = QLineEdit(self.purchases_page)
        self.search_purchases_edit.setObjectName(u"search_purchases_edit")
        self.search_purchases_edit.setMinimumSize(QSize(0, 31))
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setPointSize(12)

        self.search_purchases_edit.setFont(font4)

        # Autocomplete
        self.list_to_search_purchases = autocomplete_purchases()

        self.purchases_completer = QCompleter(self.list_to_search_purchases)
        self.search_purchases_edit.setCompleter(self.purchases_completer)
        self.search_purchases_edit.returnPressed.connect(lambda: self.update_purchases(self.search_purchases_edit.text()))

        self.gridLayout_7.addWidget(self.search_purchases_edit, 1, 0, 1, 1)
        self.purchases_tableWidget = QTableWidget(self.purchases_page)

        self.purchases_tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4)
        self.purchases_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)

        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem1.setFont(font3)
        self.purchases_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem2.setFont(font3)
        self.purchases_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem3.setFont(font3)
        self.purchases_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem4.setFont(font3)
        self.purchases_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem5.setFont(font3)
        self.purchases_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)

        self.purchases_tableWidget.setRowCount(len(self.purchases))
        __qtablewidgetitem6 = QTableWidgetItem()
        self.purchases_tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.purchases_tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.purchases_tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem8)
        self.purchases_tableWidget.setObjectName(u"purchases_tableWidget")
        self.purchases_tableWidget.setMinimumSize(QSize(0, 0))
        self.purchases_tableWidget.setFont(font3)
        self.purchases_tableWidget.setAutoFillBackground(True)
        self.purchases_tableWidget.setStyleSheet(u"alternate-background-color: rgb(100, 120, 180);")
        # self.purchases_tableWidget.setStyleSheet(u"alternate-background-color: rgb(235, 235, 235);\n"
        #                                          "selection-color: rgb(255, 255, 255);\n"
        #                                          "selection-background-color: rgb(11, 170, 255);\n"
        #                                          "background-color: rgb(204, 204, 204);\n"
        #                                          "color: rgb(255, 85, 0);")
        self.purchases_tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.purchases_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.purchases_tableWidget.setAlternatingRowColors(True)
        self.purchases_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.purchases_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.purchases_tableWidget.setTextElideMode(Qt.ElideMiddle)
        self.purchases_tableWidget.setGridStyle(Qt.SolidLine)
        self.purchases_tableWidget.setSortingEnabled(True)
        self.purchases_tableWidget.setWordWrap(True)
        self.purchases_tableWidget.setCornerButtonEnabled(True)
        # self.purchases_tableWidget.horizontalHeader().setDefaultSectionSize(106)
        self.purchases_tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.purchases_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.purchases_tableWidget.verticalHeader().setVisible(False)
        self.purchases_tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.purchases_tableWidget.verticalHeader().setHighlightSections(True)
        self.purchases_tableWidget.setUpdatesEnabled(True)
        self.purchases_tableWidget.setColumnWidth(0, 1)
        self.purchases_tableWidget.setColumnWidth(1, 200)
        self.purchases_tableWidget.setColumnWidth(2, 200)
        self.purchases_tableWidget.setColumnWidth(3, 60)
        self.purchases_tableWidget.setColumnWidth(4, 100)
        self.purchases_tableWidget.setColumnWidth(5, 50)
        self.purchases_tableWidget.doubleClicked.connect(lambda: self.edit_purchase(self.purchases_tableWidget))

        self.gridLayout_7.addWidget(self.purchases_tableWidget, 2, 0, 1, 2)
        self.stackedWidget.addWidget(self.purchases_page)

        # Import Page
        self.import_page = QWidget()
        self.import_page.setObjectName(u"import_page")
        self.gridLayout = QGridLayout(self.import_page)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.insert_invoice_label = QLabel(self.import_page)
        self.insert_invoice_label.setObjectName(u"insert_invoice_label")
        self.insert_invoice_label.setMinimumSize(QSize(0, 51))
        self.insert_invoice_label.setMaximumSize(QSize(16777215, 51))
        self.insert_invoice_label.setFont(font1)
        self.insert_invoice_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                "background-color: rgb(85, 85, 255);")
        self.insert_invoice_label.setText(
            u"\u0395\u03b9\u03c3\u03b1\u03b3\u03c9\u03b3\u03ae "
            u"\u03c0\u03b1\u03c1\u03b1\u03c3\u03c4\u03b1\u03c4\u03b9\u03ba\u03bf\u03cd")
        self.insert_invoice_label.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.insert_invoice_label, 0, 0, 1, 3)
        self.product_description_label = QLabel(self.import_page)
        self.product_description_label.setObjectName(u"product_description_label")
        self.product_description_label.setMinimumSize(QSize(0, 31))
        self.product_description_label.setFont(font3)
        self.product_description_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayout.addWidget(self.product_description_label, 9, 0, 1, 1)

        # Προμηθευτής
        self.supplier_qcompobox = QComboBox(self.import_page)
        self.supplier_qcompobox.setObjectName(u"supplier_qcompobox")
        self.supplier_qcompobox.setEnabled(True)
        self.supplier_qcompobox.setMinimumSize(QSize(0, 31))
        self.supplier_qcompobox.setFont(font3)
        self.supplier_qcompobox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.supplier_qcompobox.addItems(sorted([f"{supplier}" for supplier in self.suppliers], key=str.lower))
        self.supplier_qcompobox.setEditable(True)
        self.supplier_qcompobox.lineEdit().setFont(font3)
        self.supplier_qcompobox.validator()
        self.gridLayout.addWidget(self.supplier_qcompobox, 1, 1, 1, 1)
        # Τιμολόγιο
        self.invoice_edit = QLineEdit(self.import_page)
        self.invoice_edit.setObjectName(u"invoice_edit")
        self.invoice_edit.setMinimumSize(QSize(0, 31))
        self.invoice_edit.setMaximumSize(QSize(16777215, 16777215))
        self.invoice_edit.setFont(font3)
        self.invoice_edit.setStyleSheet(u"color: rgb(255, 255, 255);" )
        self.gridLayout.addWidget(self.invoice_edit, 3, 1, 1, 1)
        # Ημερομηνία εισαγωγής
        self.date_edit = QDateEdit(self.import_page)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setObjectName(u"date_edit")
        self.date_edit.setMinimumSize(QSize(0, 31))
        self.date_edit.setFont(font3)
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
        self.date_edit.setDateTime(QDateTime.currentDateTime())
        self.date_edit.setCurrentSection(QDateTimeEdit.DaySection)
        self.date_edit.setDisplayFormat(u"dd/MM/yyyy")
        self.gridLayout.addWidget(self.date_edit, 4, 1, 1, 1)

        # Παραλήπτης
        self.recipient_comboBox = QComboBox(self.import_page)
        self.recipient_comboBox.setObjectName(u"recipient_comboBox")
        self.recipient_comboBox.setMinimumSize(QSize(0, 31))
        self.recipient_comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.recipient_comboBox.setFont(font3)
        self.recipient_comboBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.recipient_comboBox.addItems(sorted([f"{recipient}" for recipient in self.recipients], key=str.lower))
        self.recipient_comboBox.setEditable(True)
        self.recipient_comboBox.lineEdit().setFont(font3)
        self.gridLayout.addWidget(self.recipient_comboBox, 6, 1, 1, 1)

        # Ποσό εισαγωγής
        self.amount_doubleSpinBox_at_import_page = QSpinBox(self.import_page)
        self.amount_doubleSpinBox_at_import_page.setObjectName(u"amount_doubleSpinBox_at_import_page")
        self.amount_doubleSpinBox_at_import_page.setMinimumSize(QSize(0, 31))
        self.amount_doubleSpinBox_at_import_page.setFont(font3)
        self.amount_doubleSpinBox_at_import_page.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.amount_doubleSpinBox_at_import_page.setMaximum(9999999)
        self.gridLayout.addWidget(self.amount_doubleSpinBox_at_import_page, 8, 1, 1, 1)
        # Προίον
        self.product_description_plainTextEdit = QPlainTextEdit(self.import_page)
        self.product_description_plainTextEdit.setObjectName(u"product_description_plainTextEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.product_description_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.product_description_plainTextEdit.setSizePolicy(sizePolicy4)
        self.product_description_plainTextEdit.setFont(font3)
        self.product_description_plainTextEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayout.addWidget(self.product_description_plainTextEdit, 9, 1, 1, 2)

        self.add_file_btn = QPushButton(self.import_page)
        self.add_file_btn.setObjectName(u"add_file_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add_file_btn.sizePolicy().hasHeightForWidth())
        self.add_file_btn.setSizePolicy(sizePolicy1)
        self.add_file_btn.setMinimumSize(QSize(0, 60))
        self.add_file_btn.setFont(font3)
        self.add_file_btn.setStyleSheet(u"background-color: rgb(170, 85, 0);\n"
                                        "color: rgb(255, 255, 255);")
        self.add_file_btn.clicked.connect(lambda: self.add_file())

        self.gridLayout.addWidget(self.add_file_btn, 11, 0, 1, 1)
        self.invoice_label = QLabel(self.import_page)
        self.invoice_label.setObjectName(u"invoice_label")
        self.invoice_label.setMinimumSize(QSize(0, 31))
        self.invoice_label.setFont(font3)
        self.invoice_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayout.addWidget(self.invoice_label, 3, 0, 1, 1)
        self.insert_recipier_btn = QPushButton(self.import_page)
        self.insert_recipier_btn.setObjectName(u"insert_recipier_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.insert_recipier_btn.sizePolicy().hasHeightForWidth())
        self.insert_recipier_btn.setSizePolicy(sizePolicy2)
        self.insert_recipier_btn.setMinimumSize(QSize(200, 31))
        self.insert_recipier_btn.setFont(font3)
        self.insert_recipier_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                               "background-color: rgb(63, 63, 63);")
        self.insert_recipier_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.add_recipient_page))
        self.gridLayout.addWidget(self.insert_recipier_btn, 6, 2, 1, 1)

        self.date_label = QLabel(self.import_page)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setMinimumSize(QSize(0, 31))
        self.date_label.setFont(font3)
        self.date_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayout.addWidget(self.date_label, 4, 0, 1, 1)
        self.insert_supplier_btn = QPushButton(self.import_page)
        self.insert_supplier_btn.setObjectName(u"insert_supplier_btn")
        self.insert_supplier_btn.setMinimumSize(QSize(0, 31))
        self.insert_supplier_btn.setFont(font3)
        self.insert_supplier_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                               "background-color: rgb(7, 114, 255);")
        self.insert_supplier_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.add_supplier_page))
        self.gridLayout.addWidget(self.insert_supplier_btn, 1, 2, 1, 1)

        self.recipient_label = QLabel(self.import_page)
        self.recipient_label.setObjectName(u"recipient_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.recipient_label.sizePolicy().hasHeightForWidth())
        self.recipient_label.setSizePolicy(sizePolicy3)
        self.recipient_label.setMinimumSize(QSize(0, 31))
        self.recipient_label.setFont(font3)
        self.recipient_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayout.addWidget(self.recipient_label, 6, 0, 1, 1)
        self.price_label = QLabel(self.import_page)
        self.price_label.setObjectName(u"price_label")
        self.price_label.setMinimumSize(QSize(0, 31))
        self.price_label.setFont(font3)
        self.price_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayout.addWidget(self.price_label, 8, 0, 1, 1)
        self.supplier_label = QLabel(self.import_page)
        self.supplier_label.setObjectName(u"supplier_label")
        self.supplier_label.setMinimumSize(QSize(0, 31))
        self.supplier_label.setFont(font3)
        self.supplier_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.supplier_label.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.supplier_label, 1, 0, 1, 1)

        self.save_btn = QPushButton(self.import_page)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy5)
        self.save_btn.setMinimumSize(QSize(0, 60))
        self.save_btn.setMaximumSize(QSize(16777215, 60))
        font6 = QFont()
        font6.setFamily(u"Calibri")
        font6.setPointSize(14)
        font6.setBold(True)
        font6.setUnderline(False)
        font6.setWeight(75)
        self.save_btn.setFont(font6)
        # if QT_CONFIG(accessibility)
        self.save_btn.setAccessibleName(u"")
        # endif // QT_CONFIG(accessibility)
        self.save_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(92, 184, 78);")
        self.save_btn.clicked.connect(lambda: self.save_import())
        self.gridLayout.addWidget(self.save_btn, 11, 1, 1, 2)
        self.stackedWidget.addWidget(self.import_page)

        # Pay Page
        self.pay_page = QWidget()
        self.pay_page.setObjectName(u"pay_page")
        self.pay_page.setFont(self.font)
        self.gridLayout_5 = QGridLayout(self.pay_page)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pay_supplier_label = QLabel(self.pay_page)
        self.pay_supplier_label.setObjectName(u"pay_supplier_label")
        self.pay_supplier_label.setMinimumSize(QSize(0, 51))
        self.pay_supplier_label.setMaximumSize(QSize(16777215, 51))
        self.pay_supplier_label.setFont(font1)
        self.pay_supplier_label.setCursor(QCursor(Qt.ArrowCursor))
        self.pay_supplier_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                              "background-color: rgb(85, 85, 255);")
        self.pay_supplier_label.setAlignment(Qt.AlignCenter)
        self.gridLayout_5.addWidget(self.pay_supplier_label, 0, 0, 1, 1)
        self.supplier_label_at_pay_page = QLabel(self.pay_page)
        self.supplier_label_at_pay_page.setObjectName(u"supplier_label_at_pay_page")
        self.supplier_label_at_pay_page.setFont(font2)
        self.supplier_label_at_pay_page.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.supplier_label_at_pay_page.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.gridLayout_5.addWidget(self.supplier_label_at_pay_page, 1, 0, 1, 1)
        self.supplier_qcompobox_at_pay_page = QComboBox(self.pay_page)
        self.supplier_qcompobox_at_pay_page.setObjectName(u"supplier_qcompobox_at_pay_page")
        self.supplier_qcompobox_at_pay_page.setEnabled(True)
        self.supplier_qcompobox_at_pay_page.setMinimumSize(QSize(250, 31))
        self.supplier_qcompobox_at_pay_page.setEditable(True)
        self.supplier_qcompobox_at_pay_page.setFont(font3)
        self.supplier_qcompobox_at_pay_page.lineEdit().setFont(font3)
        self.supplier_qcompobox_at_pay_page.validator()
        self.supplier_qcompobox_at_pay_page.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.supplier_qcompobox_at_pay_page.setPlaceholderText(u"")
        self.supplier_qcompobox_at_pay_page.addItems(
            sorted([f"{supplier}" for supplier in get_data(Suppliers)], key=str.lower))
        self.gridLayout_5.addWidget(self.supplier_qcompobox_at_pay_page, 2, 0, 1, 1)
        self.price_label_at_pay_page = QLabel(self.pay_page)
        self.price_label_at_pay_page.setObjectName(u"price_label_at_pay_page")
        self.price_label_at_pay_page.setFont(font2)
        self.price_label_at_pay_page.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.price_label_at_pay_page.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.gridLayout_5.addWidget(self.price_label_at_pay_page, 3, 0, 1, 1)
        self.amount_doubleSpinBox_at_pay_page = QSpinBox(self.pay_page)
        self.amount_doubleSpinBox_at_pay_page.setObjectName(u"amount_doubleSpinBox_at_pay_page")
        self.amount_doubleSpinBox_at_pay_page.setMinimumSize(QSize(0, 31))
        self.amount_doubleSpinBox_at_pay_page.setFont(font3)
        self.amount_doubleSpinBox_at_pay_page.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.amount_doubleSpinBox_at_pay_page.setMaximum(999999)
        self.gridLayout_5.addWidget(self.amount_doubleSpinBox_at_pay_page, 4, 0, 1, 1)
        self.date_label_at_pay_page = QLabel(self.pay_page)
        self.date_label_at_pay_page.setObjectName(u"date_label_at_pay_page")
        self.date_label_at_pay_page.setFont(font2)
        self.date_label_at_pay_page.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.date_label_at_pay_page.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.gridLayout_5.addWidget(self.date_label_at_pay_page, 5, 0, 1, 1)
        self.date_QDateEdit_at_pay_page = QDateEdit(self.pay_page)
        self.date_QDateEdit_at_pay_page.setObjectName(u"date_QDateEdit_at_pay_page")
        sizePolicy3.setHeightForWidth(self.date_QDateEdit_at_pay_page.sizePolicy().hasHeightForWidth())
        self.date_QDateEdit_at_pay_page.setSizePolicy(sizePolicy3)
        self.date_QDateEdit_at_pay_page.setMinimumSize(QSize(0, 31))
        self.date_QDateEdit_at_pay_page.setFont(font3)
        self.date_QDateEdit_at_pay_page.setAcceptDrops(True)
        # if QT_CONFIG(statustip)
        self.date_QDateEdit_at_pay_page.setStatusTip(u"")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(accessibility)
        self.date_QDateEdit_at_pay_page.setAccessibleName(u"")
        # endif // QT_CONFIG(accessibility)
        self.date_QDateEdit_at_pay_page.setAutoFillBackground(True)
        self.date_QDateEdit_at_pay_page.setStyleSheet(u"color: rgb(145, 145, 0);" 'font: 905 12pt "Calibri";')
        self.date_QDateEdit_at_pay_page.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.date_QDateEdit_at_pay_page.setSpecialValueText(u"")
        self.date_QDateEdit_at_pay_page.setDateTime(QDateTime.currentDateTime())
        self.date_QDateEdit_at_pay_page.setCurrentSection(QDateTimeEdit.DaySection)
        self.date_QDateEdit_at_pay_page.setDisplayFormat(u"dd/MM/yyyy")
        self.date_QDateEdit_at_pay_page.setCalendarPopup(True)
        self.gridLayout_5.addWidget(self.date_QDateEdit_at_pay_page, 6, 0, 1, 1)
        self.pay_supplier_btn = QPushButton(self.pay_page)
        self.pay_supplier_btn.setObjectName(u"pay_supplier_btn")
        self.pay_supplier_btn.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.pay_supplier_btn.sizePolicy().hasHeightForWidth())
        self.pay_supplier_btn.setSizePolicy(sizePolicy3)
        self.pay_supplier_btn.setMinimumSize(QSize(0, 60))
        self.pay_supplier_btn.setFont(font3)
        self.pay_supplier_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                            "background-color: rgb(92, 184, 78);")
        self.pay_supplier_btn.clicked.connect(lambda: self.make_payment())
        self.gridLayout_5.addWidget(self.pay_supplier_btn, 7, 0, 1, 1)
        self.stackedWidget.addWidget(self.pay_page)

        # Suppliers Page
        self.suppliers_page = QWidget()
        self.suppliers_page.setObjectName(u"suppliers_page")
        self.gridLayout_2 = QGridLayout(self.suppliers_page)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.insert_supplier_btn_at_suppliers_page = QPushButton(self.suppliers_page)
        self.insert_supplier_btn_at_suppliers_page.setObjectName(u"insert_supplier_btn_at_suppliers_page")
        self.insert_supplier_btn_at_suppliers_page.setMinimumSize(QSize(200, 60))
        font7 = QFont()
        font7.setFamily(u"Calibri")
        font7.setPointSize(13)
        font7.setBold(True)
        font7.setWeight(75)
        self.insert_supplier_btn_at_suppliers_page.setFont(font7)
        self.insert_supplier_btn_at_suppliers_page.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                                 "background-color: rgb(7, 114, 255);")
        self.insert_supplier_btn_at_suppliers_page.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.add_supplier_page))
        self.gridLayout_2.addWidget(self.insert_supplier_btn_at_suppliers_page, 5, 1, 1, 1)
        self.export_suppliers_btn_at_suppliers_page = QPushButton(self.suppliers_page)
        self.export_suppliers_btn_at_suppliers_page.setObjectName(u"export_suppliers_btn_at_suppliers_page")
        self.export_suppliers_btn_at_suppliers_page.setMinimumSize(QSize(200, 60))
        self.export_suppliers_btn_at_suppliers_page.setFont(font2)
        self.export_suppliers_btn_at_suppliers_page.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                                  "background-color: rgb(170, 85, 0);")
        self.export_suppliers_btn_at_suppliers_page.clicked.connect(lambda: self.extract(self.suppliers_tableWidget))
        self.gridLayout_2.addWidget(self.export_suppliers_btn_at_suppliers_page, 5, 0, 1, 1)
        self.suppliers_tableWidget = QTableWidget(self.suppliers_page)

        self.suppliers_tableWidget.setColumnCount(5)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setText(u"ID")
        __qtablewidgetitem9.setTextAlignment(Qt.AlignLeading | Qt.AlignVCenter)
        __qtablewidgetitem9.setFont(font4)
        self.suppliers_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem10.setFont(font3)
        self.suppliers_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem11.setFont(font3)
        self.suppliers_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem12.setFont(font3)
        self.suppliers_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem13.setFont(font3)
        self.suppliers_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem13)

        self.suppliers_tableWidget.setRowCount(len(self.suppliers))
        __qtablewidgetitem14 = QTableWidgetItem()
        self.suppliers_tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.suppliers_tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.suppliers_tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.suppliers_tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.suppliers_tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.suppliers_tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.suppliers_tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(0, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(0, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(0, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(0, 3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(1, 0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(1, 1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(1, 2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(1, 3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(1, 4, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(2, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(2, 1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(2, 2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(3, 0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(3, 1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(3, 2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(4, 0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(4, 1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(5, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(5, 1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(5, 2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(5, 4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(6, 0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.suppliers_tableWidget.setItem(6, 1, __qtablewidgetitem43)
        self.suppliers_tableWidget.setObjectName(u"suppliers_tableWidget")
        self.suppliers_tableWidget.setFont(font3)
        self.suppliers_tableWidget.setStyleSheet(u"alternate-background-color: rgb(100, 120, 180);")
        # self.suppliers_tableWidget.setStyleSheet(u"alternate-background-color: rgb(235, 235, 235);\n"
        #                                          "selection-color: rgb(255, 255, 255);\n"
        #                                          "selection-background-color: rgb(11, 170, 255);\n"
        #                                          "background-color: rgb(204, 204, 204);\n"
        #                                          "color: rgb(255, 85, 0);")
        self.suppliers_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.suppliers_tableWidget.setDragDropOverwriteMode(False)
        self.suppliers_tableWidget.setAlternatingRowColors(True)
        self.suppliers_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.suppliers_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.suppliers_tableWidget.setTextElideMode(Qt.ElideMiddle)
        self.suppliers_tableWidget.setShowGrid(True)
        self.suppliers_tableWidget.setGridStyle(Qt.SolidLine)
        self.suppliers_tableWidget.setSortingEnabled(True)
        self.suppliers_tableWidget.setWordWrap(True)
        self.suppliers_tableWidget.setCornerButtonEnabled(True)
        self.suppliers_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.suppliers_tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.suppliers_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.suppliers_tableWidget.verticalHeader().setVisible(False)
        self.suppliers_tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.suppliers_tableWidget.verticalHeader().setStretchLastSection(False)
        self.suppliers_tableWidget.setColumnWidth(0, 1)
        self.suppliers_tableWidget.setColumnWidth(1, 250)
        self.suppliers_tableWidget.setColumnWidth(2, 100)
        self.suppliers_tableWidget.setColumnWidth(3, 150)
        self.suppliers_tableWidget.setColumnWidth(4, 60)
        self.suppliers_tableWidget.doubleClicked.connect(lambda: self.edit_supplier(self.suppliers_tableWidget))

        self.gridLayout_2.addWidget(self.suppliers_tableWidget, 3, 0, 1, 2)
        self.suppliers_label = QLabel(self.suppliers_page)
        self.suppliers_label.setObjectName(u"suppliers_label")
        self.suppliers_label.setMinimumSize(QSize(0, 51))
        self.suppliers_label.setFont(font1)
        self.suppliers_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(85, 85, 255);")
        self.suppliers_label.setText(u"\u03a0\u03c1\u03bf\u03bc\u03b7\u03b8\u03b5\u03c5\u03c4\u03ad\u03c2")
        self.suppliers_label.setAlignment(Qt.AlignCenter)
        self.gridLayout_2.addWidget(self.suppliers_label, 1, 0, 1, 2)
        self.search_supplier_edit = QLineEdit(self.suppliers_page)
        self.search_supplier_edit.setObjectName(u"search_supplier_edit")
        self.search_supplier_edit.setMinimumSize(QSize(0, 31))
        self.search_supplier_edit.setFont(font3)
        self.search_supplier_edit.setStyleSheet(u"color: rgb(255, 255, 255);")
        # Autocomplete
        self.list_to_search_supplier = autocomplete(Suppliers)
        self.suppliers_completer = QCompleter(self.list_to_search_supplier)
        self.search_supplier_edit.setCompleter(self.suppliers_completer)
        # Enter
        self.search_supplier_edit.returnPressed.connect(lambda: self.update_suppliers(self.search_supplier_edit.text()))

        self.gridLayout_2.addWidget(self.search_supplier_edit, 2, 0, 1, 1)
        self.search_supplier_btn = QPushButton(self.suppliers_page)
        self.search_supplier_btn.setObjectName(u"search_supplier_btn")
        self.search_supplier_btn.setMinimumSize(QSize(0, 31))
        self.search_supplier_btn.setFont(font3)
        self.search_supplier_btn.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.search_supplier_btn.clicked.connect(lambda: self.update_suppliers(self.search_supplier_edit.text()))
        self.gridLayout_2.addWidget(self.search_supplier_btn, 2, 1, 1, 1)
        self.stackedWidget.addWidget(self.suppliers_page)

        # Recipients Page
        self.recipients_page = QWidget()
        self.recipients_page.setObjectName(u"recipients_page")
        self.gridLayout_4 = QGridLayout(self.recipients_page)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        # Προβολή παραληπτών

        self.export_recipients_btn_at_recipients_page = QPushButton(self.recipients_page)
        self.export_recipients_btn_at_recipients_page.setObjectName(u"export_recipients_btn_at_recipients_page")
        self.export_recipients_btn_at_recipients_page.setMinimumSize(QSize(200, 60))
        self.export_recipients_btn_at_recipients_page.setFont(font2)
        self.export_recipients_btn_at_recipients_page.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                                  "background-color: rgb(170, 85, 0);")
        self.export_recipients_btn_at_recipients_page.clicked.connect(lambda: self.extract(self.recipient_tableWidget))
        self.gridLayout_4.addWidget(self.export_recipients_btn_at_recipients_page, 5, 0, 1, 1)




        self.recipient_tableWidget = QTableWidget(self.recipients_page)

        self.recipient_tableWidget.setColumnCount(4)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignLeading | Qt.AlignVCenter)
        __qtablewidgetitem44.setFont(font3)
        self.recipient_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem45.setFont(font3)
        self.recipient_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem46.setFont(font3)
        self.recipient_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem47.setFont(font3)
        self.recipient_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem47)

        self.recipient_tableWidget.setRowCount(len(self.recipients))

        __qtablewidgetitem48 = QTableWidgetItem()
        self.recipient_tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.recipient_tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem49)
        self.recipient_tableWidget.setObjectName(u"recipient_tableWidget")
        self.recipient_tableWidget.setFont(font3)
        self.recipient_tableWidget.setStyleSheet(u"alternate-background-color: rgb(100, 120, 180);")
        # self.recipient_tableWidget.setStyleSheet(u"alternate-background-color: rgb(235, 235, 235);\n"
        #                                          "selection-color: rgb(255, 255, 255);\n"
        #                                          "selection-background-color: rgb(11, 170, 255);\n"
        #                                          "background-color: rgb(204, 204, 204);\n"
        #                                          "color: rgb(255, 85, 0);")
        self.recipient_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.recipient_tableWidget.setProperty("showDropIndicator", False)
        self.recipient_tableWidget.setDragDropOverwriteMode(False)
        self.recipient_tableWidget.setAlternatingRowColors(True)
        self.recipient_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.recipient_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.recipient_tableWidget.setTextElideMode(Qt.ElideMiddle)
        self.recipient_tableWidget.setGridStyle(Qt.SolidLine)
        self.recipient_tableWidget.setSortingEnabled(True)
        self.recipient_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.recipient_tableWidget.horizontalHeader().setDefaultSectionSize(176)
        self.recipient_tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.recipient_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.recipient_tableWidget.verticalHeader().setVisible(False)
        self.recipient_tableWidget.verticalHeader().setHighlightSections(False)
        self.recipient_tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.recipient_tableWidget.setColumnWidth(0, 1)
        self.recipient_tableWidget.setColumnWidth(1, 250)
        self.recipient_tableWidget.setColumnWidth(2, 150)
        self.recipient_tableWidget.setColumnWidth(3, 150)
        self.recipient_tableWidget.doubleClicked.connect(lambda: self.edit_recipient(self.recipient_tableWidget))

        self.gridLayout_4.addWidget(self.recipient_tableWidget, 3, 0, 1, 2)
        self.insert_recipient_btn_at_recipient_page = QPushButton(self.recipients_page)
        self.insert_recipient_btn_at_recipient_page.setObjectName(u"insert_recipient_btn_at_recipient_page")
        self.insert_recipient_btn_at_recipient_page.setMinimumSize(QSize(200, 60))
        self.insert_recipient_btn_at_recipient_page.setFont(font7)
        self.insert_recipient_btn_at_recipient_page.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                                  "background-color: rgb(7, 114, 255);")
        self.insert_recipient_btn_at_recipient_page.setText(u"Εισαγωγή παραλήπτη")
        self.insert_recipient_btn_at_recipient_page.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.add_recipient_page))
        self.gridLayout_4.addWidget(self.insert_recipient_btn_at_recipient_page, 5, 1, 1, 1)
        self.search_recipient_btn = QPushButton(self.recipients_page)
        self.search_recipient_btn.setObjectName(u"search_recipient_btn")
        self.search_recipient_btn.setMinimumSize(QSize(200, 31))
        self.search_recipient_btn.setFont(font3)
        self.search_recipient_btn.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.search_recipient_btn.setText(u"\u0391\u03bd\u03b1\u03b6\u03ae\u03c4\u03b7\u03c3\u03b7")
        self.search_recipient_btn.clicked.connect(lambda: self.update_recipients(self.search_recipient_edit.text()))
        self.gridLayout_4.addWidget(self.search_recipient_btn, 2, 1, 1, 1)
        self.search_recipient_edit = QLineEdit(self.recipients_page)
        self.search_recipient_edit.setObjectName(u"search_recipient_edit")
        self.search_recipient_edit.setMinimumSize(QSize(0, 31))
        self.search_recipient_edit.setFont(font3)
        self.search_recipient_edit.setStyleSheet(u"color: rgb(255, 255, 255);")
        # Autocomplete
        self.list_to_search_recipient = autocomplete(Recipients)

        self.recipient_completer = QCompleter(self.list_to_search_recipient)
        self.search_recipient_edit.setCompleter(self.recipient_completer)
        self.search_recipient_edit.returnPressed.connect(lambda: self.update_recipients(self.search_recipient_edit.text()))
        self.gridLayout_4.addWidget(self.search_recipient_edit, 2, 0, 1, 1)
        self.recipient_label_2 = QLabel(self.recipients_page)
        self.recipient_label_2.setObjectName(u"recipient_label_2")
        self.recipient_label_2.setMinimumSize(QSize(0, 51))
        self.recipient_label_2.setFont(font1)
        self.recipient_label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                             "background-color: rgb(85, 85, 255);")
        self.recipient_label_2.setText(u"\u03a0\u03b1\u03c1\u03b1\u03bb\u03ae\u03c0\u03c4\u03b5\u03c2")
        self.recipient_label_2.setAlignment(Qt.AlignCenter)
        self.gridLayout_4.addWidget(self.recipient_label_2, 1, 0, 1, 2)
        self.stackedWidget.addWidget(self.recipients_page)

        # Payments Page
        self.payments_page = QWidget()
        self.payments_page.setObjectName(u"payments_page")
        self.gridLayout_6 = QGridLayout(self.payments_page)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.payments_label = QLabel(self.payments_page)
        self.payments_label.setObjectName(u"payments_label")
        sizePolicy3.setHeightForWidth(self.payments_label.sizePolicy().hasHeightForWidth())
        self.payments_label.setSizePolicy(sizePolicy3)
        self.payments_label.setMinimumSize(QSize(0, 51))
        self.payments_label.setFont(font1)
        self.payments_label.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.payments_label.setAlignment(Qt.AlignCenter)
        self.gridLayout_6.addWidget(self.payments_label, 0, 0, 1, 3)
        self.search_payments_edit = QLineEdit(self.payments_page)
        self.search_payments_edit.setObjectName(u"search_payments_edit")
        self.search_payments_edit.setMinimumSize(QSize(0, 31))
        self.search_payments_edit.setFont(font3)
        # Autocomplete
        self.list_to_search_payments = autocomplete(Suppliers)
        self.payments_completer = QCompleter(self.list_to_search_payments)
        self.search_payments_edit.setCompleter(self.payments_completer)
        # bind enter key
        self.search_payments_edit.returnPressed.connect(lambda: self.update_payments(self.search_payments_edit.text()))

        self.gridLayout_6.addWidget(self.search_payments_edit, 1, 0, 1, 1)
        self.export_payments_btn = QPushButton(self.payments_page)
        self.export_payments_btn.setObjectName(u"export_payments_btn")
        self.export_payments_btn.setMinimumSize(QSize(0, 60))
        self.export_payments_btn.setFont(font2)
        self.export_payments_btn.setStyleSheet(u"background-color: rgb(170, 85, 0);")
        self.export_payments_btn.clicked.connect(lambda: self.extract(self.payments_tableWidget))
        self.gridLayout_6.addWidget(self.export_payments_btn, 3, 0, 1, 3)
        self.payments_tableWidget = QTableWidget(self.payments_page)

        self.payments_tableWidget.setColumnCount(4)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.payments_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem51.setFont(font3)
        self.payments_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem52.setFont(font3)
        self.payments_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem53.setFont(font3)
        self.payments_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem53)

        self.payments_tableWidget.setSortingEnabled(True)

        __qtablewidgetitem54 = QTableWidgetItem()
        self.payments_tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.payments_tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.payments_tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.payments_tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem57)
        self.payments_tableWidget.setObjectName(u"payments_tableWidget")
        sizePolicy5.setHeightForWidth(self.payments_tableWidget.sizePolicy().hasHeightForWidth())
        self.payments_tableWidget.setSizePolicy(sizePolicy5)
        self.payments_tableWidget.setFont(font3)
        self.payments_tableWidget.setStyleSheet(u"alternate-background-color: rgb(100, 120, 180);")
        # self.payments_tableWidget.setStyleSheet(u"alternate-background-color: rgb(235, 235, 235);\n"
        #                                         "selection-color: rgb(255, 255, 255);\n"
        #                                         "selection-background-color: rgb(11, 170, 255);\n"
        #                                         "background-color: rgb(204, 204, 204);\n"
        #                                         "color: rgb(255, 85, 0);")
        self.payments_tableWidget.setFrameShape(QFrame.StyledPanel)
        self.payments_tableWidget.setAlternatingRowColors(True)
        self.payments_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.payments_tableWidget.horizontalHeader().setDefaultSectionSize(176)
        self.payments_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.payments_tableWidget.verticalHeader().setVisible(False)
        self.payments_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.payments_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.payments_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.payments_tableWidget.setColumnWidth(0, 1)
        self.payments_tableWidget.setColumnWidth(1, 400)
        self.payments_tableWidget.setColumnWidth(2, 100)
        self.payments_tableWidget.setColumnWidth(3, 100)
        self.payments_tableWidget.doubleClicked.connect(lambda: self.edit_payment(self.payments_tableWidget))

        self.gridLayout_6.addWidget(self.payments_tableWidget, 2, 0, 1, 3)
        self.search_payments_btn = QPushButton(self.payments_page)
        self.search_payments_btn.setObjectName(u"search_payments_btn")
        self.search_payments_btn.setMinimumSize(QSize(200, 31))
        self.search_payments_btn.setFont(font3)
        self.search_payments_btn.clicked.connect(lambda: self.update_payments(self.search_payments_edit.text()))

        self.gridLayout_6.addWidget(self.search_payments_btn, 1, 1, 1, 2)
        self.stackedWidget.addWidget(self.payments_page)

        ################################################################################################################
        ###############                             Add supplier page                                             ######
        ################################################################################################################

        self.add_supplier_page = QWidget()
        self.add_supplier_page.setObjectName(u"add_supplier_page")
        self.gridLayout_8 = QGridLayout(self.add_supplier_page)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")

        # Supplier Name
        self.supplier_name_edit = QLineEdit(self.add_supplier_page)
        self.supplier_name_edit.setObjectName(u"supplier_name_edit")
        self.supplier_name_edit.setMinimumSize(QSize(0, 31))
        self.supplier_name_edit.setMaximumSize(QSize(16777215, 16777215))
        self.supplier_name_edit.setFont(font3)
        self.supplier_name_edit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayout_8.addWidget(self.supplier_name_edit, 1, 1, 1, 1)
        # Supplier vat nr
        self.supplier_vat_nr_edit = QLineEdit(self.add_supplier_page)
        self.supplier_vat_nr_edit.setObjectName(u"supplier_vat_nr_edit")
        self.supplier_vat_nr_edit.setMinimumSize(QSize(0, 31))
        self.supplier_vat_nr_edit.setMaximumSize(QSize(16777215, 16777215))
        self.supplier_vat_nr_edit.setFont(font3)
        self.supplier_vat_nr_edit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayout_8.addWidget(self.supplier_vat_nr_edit, 3, 1, 1, 1)
        # Supplier Phone
        self.supplier_phone_edit = QLineEdit(self.add_supplier_page)
        self.supplier_phone_edit.setObjectName(u"supplier_phone_edit")
        self.supplier_phone_edit.setMinimumSize(QSize(0, 31))
        self.supplier_phone_edit.setMaximumSize(QSize(16777215, 16777215))
        self.supplier_phone_edit.setFont(font3)
        self.supplier_phone_edit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayout_8.addWidget(self.supplier_phone_edit, 4, 1, 1, 1)
        # Supplier address
        self.supplier_address_edit = QLineEdit(self.add_supplier_page)
        self.supplier_address_edit.setObjectName(u"supplier_address_edit")
        self.supplier_address_edit.setMinimumSize(QSize(0, 31))
        self.supplier_address_edit.setMaximumSize(QSize(16777215, 16777215))
        self.supplier_address_edit.setFont(font3)
        self.supplier_address_edit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayout_8.addWidget(self.supplier_address_edit, 5, 1, 1, 1)
        # Supplier balance
        self.supplier_balance_edit = QSpinBox(self.add_supplier_page)
        self.supplier_balance_edit.setObjectName(u"supplier_balance_edit")
        self.supplier_balance_edit.setMinimumSize(QSize(0, 31))
        self.supplier_balance_edit.setFont(font3)
        self.supplier_balance_edit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.supplier_balance_edit.setMaximum(999999)
        self.gridLayout_8.addWidget(self.supplier_balance_edit, 7, 1, 1, 1)

        self.save_supplier_btn = QPushButton(self.add_supplier_page)
        self.save_supplier_btn.setObjectName(u"save_supplier_btn")
        self.save_supplier_btn.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.save_supplier_btn.sizePolicy().hasHeightForWidth())
        self.save_supplier_btn.setSizePolicy(sizePolicy3)
        self.save_supplier_btn.setMinimumSize(QSize(0, 60))
        self.save_supplier_btn.setFont(font3)
        self.save_supplier_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                             "background-color: rgb(92, 184, 78);")
        self.save_supplier_btn.clicked.connect(lambda: self.add_supplier())
        self.gridLayout_8.addWidget(self.save_supplier_btn, 9, 0, 1, 3)

        self.supplier_name_label = QLabel(self.add_supplier_page)
        self.supplier_name_label.setObjectName(u"supplier_name_label")
        self.supplier_name_label.setMinimumSize(QSize(0, 31))
        self.supplier_name_label.setFont(font3)
        self.supplier_name_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.supplier_name_label.setAlignment(Qt.AlignCenter)
        self.gridLayout_8.addWidget(self.supplier_name_label, 1, 0, 1, 1)

        self.supplier_address_label = QLabel(self.add_supplier_page)
        self.supplier_address_label.setObjectName(u"supplier_address_label")
        self.supplier_address_label.setMinimumSize(QSize(0, 31))
        self.supplier_address_label.setFont(font3)
        self.supplier_address_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.supplier_address_label.setAlignment(Qt.AlignCenter)
        self.gridLayout_8.addWidget(self.supplier_address_label, 5, 0, 1, 1)


        self.supplier_balance_label = QLabel(self.add_supplier_page)
        self.supplier_balance_label.setObjectName(u"supplier_balance_label")
        self.supplier_balance_label.setMinimumSize(QSize(0, 31))
        self.supplier_balance_label.setFont(font3)
        self.supplier_balance_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.supplier_balance_label.setAlignment(Qt.AlignCenter)
        self.gridLayout_8.addWidget(self.supplier_balance_label, 7, 0, 1, 1)

        self.vat_nr_label = QLabel(self.add_supplier_page)
        self.vat_nr_label.setObjectName(u"vat_nr_label")
        self.vat_nr_label.setMinimumSize(QSize(0, 31))
        self.vat_nr_label.setFont(font3)
        self.vat_nr_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.vat_nr_label.setAlignment(Qt.AlignCenter)
        self.gridLayout_8.addWidget(self.vat_nr_label, 3, 0, 1, 1)

        self.supplier_phone_label = QLabel(self.add_supplier_page)
        self.supplier_phone_label.setObjectName(u"supplier_phone_label")
        self.supplier_phone_label.setMinimumSize(QSize(0, 31))
        self.supplier_phone_label.setFont(font3)
        self.supplier_phone_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.supplier_phone_label.setAlignment(Qt.AlignCenter)
        self.gridLayout_8.addWidget(self.supplier_phone_label, 4, 0, 1, 1)

        self.insert_supplier_label = QLabel(self.add_supplier_page)
        self.insert_supplier_label.setObjectName(u"insert_supplier_label")
        self.insert_supplier_label.setMinimumSize(QSize(0, 51))
        self.insert_supplier_label.setMaximumSize(QSize(16777215, 51))
        self.insert_supplier_label.setFont(font1)
        self.insert_supplier_label.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.insert_supplier_label.setText(u"Εισαγωγή προμηθευτή")
        self.insert_supplier_label.setAlignment(Qt.AlignCenter)
        self.gridLayout_8.addWidget(self.insert_supplier_label, 0, 0, 1, 3)
        self.stackedWidget.addWidget(self.add_supplier_page)

        ################################################################################################################
        ###############                             Finish Add supplier page                                      ######
        ################################################################################################################
        ################################################################################################################
        ###############                             Add recipient page                                             ######
        ################################################################################################################

        self.add_recipient_page = QWidget()
        self.add_recipient_page.setObjectName(u"add_recipient_page")
        self.gridLayout_9 = QGridLayout(self.add_recipient_page)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")

        # Recipient Name
        self.recipient_name_edit = QLineEdit(self.add_recipient_page)
        self.recipient_name_edit.setObjectName(u"recipient_name_edit")
        self.recipient_name_edit.setMinimumSize(QSize(0, 31))
        self.recipient_name_edit.setMaximumSize(QSize(16777215, 16777215))
        self.recipient_name_edit.setFont(font3)
        self.recipient_name_edit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayout_9.addWidget(self.recipient_name_edit, 1, 1, 1, 1)
        # Recipient Phone
        self.recipient_phone_edit = QLineEdit(self.add_recipient_page)
        self.recipient_phone_edit.setObjectName(u"recipient_phone_edit")
        self.recipient_phone_edit.setMinimumSize(QSize(0, 31))
        self.recipient_phone_edit.setMaximumSize(QSize(16777215, 16777215))
        self.recipient_phone_edit.setFont(font3)
        self.recipient_phone_edit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayout_9.addWidget(self.recipient_phone_edit, 2, 1, 1, 1)
        # Recipient address
        self.recipient_address_edit = QLineEdit(self.add_recipient_page)
        self.recipient_address_edit.setObjectName(u"recipient_address_edit")
        self.recipient_address_edit.setMinimumSize(QSize(0, 31))
        self.recipient_address_edit.setMaximumSize(QSize(16777215, 16777215))
        self.recipient_address_edit.setFont(font3)
        self.recipient_address_edit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayout_9.addWidget(self.recipient_address_edit, 3, 1, 1, 1)

        self.save_recipient_btn = QPushButton(self.add_recipient_page)
        self.save_recipient_btn.setObjectName(u"save_recipient_btn")
        self.save_recipient_btn.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.save_recipient_btn.sizePolicy().hasHeightForWidth())
        self.save_recipient_btn.setSizePolicy(sizePolicy3)
        self.save_recipient_btn.setMinimumSize(QSize(0, 60))
        self.save_recipient_btn.setFont(font3)
        self.save_recipient_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                             "background-color: rgb(92, 184, 78);")
        self.save_recipient_btn.clicked.connect(lambda: self.add_recipient())
        self.gridLayout_9.addWidget(self.save_recipient_btn, 9, 0, 1, 3)

        self.recipient_name_label = QLabel(self.add_recipient_page)
        self.recipient_name_label.setObjectName(u"recipient_name_label")
        self.recipient_name_label.setMinimumSize(QSize(0, 31))
        self.recipient_name_label.setFont(font3)
        self.recipient_name_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.recipient_name_label.setAlignment(Qt.AlignCenter)
        self.gridLayout_9.addWidget(self.recipient_name_label, 1, 0, 1, 1)

        self.recipient_address_label = QLabel(self.add_recipient_page)
        self.recipient_address_label.setObjectName(u"recipient_address_label")
        self.recipient_address_label.setMinimumSize(QSize(0, 31))
        self.recipient_address_label.setFont(font3)
        self.recipient_address_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.recipient_address_label.setAlignment(Qt.AlignCenter)
        self.gridLayout_9.addWidget(self.recipient_address_label, 3, 0, 1, 1)

        self.recipient_phone_label = QLabel(self.add_recipient_page)
        self.recipient_phone_label.setObjectName(u"recipient_phone_label")
        self.recipient_phone_label.setMinimumSize(QSize(0, 31))
        self.recipient_phone_label.setFont(font3)
        self.recipient_phone_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.recipient_phone_label.setAlignment(Qt.AlignCenter)
        self.gridLayout_9.addWidget(self.recipient_phone_label, 2, 0, 1, 1)

        self.insert_recipient_label = QLabel(self.add_recipient_page)
        self.insert_recipient_label.setObjectName(u"insert_recipient_label")
        self.insert_recipient_label.setMinimumSize(QSize(0, 51))
        self.insert_recipient_label.setMaximumSize(QSize(16777215, 51))
        self.insert_recipient_label.setFont(font1)
        self.insert_recipient_label.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.insert_recipient_label.setText(u"Εισαγωγή παραλήπτη")
        self.insert_recipient_label.setAlignment(Qt.AlignCenter)
        self.gridLayout_9.addWidget(self.insert_recipient_label, 0, 0, 1, 3)
        self.stackedWidget.addWidget(self.add_recipient_page)

        ################################################################################################################
        ###############                             Finish Add recipient page                                      ######
        ################################################################################################################
        self.gridLayout_3.addWidget(self.stackedWidget, 0, 2, 8, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        # Menu Bar
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 843, 21))
        palette = QPalette()
        brush = QBrush(QColor(229, 249, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(55, 88, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush2 = QBrush(QColor(160, 161, 162, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.menubar.setPalette(palette)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.actionInfo = QAction(MainWindow)
        self.actionInfo.setObjectName(u"actionInfo")
        self.actionInfo.triggered.connect(lambda: self.show_info())


        palette1 = QPalette()
        brush3 = QBrush(QColor(255, 255, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush4 = QBrush(QColor(229, 249, 255, 128))
        brush4.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
        # endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush5 = QBrush(QColor(229, 249, 255, 128))
        brush5.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
        # endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        brush6 = QBrush(QColor(168, 169, 169, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush7 = QBrush(QColor(229, 249, 255, 128))
        brush7.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
        # endif
        self.menu.setPalette(palette1)
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu.menuAction())


        self.retranslateUi(MainWindow)

        self.purchases_btn.setDefault(False)
        self.stackedWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", f"Εξοδα {version}", None))
        self.import_btn.setText(
            QCoreApplication.translate("MainWindow", u"Εισαγωγή", None))
        self.pay_btn.setText(
            QCoreApplication.translate("MainWindow", u"Πληρωμή", None))
        self.purchases_btn.setText(
            QCoreApplication.translate("MainWindow", u"\u0391\u03b3\u03bf\u03c1\u03ad\u03c2", None))
        self.suppliers_btn.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u03a0\u03c1\u03bf\u03bc\u03b7\u03b8\u03b5\u03c5\u03c4\u03ad\u03c2",
                                                              None))
        self.recipients_btn.setText(
            QCoreApplication.translate("MainWindow", u"\u03a0\u03b1\u03c1\u03b1\u03bb\u03ae\u03c0\u03c4\u03b5\u03c2",
                                       None))
        self.payments_btn.setText(
            QCoreApplication.translate("MainWindow", u"\u03a0\u03bb\u03b7\u03c1\u03c9\u03bc\u03ad\u03c2", None))
        self.purchases_label.setText(
            QCoreApplication.translate("MainWindow", u"\u0391\u03b3\u03bf\u03c1\u03ad\u03c2", None))
        self.export_purchases_btn.setText(
            QCoreApplication.translate("MainWindow", u"\u0395\u03be\u03b1\u03b3\u03c9\u03b3\u03ae", None))
        self.search_purchases_btn.setText(
            QCoreApplication.translate("MainWindow", u"\u0391\u03bd\u03b1\u03b6\u03ae\u03c4\u03b7\u03c3\u03b7", None))
        self.search_purchases_edit.setText("")
        ___qtablewidgetitem = self.purchases_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.purchases_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u03a0\u03c1\u03bf\u03bc\u03b7\u03b8\u03b5\u03c5\u03c4\u03ae\u03c2",
                                                                None));
        ___qtablewidgetitem2 = self.purchases_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", u"\u03a0\u03c1\u03bf\u03b9\u03cc\u03bd", None));
        ___qtablewidgetitem3 = self.purchases_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u03a4\u03b9\u03bc\u03ae", None));
        ___qtablewidgetitem4 = self.purchases_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("MainWindow", u"\u03a0\u03b1\u03c1\u03b1\u03bb\u03ae\u03c0\u03c4\u03b7\u03c2",
                                       None));
        ___qtablewidgetitem5 = self.purchases_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("MainWindow", u"\u0397\u03bc\u03b5\u03c1\u03bf\u03bc\u03b7\u03bd\u03af\u03b1",
                                       None))

        self.product_description_label.setText(QCoreApplication.translate("MainWindow",
                                                                          u"\u03a0\u03b5\u03c1\u03b9\u03b3\u03c1\u03b1\u03c6\u03ae \u03c0\u03c1\u03bf\u03b9\u03cc\u03bd\u03c4\u03bf\u03c2",
                                                                          None))
        self.add_file_btn.setText(QCoreApplication.translate("MainWindow", u"Προσθήκη αρχείου", None))
        self.invoice_label.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u0391\u03c1\u03b9\u03b8\u03bc\u03cc\u03c2 \u03c4\u03b9\u03bc\u03bf\u03bb\u03bf\u03b3\u03af\u03bf\u03c5",
                                                              None))
        self.insert_recipier_btn.setText(QCoreApplication.translate("MainWindow",
                                                                    u"\u0395\u03b9\u03c3\u03b1\u03b3\u03c9\u03b3\u03ae \u03c0\u03b1\u03c1\u03b1\u03bb\u03ae\u03c0\u03c4\u03b7",
                                                                    None))
        self.amount_doubleSpinBox_at_import_page.setSuffix(QCoreApplication.translate("MainWindow", u" \u20ac", None))
        self.date_label.setText(
            QCoreApplication.translate("MainWindow", u"\u0397\u03bc\u03b5\u03c1\u03bf\u03bc\u03b7\u03bd\u03af\u03b1",
                                       None))
        self.insert_supplier_btn.setText(QCoreApplication.translate("MainWindow",
                                                                    u"\u0395\u03b9\u03c3\u03b1\u03b3\u03c9\u03b3\u03ae \u03c0\u03c1\u03bf\u03bc\u03b7\u03b8\u03b5\u03c5\u03c4\u03ae",
                                                                    None))
        self.recipient_label.setText(
            QCoreApplication.translate("MainWindow", u"\u03a0\u03b1\u03c1\u03b1\u03bb\u03ae\u03c0\u03c4\u03b7\u03c2",
                                       None))
        self.price_label.setText(QCoreApplication.translate("MainWindow", u"\u03a0\u03bf\u03c3\u03cc \u20ac ", None))
        self.supplier_label.setText(QCoreApplication.translate("MainWindow",
                                                               u"\u0395\u03c0\u03b9\u03bb\u03bf\u03b3\u03ae \u03a0\u03c1\u03bf\u03bc\u03b7\u03b8\u03b5\u03c5\u03c4\u03ae",
                                                               None))
        self.save_btn.setText(
            QCoreApplication.translate("MainWindow", u"\u0391\u03c0\u03bf\u03b8\u03ae\u03ba\u03b5\u03c5\u03c3\u03b7",
                                       None))
        self.pay_supplier_label.setText(QCoreApplication.translate("MainWindow",
                                                                   u"\u03a0\u03bb\u03b7\u03c1\u03c9\u03bc\u03ae \u03c0\u03c1\u03bf\u03bc\u03b7\u03b8\u03b5\u03c5\u03c4\u03ae",
                                                                   None))
        self.supplier_label_at_pay_page.setText(QCoreApplication.translate("MainWindow",
                                                                           u"\u0395\u03c0\u03b9\u03bb\u03bf\u03b3\u03ae \u03a0\u03c1\u03bf\u03bc\u03b7\u03b8\u03b5\u03c5\u03c4\u03ae",
                                                                           None))
        self.price_label_at_pay_page.setText(
            QCoreApplication.translate("MainWindow", u"\u03a0\u03bf\u03c3\u03cc \u20ac ", None))
        self.amount_doubleSpinBox_at_pay_page.setSuffix(QCoreApplication.translate("MainWindow", u" \u20ac", None))
        self.date_label_at_pay_page.setText(
            QCoreApplication.translate("MainWindow", u"\u0397\u03bc\u03b5\u03c1\u03bf\u03bc\u03b7\u03bd\u03af\u03b1",
                                       None))
        self.pay_supplier_btn.setText(
            QCoreApplication.translate("MainWindow", u"\u03a0\u03bb\u03b7\u03c1\u03c9\u03bc\u03ae", None))
        self.insert_supplier_btn_at_suppliers_page.setText(QCoreApplication.translate("MainWindow",
                                                                                      u"\u0395\u03b9\u03c3\u03b1\u03b3\u03c9\u03b3\u03ae \u03c0\u03c1\u03bf\u03bc\u03b7\u03b8\u03b5\u03c5\u03c4\u03ae",
                                                                                      None))
        self.export_suppliers_btn_at_suppliers_page.setText(
            QCoreApplication.translate("MainWindow", u"Εξαγωγή", None))
        self.export_recipients_btn_at_recipients_page.setText(QCoreApplication.translate("MainWindow", u"Εξαγωγή", None))
        ___qtablewidgetitem9 = self.suppliers_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(
            QCoreApplication.translate("MainWindow", u"\u0395\u03c0\u03c9\u03bd\u03c5\u03bc\u03af\u03b1", None));
        ___qtablewidgetitem10 = self.suppliers_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u0391.\u03a6.\u039c.", None));
        ___qtablewidgetitem11 = self.suppliers_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(
            QCoreApplication.translate("MainWindow", u"\u03a4\u03b7\u03bb\u03ad\u03c6\u03c9\u03bd\u03bf", None));
        ___qtablewidgetitem12 = self.suppliers_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(
            QCoreApplication.translate("MainWindow", u"\u03a5\u03c0\u03cc\u03bb\u03bf\u03b9\u03c0\u03bf", None));

        __sortingEnabled = self.suppliers_tableWidget.isSortingEnabled()
        self.suppliers_tableWidget.setSortingEnabled(True)
        self.suppliers_tableWidget.setSortingEnabled(__sortingEnabled)

        self.search_supplier_btn.setText(
            QCoreApplication.translate("MainWindow", u"\u0391\u03bd\u03b1\u03b6\u03ae\u03c4\u03b7\u03c3\u03b7", None))
        ___qtablewidgetitem36 = self.recipient_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        ___qtablewidgetitem37 = self.recipient_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow",
                                                                 u"\u039f\u03bd\u03bf\u03bc\u03b1\u03c4\u03b5\u03c0\u03ce\u03bd\u03c5\u03bc\u03bf",
                                                                 None));
        ___qtablewidgetitem38 = self.recipient_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem38.setText(
            QCoreApplication.translate("MainWindow", u"\u03a4\u03b7\u03bb\u03ad\u03c6\u03c9\u03bd\u03bf", None));
        ___qtablewidgetitem39 = self.recipient_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem39.setText(
            QCoreApplication.translate("MainWindow", u"\u0394\u03b9\u03b5\u03cd\u03b8\u03c5\u03bd\u03c3\u03b7", None));

        self.payments_label.setText(
            QCoreApplication.translate("MainWindow", u"\u03a0\u03bb\u03b7\u03c1\u03c9\u03bc\u03ad\u03c2", None))
        self.export_payments_btn.setText(
            QCoreApplication.translate("MainWindow", u"\u0395\u03be\u03b1\u03b3\u03c9\u03b3\u03ae", None))
        ___qtablewidgetitem42 = self.payments_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        ___qtablewidgetitem43 = self.payments_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Προμηθευτής", None))
        ___qtablewidgetitem44 = self.payments_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Ποσό", None))
        ___qtablewidgetitem45 = self.payments_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Ημερομηνία", None))

        self.search_payments_btn.setText(
            QCoreApplication.translate("MainWindow", u"\u0391\u03bd\u03b1\u03b6\u03ae\u03c4\u03b7\u03c3\u03b7", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))

        # Insert Supplier page
        self.save_supplier_btn.setText(QCoreApplication.translate("MainWindow", u"Αποθήκευση",  None))
        self.supplier_name_label.setText(QCoreApplication.translate("MainWindow", u"Ονοματεπώνυμο", None))
        self.supplier_address_label.setText(QCoreApplication.translate("MainWindow", u"Διεύθυνση", None))
        self.supplier_balance_edit.setSuffix(QCoreApplication.translate("MainWindow", u"", None))
        self.supplier_balance_label.setText(QCoreApplication.translate("MainWindow", u"Υπόλοιπο", None))
        self.vat_nr_label.setText(QCoreApplication.translate("MainWindow", u"Α.Φ.Μ.", None))
        self.supplier_phone_label.setText(QCoreApplication.translate("MainWindow", u"Τηλέφωνο", None))
        # Insert Recipient page
        # Insert Supplier page
        self.save_recipient_btn.setText(QCoreApplication.translate("MainWindow", u"Αποθήκευση", None))
        self.recipient_name_label.setText(QCoreApplication.translate("MainWindow", u"Ονοματεπώνυμο", None))
        self.recipient_address_label.setText(QCoreApplication.translate("MainWindow", u"Διεύθυνση", None))
        self.recipient_phone_label.setText(QCoreApplication.translate("MainWindow", u"Τηλέφωνο", None))
        self.actionInfo.setText(QCoreApplication.translate("MainWindow", u"Info", None))

    # retranslateUi

    # Update Suppliers
    def update_suppliers(self, search_string=None):
        # Πρώτα αδειάζουμε τον  πίνακα
        self.suppliers_tableWidget.setRowCount(0)

        self.suppliers = get_data(Suppliers)
        # Αποκόμηση νέων δεδομένων
        # Αποκόμηση νέων δεδομένων και ελεγχος αν είναι απο αναζήτηση
        if search_string:
            self.suppliers = Session.query(Suppliers).filter(
                Suppliers.name.like(search_string) |
                (Suppliers.vat_nr.like(search_string)) |
                (Suppliers.phone.like(search_string)) |
                (Suppliers.address.like(search_string)) |
                (Suppliers.balance.like(search_string))).all()

        # Ορισμός γραμμων
        self.suppliers_tableWidget.setRowCount(len(self.suppliers))
        # Εισαγωγή δεδομένων
        # Προβολή προμηθευτών
        for row, data in enumerate(self.suppliers):
            _id = QTableWidgetItem(data.id)
            _id.setData(Qt.DisplayRole, int(data.id))
            self.suppliers_tableWidget.setItem(row, 0, _id)

            name = QTableWidgetItem(str(data.name))
            self.suppliers_tableWidget.setItem(row, 1, name)

            vat_nr = QTableWidgetItem(str(data.vat_nr))
            vat_nr.setData(Qt.DisplayRole, int(data.vat_nr))
            self.suppliers_tableWidget.setItem(row, 2, vat_nr)

            phone = QTableWidgetItem(str(data.phone))
            phone.setData(Qt.DisplayRole, data.phone)
            self.suppliers_tableWidget.setItem(row, 3, phone)

            balance = QTableWidgetItem(data.balance)
            balance.setData(Qt.DisplayRole, int(data.balance))
            self.suppliers_tableWidget.setItem(row, 4, balance)
        # Ενημέρωση του view
        self.suppliers_tableWidget.viewport().update()

    # Update Recipients
    def update_recipients(self, search_string=None):
        # Πρώτα αδειάζουμε τον  πίνακα
        self.recipient_tableWidget.setRowCount(0)
        # Αποκόμηση νέων δεδομένων
        # Αποκόμηση νέων δεδομένων και ελεγχος αν είναι απο αναζήτηση
        if search_string:
            self.recipients = Session.query(Recipients).filter(
                Recipients.name.like(search_string) |
                (Recipients.phone.like(search_string)) |
                (Recipients.address.like(search_string))).all()
        else:
            self.recipients = get_data(Recipients)
        # Ορισμός γραμμων
        self.recipient_tableWidget.setRowCount(len(self.recipients))
        # Εισαγωγή δεδομένων
        # Προβολή παραληπτών
        for row, data in enumerate(self.recipients):
            _id = QTableWidgetItem(data.id)
            _id.setData(Qt.DisplayRole, int(data.id))
            self.recipient_tableWidget.setItem(row, 0, _id)

            name = QTableWidgetItem(str(data.name))
            self.recipient_tableWidget.setItem(row, 1, name)

            phone = QTableWidgetItem(str(data.phone))

            phone.setData(Qt.DisplayRole, data.phone)
            self.recipient_tableWidget.setItem(row, 2, phone)

            address = QTableWidgetItem(str(data.address))
            self.recipient_tableWidget.setItem(row, 3, address)

        # Ενημέρωση του view
        self.recipient_tableWidget.viewport().update()

    # Update Purchases
    def update_purchases(self, search_string=None):
        # Πρώτα αδειάζουμε τον  πίνακα
        self.purchases_tableWidget.setRowCount(0)
        # Αποκόμηση νέων δεδομένων και ελεγχος αν είναι απο αναζήτηση
        if search_string:
            self.purchases = Session.query(Purchases).join(Suppliers, Recipients).filter(
                Suppliers.name.like(search_string) |
                (Suppliers.phone.like(search_string)) |
                (Recipients.name.like(search_string)) |
                (Recipients.phone.like(search_string)) |
                (Purchases.price.like(search_string)) |
                (Purchases.product.like(search_string)) |
                (Purchases.date.like(search_string))).all()
        else:
            # Διαφορετικά είναι απο ενημέρωση πίνακα
            self.purchases = get_data(Purchases)

        # Ορισμός γραμμων
        self.purchases_tableWidget.setRowCount(len(self.purchases))
        # Εισαγωγή δεδομένων
        for row, data in enumerate(self.purchases):
            _id = QTableWidgetItem(str(data.id))
            _id.setData(Qt.DisplayRole, int(data.id))
            self.purchases_tableWidget.setItem(row, 0, _id)
            # Προμηθευτής
            supplier = QTableWidgetItem(str(data.supplier))
            self.purchases_tableWidget.setItem(row, 1, supplier)
            # Προιόν
            product = QTableWidgetItem(str(data.product))
            self.purchases_tableWidget.setItem(row, 2, product)
            # Τιμή
            price = QTableWidgetItem(str(data.price))
            price.setData(Qt.DisplayRole, data.price)
            self.purchases_tableWidget.setItem(row, 3, price)
            # Παραλήπτης
            recipient = QTableWidgetItem(str(data.recipient))
            self.purchases_tableWidget.setItem(row, 4, recipient)
            # Ημερομηνία
            date = QTableWidgetItem(str(data.date))
            QDate_obj = QDate.fromString(data.date, "d/M/yyyy")
            date.setData(Qt.DisplayRole, QDate_obj)
            self.purchases_tableWidget.setItem(row, 5, date)
        # Ενημέρωση του view
        self.purchases_tableWidget.viewport().update()

    # Update Payments
    def update_payments(self, search_string=None):
        # Πρώτα αδειάζουμε τον πίνακα
        self.payments_tableWidget.setRowCount(0)
        # Αποκόμηση νέων δεδομένων και ελεγχος αν είναι απο αναζήτηση
        if search_string:
            self.payments = Session.query(Payments).join(Suppliers).filter(
                Suppliers.name.like(search_string) |
                (Suppliers.phone.like(search_string)) |
                (Payments.amount.like(search_string)) |
                (Payments.date.like(search_string))).all()
        else:
            # Διαφορετικά είναι απο ενημέρωση πίνακα
            self.payments = get_data(Payments)
        # Ορισμός γραμμων
        self.payments_tableWidget.setRowCount(len(self.payments))
        # Προβολή πληρωμών
        for row, data in enumerate(self.payments):
            _id = QTableWidgetItem(str(data.id))
            _id.setData(Qt.DisplayRole, int(data.id))
            self.payments_tableWidget.setItem(row, 0, _id)
            supplier = QTableWidgetItem(str(data.supplier))
            self.payments_tableWidget.setItem(row, 1, supplier)

            # Amount
            amount = QTableWidgetItem(str(data.amount))
            amount.setData(Qt.DisplayRole, int(data.amount))
            self.payments_tableWidget.setItem(row, 2, amount)

            # Date
            date = QTableWidgetItem(str(data.date))
            QDate_obj = QDate.fromString(data.date, "d/M/yyyy")
            date.setData(Qt.DisplayRole, QDate_obj)
            self.payments_tableWidget.setItem(row, 3, date)

        # Ενημέρωση του view
        self.payments_tableWidget.viewport().update()

    # Αποθήκευση τιμπολογίου - αγοράς
    def save_import(self):

        supplier_name = self.supplier_qcompobox.currentText()
        if supplier_name == "":
            msgBox = QMessageBox.critical(None, "Πρόβλημα", "Παρακαλώ ορίστε προμηθευτή!")
            return
        invoice_nr = self.invoice_edit.text()
        date = self.date_edit.date().toPython().strftime("%#d/%#m/%Y")

        recipient_name = self.recipient_comboBox.currentText()
        if recipient_name == "":
            msgBox = QMessageBox.critical(None, "Πρόβλημα", "Παρακαλώ ορίστε παραλήπτη!")
            return
        amount = int(self.amount_doubleSpinBox_at_import_page.text()[:-1])   # το τελευταίο είναι το € δεν το θελουμε
        if amount == 0 or amount == "":
            msgBox = QMessageBox.warning(None, "Πρόβλημα", "Παρακαλώ ορίστε ποσό!")
            return
        product = self.product_description_plainTextEdit.toPlainText()
        try:
            # Ευρεση id προμηθευτή με βάση το όνομα
            supplier = Session.query(Suppliers).filter_by(name=supplier_name).one_or_none()

            supplier_id = supplier.id
        except AttributeError:  # Αν δεν υπάρχει αυτό το όνομα 'NoneType' object has no attribute 'id'
            msgBox = QMessageBox.critical(None, "Πρόβλημα", f"Ο προμηθευτής {supplier_name} δεν υπάρχει")
            return
        # Ελεγχος αν το όνομα υπάρχει πολλές φορές
        except MultipleResultsFound:
            msgBox = QMessageBox.critical(None, "Πρόβλημα", f"Το ονομά του προμηθευτή {supplier_name} υπάρχει πολλές "
                                                            f"φορές")
            return

        try:
            # Ευρεση id παραλήπτη με βάση το όνομα
            recipient = Session.query(Recipients).filter_by(name=recipient_name).one_or_none()
            recipient_id = recipient.id
        except AttributeError:  # Αν δεν υπάρχει αυτό το όνομα 'NoneType' object has no attribute 'id'
            msgBox = QMessageBox.critical(None, "Πρόβλημα", f"Ο παραλήπτης '{recipient_name}' δεν υπάρχει")
            return
        # Ελεγχος αν ο χρήστης εχει επιλέξει αρχείο
        if self.filename:
            self.files_path = "files" + "/" + supplier.name + "/" + str(datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")) + "/"

            # Δημηουργία φακέλου για το αρχείο
            if not os.path.exists(self.files_path):
                os.makedirs(self.files_path, exist_ok=True)
            #  Returns the absolute path to the newly created file.
            # If follow_symlinks is false, and src is a symbolic link, dst will be created as a symbolic link.
            # If follow_symlinks is true and src is a symbolic link, dst will be a copy of the file src refers to.
            file_to_add = os.path.abspath(shutil.copy(self.filename, self.files_path, follow_symlinks=True))

        else:
            file_to_add = None

        item = Purchases(supplier_id=supplier_id, invoice=invoice_nr, recipient_id=recipient_id, price=amount,
                         product=product, date=date, file=file_to_add)
        Session.add(item)

        supplier.balance += int(amount)
        Session.add(supplier)
        Session.commit()

        # Προσθήκη αγοράς στον πίνακα Purchases
        print(40 * "#", "Αποθήκευση τιμολογίου - αγοράς", 40 * "#")
        print(f"Προμηθευτής '{supplier_name}' Αριθμός τιμολογίου '{invoice_nr}' Παραλήπτης '{recipient_name}' "
              f"Τιμή '{amount}' Προιόν '{product}' Ημερομηνία αγοράς '{date}' Αρχείο '{file_to_add}'")
        print(40 * "#", "Save Done", 40 * "#")

        self.filename = None
        self.files_path = None
        self.add_file_btn.setStyleSheet(u"background-color: rgb(170, 85, 0); color: rgb(255, 255, 255);")
        self.add_file_btn.setText(QCoreApplication.translate("MainWindow", u"Προσθήκη αρχείου", None))

        msgBox = QMessageBox.information(None, "Πληροφορία", f"Η αγορά απο προμηθευτή {supplier.name} ολοκληρώθηκε.")

    # Πληρωμή προμηθευτή
    def make_payment(self):
        # επιλεγμένος προμηθευτής για πληρωμή
        supplier_name = self.supplier_qcompobox_at_pay_page.currentText()
        # Ελεγχος αν εχουμε επιλέξει προμηθευτή
        if supplier_name == "":
            msgBox = QMessageBox.warning(None, "Πρόβλημα", "Παρακαλώ ορίστε προμηθευτή!")
            return

        try:
            supplier = Session.query(Suppliers).filter_by(name=supplier_name).one_or_none()
            supplier_id = supplier.id
        except AttributeError:  # 'NoneType' object has no attribute 'id'
            msgBox = QMessageBox.critical(None, "Πρόβλημα", f"O προμηθευτής {supplier_name} δεν υπάρχει!")
            return
        except MultipleResultsFound:
            msgBox = QMessageBox.critical(None, "Πρόβλημα", f"Το όνομα του προμηθευτή {supplier_name} υπάρχει πολλές φορές!")
            return
        # Ελεγχος αν βάλαμε ποσό για πληρωμή
        amount = int(self.amount_doubleSpinBox_at_pay_page.text()[:-1])  # το τελευταίο είναι το € δεν το θελουμε
        if amount == 0 or amount == "":
            msgBox = QMessageBox.warning(None, "Πρόβλημα", "Παρακαλώ ορίστε ποσό πληρωμής!")
            return

        amount = self.amount_doubleSpinBox_at_pay_page.text()[:-1]  # το τελευταίο είναι το € δεν το θελουμε
        date = self.date_QDateEdit_at_pay_page.date().toPython().strftime("%#d/%#m/%Y")

        # Αφαίρεση ποσού απο τον προμηθευτή
        current_balance = int(supplier.balance)
        new_balance = int(current_balance) - int(amount)
        supplier.balance = new_balance
        Session.add(supplier)
        Session.commit()
        print("*" * 40, "Πληρωμή", "*" * 40)
        print(f"Προμηθευτή  {supplier_name} Ποσό {amount} Ημερομηνία {date}")
        print(f"Ενημέρωση υπολοίπου προμηθευτή  {supplier_name} ολοκληρώθηκε")
        # Ενημέρωση πίνακα πληρωμών
        payment = Payments(supplier_id=supplier_id, amount=amount, date=date)
        Session.add(payment)
        Session.commit()
        print(40 * "#", "Ολοκλήρωση πληρωμής", 40 * "#")
        msgBox = QMessageBox.information(None, "Πληροφορία", f"Η πληρωμή του προμηθευτή {supplier.name} ολοκληρώθηκε.")

    # Επεξεργασία προμηθευτή
    def edit_supplier(self, tableWidget):

        self.edit_window = QMainWindow(parent=None)
        edit_supplier = Edit_supplier_window()
        edit_supplier.setupUi(self.edit_window)

        row = tableWidget.currentIndex().row()
        id_ = tableWidget.item(row, 0)  # Περνουμε το id απο την 0 στήλη της επιλεγμένης γραμμής

        columns = tableWidget.columnCount()
        headers = [str(tableWidget.horizontalHeaderItem(i).text()) for i in range(columns)]

        instance = Session.query(Suppliers).get(id_.text())  # Πέρνουμε τον supplier για να το στείλουμε το edit_supplier
        edit_supplier.supplier_id = instance.id

        edit_supplier.supplier_name_edit.setText(instance.name)
        edit_supplier.vat_nr_edit.setText(str(instance.vat_nr))
        edit_supplier.supplier_phone_edit.setText(str(instance.phone))
        edit_supplier.supplier_address_edit.setText(instance.address)
        edit_supplier.supplier_balance_QSpinBox.setValue(int(instance.balance))
        self.edit_window.show()

    # Επεξεργασία παραλήπτη
    def edit_recipient(self, tableWidget):
        self.edit_window = QMainWindow(parent=None)
        edit_recipient = Edit_recipient_window()
        edit_recipient.setupUi(self.edit_window)

        row = tableWidget.currentIndex().row()
        id_ = tableWidget.item(row, 0)  # Περνουμε το id απο την 0 στήλη της επιλεγμένης γραμμής

        columns = tableWidget.columnCount()
        headers = [str(tableWidget.horizontalHeaderItem(i).text()) for i in range(columns)]

        # Πέρνουμε τον recipient για να το στείλουμε στο edit_recipient
        instance = Session.query(Recipients).get(id_.text())
        edit_recipient.recipient_id = instance.id
        edit_recipient.recipient_name_edit.setText(instance.name)
        edit_recipient.recipient_phone_edit.setText(str(instance.phone))
        edit_recipient.recipient_address_edit.setText(instance.address)
        self.edit_window.show()

    # Εξαγωγή αγορών
    def extract(self, tableWidget):
        """
        :param tableWidget:  απο που να εξάγουμε δεδομένα
        :return:  Αποθήκευση σε excel των στοιχειων που εμφανίζονται στον πίνακα αγορες
        """

        rows = tableWidget.rowCount()
        columns = tableWidget.columnCount()

        headers = [str(tableWidget.horizontalHeaderItem(i).text()) for i in range(columns)]
        # Pandas Dataframe
        # df indexing is slow, so use lists
        df_list = []
        for row in range(rows):
            df_list2 = []
            for col in range(columns):
                table_item = tableWidget.item(row, col)

                df_list2.append('' if table_item is None else table_item.text())
            df_list.append(df_list2)

        df = pd.DataFrame(df_list, columns=headers)
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        filename = QFileDialog.getSaveFileName(None, 'Εξαγωγή', desktop, "Excel (*.xlsx)")

        if filename[0] == '':  # filename == ('C:/Users/Dannys/Desktop/fa.xlsx', 'Excel (*.xlsx)')
            return 0

        writer = pd.ExcelWriter(filename[0], engine="xlsxwriter")
        df.to_excel(writer, sheet_name=f"{datetime.datetime.today().date()}", index=False)
        writer.save()
        msgBox = QMessageBox.information(None, "Πληροφορία", "Η εξαγωγή ολοκληρώθηκε.")

    # Εισαγωγή προμηθευτή
    def add_supplier(self):
        supplier_name = self.supplier_name_edit.text()
        # Ελεγχος αν το όνομα υπάρχει στους προμηθευτές
        try:
            existing_supplier = Session.query(Suppliers).filter_by(name=supplier_name).one_or_none()
            if existing_supplier:
                msgBox = QMessageBox.critical(None, "Σφάλμα", f"Ο {supplier_name} υπάρχει με ΑΦΜ {existing_supplier.vat_nr}")
                return
        except MultipleResultsFound:
            msgBox = QMessageBox.critical(None, "Σφάλμα", f"Ο {supplier_name} υπάρχει πολλές φορές")
            return

        if supplier_name == "":
            msgBox = QMessageBox.warning(None, "Σφάλμα", f"Το Ονοματεπώνυμο δεν μπορεί να είναι κενό!")
            return

        supplier_vat = self.supplier_vat_nr_edit.text().replace(" ", "")

        if not supplier_vat.isdigit():
            msgBox = QMessageBox.critical(None, "Σφάλμα", f"Το Α.Φ.Μ. πρέπει να είναι αριθμός")
            return
        elif len(supplier_vat) != 9:
            msgBox = QMessageBox.critical(None, "Σφάλμα", f"Το Α.Φ.Μ. πρέπει να είναι αριθμός με 9 ψηφία!")
            return

        # Ελεγχος αν υπάρχει το ΑΦΜ
        try:
            existing_supplier = Session.query(Suppliers).filter_by(vat_nr=supplier_vat).one_or_none()
            if existing_supplier:
                msgBox = QMessageBox.critical(None, "Σφάλμα", f"Το Α.Φ.Μ. {supplier_vat} υπάρχει στον προμηθευτή {existing_supplier.name}!")
                return
        except MultipleResultsFound:
            msgBox = QMessageBox.critical(None, "Σφάλμα", f"Το Α.Φ.Μ. υπάρχει πολλές φορές!")
            return

        supplier_phone = self.supplier_phone_edit.text()
        supplier_address = self.supplier_address_edit.text()
        supplier_balance = self.supplier_balance_edit.text()
        new_supplier = Suppliers(name=supplier_name, vat_nr=supplier_vat, phone=supplier_phone, address=supplier_address,
                                 balance=supplier_balance)

        Session.add(new_supplier)
        Session.commit()
        print("*" * 40, "Εισαγωγή προμηθευτή", "*" * 40)
        print(f"Ονοματεπώνυμο {supplier_name} ΑΦΜ {supplier_vat}, Υπόλοιπο {supplier_balance} Τηλέφωνο {supplier_phone}")
        print("*" * 40, "Εισαγωγή προμηθευτή ολοκληρώθηκε", "*" * 40)
        # Ενημέρωση για το autocomplete
        self.list_to_search_supplier = autocomplete(Suppliers)
        self.supplier_qcompobox.clear()  # Πρώτα άδειασμα
        self.supplier_qcompobox.addItems(sorted([f"{supplier}" for supplier in get_data(Suppliers)], key=str.lower))

        self.supplier_qcompobox_at_pay_page.clear()  # Πρώτα άδειασμα
        self.supplier_qcompobox_at_pay_page.addItems(sorted([f"{supplier}" for supplier in get_data(Suppliers)], key=str.lower))

        self.list_to_search_purchases = autocomplete_purchases()
        self.purchases_completer = QCompleter(self.list_to_search_purchases)
        self.search_purchases_edit.setCompleter(self.purchases_completer)

        self.suppliers_completer = QCompleter(self.list_to_search_supplier)
        self.search_supplier_edit.setCompleter(self.suppliers_completer)

        self.payments_completer = QCompleter(self.list_to_search_supplier)
        self.search_payments_edit.setCompleter(self.payments_completer)

        msgBox = QMessageBox.information(None, "Πληροφορία", f"Ο {supplier_name} αποθηκεύτηκε.")

    # Εισαγωγή παραλήπτη
    def add_recipient(self):

        recipient_name = self.recipient_name_edit.text()
        # Αν είναι κενό
        if recipient_name == "":
            msgBox = QMessageBox.warning(None, "Σφάλμα", f"Το Ονοματεπώνυμο δεν μπορεί να είναι κενό!")
            return
        # Αν υπάρχει
        try:
            existing_recipient = Session.query(Recipients).filter_by(name=recipient_name).one_or_none()
            if existing_recipient:
                msgBox = QMessageBox.warning(None, "Σφάλμα", f"Το Ονοματεπώνυμο υπάρχει!")
                return
        except MultipleResultsFound:
            msgBox = QMessageBox.warning(None, "Σφάλμα", f"Το Ονοματεπώνυμο υπάρχει πολλές φορές!")
            return

        recipient_phone = self.recipient_phone_edit.text()
        recipient_address = self.recipient_address_edit.text()
        new_recipient = Recipients(name=recipient_name, phone=recipient_phone, address=recipient_address)

        Session.add(new_recipient)
        Session.commit()
        print("*" * 40, "Εισαγωγή παραλήπτη", "*" * 40)
        print(f"Ονοματεπώνυμο {recipient_name} , Διεύθυνση {recipient_address} Τηλέφωνο {recipient_phone}")
        print("*" * 40, "Εισαγωγή παραλήπτη ολοκληρώθηκε", "*" * 40)
        # Ενημέρωση για το autocomplete
        self.list_to_search_recipient = autocomplete(Recipients)

        self.recipient_completer = QCompleter(self.list_to_search_recipient)
        self.search_recipient_edit.setCompleter(self.recipient_completer)

        self.list_to_search_purchases = autocomplete_purchases()

        self.purchases_completer = QCompleter(self.list_to_search_purchases)
        self.search_purchases_edit.setCompleter(self.purchases_completer)

        self.recipient_comboBox.clear()  # Πρώτα άδειασμα
        self.recipient_comboBox.addItems(sorted([f"{recipient}" for recipient in get_data(Recipients)], key=str.lower))

        msgBox = QMessageBox.information(None, "Πληροφορία", f"Ο {recipient_name} αποθηκεύτηκε.")

    # Επεξεργασία Αγοράς
    def edit_purchase(self, tableWidget):
        self.edit_window = QMainWindow(parent=None)
        edit_purchase = Edit_Purchase_Window()
        edit_purchase.setupUi(self.edit_window)

        row = tableWidget.currentIndex().row()
        id_ = tableWidget.item(row, 0)  # Περνουμε το id απο την 0 στήλη της επιλεγμένης γραμμής

        # Πέρνουμε το id του πινακα purchases για να το στείλουμε στο edit_purchase
        instance = Session.query(Purchases).get(id_.text())
        edit_purchase.purchase_id = instance.id

        # Ελεγχος αν υπάρχει αρχείο
        file = instance.file

        try:
            if os.path.isfile(file):
                edit_purchase.add_file_btn.hide()  # Αποκρυψη προσθήκης αρχείου αφου υπάρχει
                edit_purchase.view_file_btn.show()  # εμφάνιση προβολής αρχείου
                edit_purchase.delete_file_btn.show()  # εμφάνιση διαγραφής αρχείου
                edit_purchase.file = instance.file
        except TypeError:  # stat: path should be string, bytes, os.PathLike or integer, not NoneType
            pass  # Δεν υπάρχει το αρχείο

        edit_purchase.supplier_qcompobox.addItem(instance.supplier.name)
        edit_purchase.supplier_qcompobox.setEditable(False)

        edit_purchase.invoice_edit.setText(str(instance.invoice))
        edit_purchase.price_QSpinBox.setValue(instance.price)
        edit_purchase.recipient_comboBox.addItem(instance.recipient.name)
        edit_purchase.recipient_comboBox.setEditable(False)

        QDate_obj = QDate.fromString(instance.date, "d/M/yyyy")
        edit_purchase.date_edit.setDate(QDate_obj)

        edit_purchase.product_description_plainTextEdit.setPlainText(instance.product)
        self.edit_window.show()

    # Επεξεργασία Πληρωμής
    def edit_payment(self, tableWidget):
        self.edit_window = QMainWindow(parent=None)
        edit_payment = Edit_Payment_Window()
        edit_payment.setupUi(self.edit_window)

        row = tableWidget.currentIndex().row()
        id_ = tableWidget.item(row, 0)  # Περνουμε το id απο την 0 στήλη της επιλεγμένης γραμμής

        # Πέρνουμε το id του πινακα purchases για να το στείλουμε στο edit_purchase
        instance = Session.query(Payments).get(id_.text())
        edit_payment.payment_id = instance.id

        edit_payment.supplier_qcompobox.addItem(instance.supplier.name)
        edit_payment.supplier_qcompobox.setEditable(False)

        edit_payment.amount_QSpinBox.setValue(instance.amount)

        QDate_obj = QDate.fromString(instance.date, "d/M/yyyy")
        edit_payment.date_edit.setDate(QDate_obj)

        self.edit_window.show()

    # Εισαγωγή αρχείου
    def add_file(self):
        self.filename, filters = QFileDialog.getOpenFileName(None, caption='Προσθήκη αρχείου', dir='.',
                                                                 filter='*.pdf')

        self.add_file_btn.setStyleSheet(u"background-color: rgb(92, 184, 78); color: rgb(255, 255, 255);")
        self.add_file_btn.setText(QCoreApplication.translate("MainWindow", u"Αρχείο για προσθήκη", None))


    def show_info(self,):
        QMessageBox.information(None, "Πληροφορίες", f""" 
            Αuthor     : "Jordanis Ntini"
            Copyright  : "Copyright © {datetime.datetime.today().year}"
            Credits    : 'Athanasia Tzampazi'
            Version    : '{version}'
            Maintainer : "Jordanis Ntini"
            Email      : "ntinisiordanis@gmail.com"
            Status     : 'Development' 
            For        : Νάτσης Αντώνης
    
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Ορισμός εμφάνισης
    app.setStyle(QStyleFactory.create("Fusion"))
    MainWindow = QMainWindow(parent=None)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
