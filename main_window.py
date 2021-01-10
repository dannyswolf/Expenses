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
# V 0.1 Alfa
# todo ενα function για ενημερωση πινακων με το πατημα των αριστερών κουμπιών
# -------------------------------------------------------------------------------

from PySide2.QtCore import QCoreApplication, QLocale, QSize, Qt, QDateTime, QRect, QMetaObject, QDate
from PySide2.QtGui import QPalette, QFont, QBrush, QCursor, QColor, QValidator
from PySide2.QtWidgets import QAbstractScrollArea, QTableWidgetItem, QTableWidget, QLineEdit, QLabel, QFrame, \
    QMainWindow, QComboBox, QStackedWidget, QPushButton, QSizePolicy, QWidget, QGridLayout, QApplication, \
    QStyleFactory, QAbstractItemView, QDateEdit, QAbstractSpinBox, QDateTimeEdit, QSpinBox, QPlainTextEdit, \
    QMenu, QMenuBar

import datetime
import sys
from settings import root_logger, version
from sql import Suppliers, Recipients, Payments, Purchases, Session, get_data, MultipleResultsFound, NoResultFound

sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(843, 671)
        MainWindow.setMinimumSize(QSize(400, 400))
        MainWindow.setSizeIncrement(QSize(20, 20))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(55, 88, 120);")
        MainWindow.setLocale(QLocale(QLocale.Greek, QLocale.Greece))
        MainWindow.setWindowFilePath(u"")

        self.suppliers = get_data(Suppliers)
        self.recipients = get_data(Recipients)
        self.purchases  = get_data(Purchases)
        self.payments = get_data(Payments)


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
        self.gridLayout_3.addWidget(self.import_btn, 1, 0, 3, 1)
        self.import_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.import_page))

        # Pay Btn
        self.pay_btn = QPushButton(self.centralwidget)
        self.pay_btn.setObjectName(u"pay_btn")
        sizePolicy.setHeightForWidth(self.pay_btn.sizePolicy().hasHeightForWidth())
        self.pay_btn.setSizePolicy(sizePolicy)
        self.pay_btn.setFont(self.font)
        self.pay_btn.setStyleSheet(u"background-color: rgb(0, 85, 0); color: rgb(255, 255, 255);")
        self.gridLayout_3.addWidget(self.pay_btn, 4, 0, 1, 1)
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
        self.gridLayout_3.addWidget(self.purchases_btn, 0, 0, 1, 1)
        self.purchases_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.purchases_page))
        self.purchases_btn.clicked.connect(lambda: self.update_purchases(Purchases))
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
        self.gridLayout_3.addWidget(self.suppliers_btn, 5, 0, 1, 1)
        self.suppliers_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.suppliers_page))

        # Recipients Btn
        self.recipients_btn = QPushButton(self.centralwidget)
        self.recipients_btn.setObjectName(u"recipients_btn")
        sizePolicy.setHeightForWidth(self.recipients_btn.sizePolicy().hasHeightForWidth())
        self.recipients_btn.setSizePolicy(sizePolicy)
        self.recipients_btn.setFont(self.font)
        self.recipients_btn.setStyleSheet(u"background-color: rgb(0, 85, 0); color: rgb(255, 255, 255);")
        self.gridLayout_3.addWidget(self.recipients_btn, 6, 0, 1, 1)
        self.recipients_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.recipients_page))

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
        self.gridLayout_7.addWidget(self.export_purchases_btn, 3, 0, 1, 2)
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
        self.gridLayout_7.addWidget(self.search_purchases_btn, 1, 1, 1, 1)
        self.search_purchases_edit = QLineEdit(self.purchases_page)
        self.search_purchases_edit.setObjectName(u"search_purchases_edit")
        self.search_purchases_edit.setMinimumSize(QSize(0, 31))
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setPointSize(12)
        self.search_purchases_edit.setFont(font4)
        self.gridLayout_7.addWidget(self.search_purchases_edit, 1, 0, 1, 1)
        self.purchases_tableWidget = QTableWidget(self.purchases_page)
        if (self.purchases_tableWidget.columnCount() < 6):
            self.purchases_tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        self.purchases_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font3);
        self.purchases_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font3);
        self.purchases_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font3);
        self.purchases_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font3);
        self.purchases_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font3);
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
        self.purchases_tableWidget.horizontalHeader().setDefaultSectionSize(106)
        self.purchases_tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.purchases_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.purchases_tableWidget.verticalHeader().setVisible(False)
        self.purchases_tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.purchases_tableWidget.verticalHeader().setHighlightSections(True)



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
        self.insert_invoice_label.setMinimumSize(QSize(0, 0))
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
        self.invoice_edit = QLineEdit(self.import_page)
        self.invoice_edit.setObjectName(u"invoice_edit")
        self.invoice_edit.setMinimumSize(QSize(0, 31))
        self.invoice_edit.setMaximumSize(QSize(16777215, 16777215))
        self.invoice_edit.setFont(font3)
        self.invoice_edit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayout.addWidget(self.invoice_edit, 3, 1, 1, 1)
        self.date_edit = QDateEdit(self.import_page)
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
        self.date_edit.setStyleSheet(u"color: rgb(145, 145, 0);")
        self.date_edit.setInputMethodHints(Qt.ImhDate)
        self.date_edit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.date_edit.setSpecialValueText(u"")
        self.date_edit.setDateTime(QDateTime.currentDateTime())
        self.date_edit.setCurrentSection(QDateTimeEdit.DaySection)
        self.date_edit.setDisplayFormat(u"d/M/yy")
        self.date_edit.setCalendarPopup(True)
        self.gridLayout.addWidget(self.date_edit, 4, 1, 1, 1)
        self.recipient_comboBox = QComboBox(self.import_page)
        self.recipient_comboBox.setObjectName(u"recipient_comboBox")
        self.recipient_comboBox.setMinimumSize(QSize(0, 31))
        self.recipient_comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.recipient_comboBox.setFont(font3)
        self.recipient_comboBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.recipient_comboBox.addItems(sorted([f"{recipient}" for recipient in self.recipients]))
        self.recipient_comboBox.setEditable(True)
        self.recipient_comboBox.lineEdit().setFont(font3)
        self.gridLayout.addWidget(self.recipient_comboBox, 6, 1, 1, 1)
        self.supplier_qcompobox = QComboBox(self.import_page)
        self.supplier_qcompobox.setObjectName(u"supplier_qcompobox")
        self.supplier_qcompobox.setEnabled(True)
        self.supplier_qcompobox.setMinimumSize(QSize(0, 31))
        self.supplier_qcompobox.setFont(font3)
        self.supplier_qcompobox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.supplier_qcompobox.addItems(sorted([f"{supplier}" for supplier in self.suppliers]))
        self.supplier_qcompobox.setEditable(True)
        self.supplier_qcompobox.lineEdit().setFont(font3)

        self.supplier_qcompobox.validator()

        self.gridLayout.addWidget(self.supplier_qcompobox, 1, 1, 1, 1)
        self.add_file_btn = QPushButton(self.import_page)
        self.add_file_btn.setObjectName(u"add_file_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add_file_btn.sizePolicy().hasHeightForWidth())
        self.add_file_btn.setSizePolicy(sizePolicy1)
        self.add_file_btn.setMinimumSize(QSize(0, 0))
        self.add_file_btn.setFont(font3)
        self.add_file_btn.setStyleSheet(u"background-color: rgb(170, 85, 0);\n"
                                        "color: rgb(255, 255, 255);")

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
        self.gridLayout.addWidget(self.insert_recipier_btn, 6, 2, 1, 1)

        self.amount_doubleSpinBox_at_import_page = QSpinBox(self.import_page)
        self.amount_doubleSpinBox_at_import_page.setObjectName(u"amount_doubleSpinBox_at_import_page")
        self.amount_doubleSpinBox_at_import_page.setMinimumSize(QSize(0, 31))
        self.amount_doubleSpinBox_at_import_page.setFont(font3)
        self.amount_doubleSpinBox_at_import_page.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.amount_doubleSpinBox_at_import_page.setMaximum(9999999)
        self.gridLayout.addWidget(self.amount_doubleSpinBox_at_import_page, 8, 1, 1, 1)
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
        self.save_btn = QPushButton(self.import_page)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy5)
        self.save_btn.setMinimumSize(QSize(0, 0))
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
        self.save_btn.clicked.connect(self.save_import)
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
        self.supplier_qcompobox_at_pay_page.setFont(font3)
        self.supplier_qcompobox_at_pay_page.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.supplier_qcompobox_at_pay_page.setPlaceholderText(u"")
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
        self.date_QDateEdit_at_pay_page.setStyleSheet(u"color: rgb(145, 145, 0);")
        self.date_QDateEdit_at_pay_page.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.date_QDateEdit_at_pay_page.setSpecialValueText(u"")
        self.date_QDateEdit_at_pay_page.setDateTime(QDateTime.currentDateTime())
        self.date_QDateEdit_at_pay_page.setCurrentSection(QDateTimeEdit.DaySection)
        self.date_QDateEdit_at_pay_page.setDisplayFormat(u"d/M/yy")
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
        self.gridLayout_2.addWidget(self.insert_supplier_btn_at_suppliers_page, 5, 1, 1, 1)
        self.export_suppliers_btn_at_suppliers_page = QPushButton(self.suppliers_page)
        self.export_suppliers_btn_at_suppliers_page.setObjectName(u"export_suppliers_btn_at_suppliers_page")
        self.export_suppliers_btn_at_suppliers_page.setMinimumSize(QSize(200, 60))
        self.export_suppliers_btn_at_suppliers_page.setFont(font2)
        self.export_suppliers_btn_at_suppliers_page.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                                  "background-color: rgb(170, 85, 0);")
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
        self.gridLayout_2.addWidget(self.search_supplier_edit, 2, 0, 1, 1)
        self.search_supplier_btn = QPushButton(self.suppliers_page)
        self.search_supplier_btn.setObjectName(u"search_supplier_btn")
        self.search_supplier_btn.setMinimumSize(QSize(0, 31))
        self.search_supplier_btn.setFont(font3)
        self.search_supplier_btn.setStyleSheet(u"color: rgb(255, 255, 255);")
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
        self.recipient_tableWidget = QTableWidget(self.recipients_page)

        if (self.recipient_tableWidget.columnCount() < 4):
            self.recipient_tableWidget.setColumnCount(4)
        font8 = QFont()
        font8.setBold(False)
        font8.setWeight(50)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignLeading | Qt.AlignVCenter)
        __qtablewidgetitem44.setFont(font8)
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
        # Προβολή προμηθευτών
        for row, data in enumerate(self.recipients):
            _id = QTableWidgetItem(str(data.id))
            _id.setData(Qt.DisplayRole, int(data.id))
            self.recipient_tableWidget.setItem(row, 0, _id)
            name = QTableWidgetItem(str(data.name))
            self.recipient_tableWidget.setItem(row, 1, name)
            # Phone
            phone = QTableWidgetItem(str(data.phone))
            phone.setData(Qt.DisplayRole, data.phone)
            self.recipient_tableWidget.setItem(row, 2, phone)

            address = QTableWidgetItem(str(data.address))
            self.recipient_tableWidget.setItem(row, 3, address)

        __qtablewidgetitem48 = QTableWidgetItem()
        self.recipient_tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.recipient_tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem49)
        self.recipient_tableWidget.setObjectName(u"recipient_tableWidget")
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
        self.gridLayout_4.addWidget(self.recipient_tableWidget, 3, 0, 1, 2)
        self.insert_recipient_btn_at_recipient_page = QPushButton(self.recipients_page)
        self.insert_recipient_btn_at_recipient_page.setObjectName(u"insert_recipient_btn_at_recipient_page")
        self.insert_recipient_btn_at_recipient_page.setMinimumSize(QSize(200, 60))
        self.insert_recipient_btn_at_recipient_page.setFont(font2)
        self.insert_recipient_btn_at_recipient_page.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                                  "background-color: rgb(7, 114, 255);")
        self.insert_recipient_btn_at_recipient_page.setText(
            u"\u0395\u03b9\u03c3\u03b1\u03b3\u03c9\u03b3\u03ae \u03c0\u03b1\u03c1\u03b1\u03bb\u03ae\u03c0\u03c4\u03b7")
        self.gridLayout_4.addWidget(self.insert_recipient_btn_at_recipient_page, 4, 0, 1, 2)
        self.search_recipient_btn = QPushButton(self.recipients_page)
        self.search_recipient_btn.setObjectName(u"search_recipient_btn")
        self.search_recipient_btn.setMinimumSize(QSize(200, 0))
        self.search_recipient_btn.setFont(font3)
        self.search_recipient_btn.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.search_recipient_btn.setText(u"\u0391\u03bd\u03b1\u03b6\u03ae\u03c4\u03b7\u03c3\u03b7")
        self.gridLayout_4.addWidget(self.search_recipient_btn, 2, 1, 1, 1)
        self.search_recipient_edit = QLineEdit(self.recipients_page)
        self.search_recipient_edit.setObjectName(u"search_recipient_edit")
        self.search_recipient_edit.setMinimumSize(QSize(0, 31))
        self.search_recipient_edit.setStyleSheet(u"color: rgb(255, 255, 255);")
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
        self.gridLayout_6.addWidget(self.search_payments_edit, 1, 0, 1, 1)
        self.export_payments_btn = QPushButton(self.payments_page)
        self.export_payments_btn.setObjectName(u"export_payments_btn")
        self.export_payments_btn.setMinimumSize(QSize(0, 60))
        self.export_payments_btn.setFont(font2)
        self.export_payments_btn.setStyleSheet(u"background-color: rgb(170, 85, 0);")
        self.gridLayout_6.addWidget(self.export_payments_btn, 3, 0, 1, 3)
        self.payments_tableWidget = QTableWidget(self.payments_page)
        if (self.payments_tableWidget.columnCount() < 4):
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
        self.payments_tableWidget.setRowCount(len(self.payments))
        for row, data in enumerate(self.payments):
            _id = QTableWidgetItem(str(data.id))
            _id.setData(Qt.DisplayRole, float(data.id))
            self.payments_tableWidget.setItem(row, 0, _id)
            supplier = QTableWidgetItem(str(data.supplier))
            self.payments_tableWidget.setItem(row, 1, supplier)

            # Amount
            amount = QTableWidgetItem(str(data.amount))
            amount.setData(Qt.DisplayRole, int(data.amount))
            self.payments_tableWidget.setItem(row, 2, amount)

            # Date
            date = QTableWidgetItem(str(data.date.strftime("%d/%m/%Y")))
            date.setData(Qt.DisplayRole, QDate(data.date))
            self.payments_tableWidget.setItem(row, 3, date)

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
        self.payments_tableWidget.verticalHeader().setVisible(False)
        self.payments_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.payments_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.payments_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_6.addWidget(self.payments_tableWidget, 2, 0, 1, 3)
        self.search_payments_btn = QPushButton(self.payments_page)
        self.search_payments_btn.setObjectName(u"search_payments_btn")
        self.search_payments_btn.setMinimumSize(QSize(200, 31))
        self.search_payments_btn.setFont(font3)
        self.gridLayout_6.addWidget(self.search_payments_btn, 1, 1, 1, 2)
        self.stackedWidget.addWidget(self.payments_page)

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

    # setupUi

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
                                       None));
        ___qtablewidgetitem6 = self.purchases_tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.purchases_tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.purchases_tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.product_description_label.setText(QCoreApplication.translate("MainWindow",
                                                                          u"\u03a0\u03b5\u03c1\u03b9\u03b3\u03c1\u03b1\u03c6\u03ae \u03c0\u03c1\u03bf\u03b9\u03cc\u03bd\u03c4\u03bf\u03c2",
                                                                          None))
        self.add_file_btn.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u03a0\u03c1\u03bf\u03c3\u03b8\u03ae\u03ba\u03b7 \u03b1\u03c1\u03c7\u03b5\u03af\u03bf\u03c5",
                                                             None))
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

        # Προβολή προμηθευτών
        for row, data in enumerate(self.suppliers):
            _id = QTableWidgetItem(str(data.id))
            _id.setData(Qt.DisplayRole, int(data.id))
            self.suppliers_tableWidget.setItem(row, 0, _id)

            name = QTableWidgetItem(str(data.name))
            self.suppliers_tableWidget.setItem(row, 1, name)

            vat_nr = QTableWidgetItem(str(data.vat_nr))
            vat_nr.setData(Qt.DisplayRole, int(data.vat_nr))
            self.suppliers_tableWidget.setItem(row, 2, vat_nr)

            phone = QTableWidgetItem(str(data.phone))
            phone.setData(Qt.DisplayRole, int(data.phone))
            self.suppliers_tableWidget.setItem(row, 3, phone)

            balance = QTableWidgetItem(str(data.balance))
            balance.setData(Qt.DisplayRole, int(data.balance))
            self.suppliers_tableWidget.setItem(row, 4, balance)

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
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0391\u03c1\u03c7\u03b5\u03af\u03bf", None))

    # retranslateUi

    # Update Purchases
    def update_purchases(self, table):
        self.purchases = get_data(Purchases)
        for row, data in enumerate(self.purchases):
            _id = QTableWidgetItem(str(data.id))
            _id.setData(Qt.DisplayRole, int(data.id))
            self.purchases_tableWidget.setItem(row, 0, _id)

            supplier = QTableWidgetItem(str(data.supplier))
            self.purchases_tableWidget.setItem(row, 1, supplier)
            # Phone
            product = QTableWidgetItem(str(data.product))

            self.purchases_tableWidget.setItem(row, 2, product)

            price = QTableWidgetItem(str(data.price))
            price.setData(Qt.DisplayRole, data.price)
            self.purchases_tableWidget.setItem(row, 3, price)

            recipient = QTableWidgetItem(str(data.recipient))
            self.purchases_tableWidget.setItem(row, 4, recipient)

            date = QTableWidgetItem(str(data.date))
            date.setData(Qt.DisplayRole, data.date)
            self.purchases_tableWidget.setItem(row, 5, date)

    # Αποθήκευση τιμπολογίου - αγοράς
    def save_import(self):
        supplier = self.supplier_qcompobox.currentData(Qt.DisplayRole)
        invoice_nr = self.invoice_edit.text()
        date = self.date_edit.date().toPython()
        recipient = self.recipient_comboBox.currentData(Qt.DisplayRole)
        amount = self.amount_doubleSpinBox_at_import_page.text()[:-1]
        product = self.product_description_plainTextEdit.toPlainText()

        try:
            supplier_id = Session.query(Suppliers).filter_by(name=supplier).one_or_none()
            supplier_id = supplier_id.id
        except (NoResultFound, MultipleResultsFound):
            return

        try:
            recipient_id = Session.query(Recipients).filter_by(name=recipient).one_or_none()
            recipient_id = recipient_id.id
        except (NoResultFound, MultipleResultsFound):
            return

        item = Purchases(supplier_id=supplier_id, recipient_id=recipient_id, price=amount, product=product, file="C:\\", date=date )
        Session.add(item)
        Session.commit()
        self.purchases = get_data(Purchases)
        self.update_purchases(Purchases)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    MainWindow = QMainWindow(parent=None)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
