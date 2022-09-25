from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setMinimumSize(QSize(300, 400))
        icon = QIcon()
        icon.addFile(u":/icons/icons/calculate_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"    font-family: 'Segoe UI';\n"
"    color: white;\n"
"    background-color: black;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"@font-face {\n"
"    font-family: \"Segoe UI\"; \n"
"    src: url('/font/Segoe\\ UI\\ Bold.ttf') format(\"truetype\"); \n"
"    font-style: normal; \n"
"    font-weight: normal; \n"
"    } \n"
"QPushButton{\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #666;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #888;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_temp = QLabel(self.centralwidget)
        self.lbl_temp.setObjectName(u"lbl_temp")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy)
        self.lbl_temp.setStyleSheet(u"color: #888;")
        self.lbl_temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lbl_temp)

        self.le_entry = QLineEdit(self.centralwidget)
        self.le_entry.setObjectName(u"le_entry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_entry.sizePolicy().hasHeightForWidth())
        self.le_entry.setSizePolicy(sizePolicy1)
        self.le_entry.setStyleSheet(u"font-size: 40pt;\n"
"border: none;")
        self.le_entry.setMaxLength(12)
        self.le_entry.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.le_entry.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_entry)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_sin = QPushButton(self.centralwidget)
        self.btn_sin.setObjectName(u"btn_sin")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_sin.sizePolicy().hasHeightForWidth())
        self.btn_sin.setSizePolicy(sizePolicy2)
        self.btn_sin.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_sin, 4, 4, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy2.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy2)
        self.btn_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy2.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy2)
        self.btn_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_remove = QPushButton(self.centralwidget)
        self.btn_remove.setObjectName(u"btn_remove")
        sizePolicy2.setHeightForWidth(self.btn_remove.sizePolicy().hasHeightForWidth())
        self.btn_remove.setSizePolicy(sizePolicy2)
        self.btn_remove.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/backspace_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remove.setIcon(icon1)
        self.btn_remove.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.btn_remove, 0, 2, 1, 1)

        self.btn_sub = QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy2.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy2)
        self.btn_sub.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sub.setStyleSheet(u"font-size:36px")

        self.gridLayout.addWidget(self.btn_sub, 2, 3, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy2.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy2)
        self.btn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy2.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy2)
        self.btn_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_div = QPushButton(self.centralwidget)
        self.btn_div.setObjectName(u"btn_div")
        sizePolicy2.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy2)
        self.btn_div.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_div, 0, 3, 1, 1)

        self.btn_calc = QPushButton(self.centralwidget)
        self.btn_calc.setObjectName(u"btn_calc")
        sizePolicy2.setHeightForWidth(self.btn_calc.sizePolicy().hasHeightForWidth())
        self.btn_calc.setSizePolicy(sizePolicy2)
        self.btn_calc.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_calc, 4, 3, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy2.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy2)
        self.btn_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_cos = QPushButton(self.centralwidget)
        self.btn_cos.setObjectName(u"btn_cos")
        sizePolicy2.setHeightForWidth(self.btn_cos.sizePolicy().hasHeightForWidth())
        self.btn_cos.setSizePolicy(sizePolicy2)
        self.btn_cos.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_cos, 3, 4, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy2.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy2)
        self.btn_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_C = QPushButton(self.centralwidget)
        self.btn_C.setObjectName(u"btn_C")
        sizePolicy2.setHeightForWidth(self.btn_C.sizePolicy().hasHeightForWidth())
        self.btn_C.setSizePolicy(sizePolicy2)
        self.btn_C.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_C, 0, 0, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy2.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy2)
        self.btn_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_change_sign = QPushButton(self.centralwidget)
        self.btn_change_sign.setObjectName(u"btn_change_sign")
        sizePolicy2.setHeightForWidth(self.btn_change_sign.sizePolicy().hasHeightForWidth())
        self.btn_change_sign.setSizePolicy(sizePolicy2)
        self.btn_change_sign.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_change_sign, 4, 0, 1, 1)

        self.btn_CE = QPushButton(self.centralwidget)
        self.btn_CE.setObjectName(u"btn_CE")
        sizePolicy2.setHeightForWidth(self.btn_CE.sizePolicy().hasHeightForWidth())
        self.btn_CE.setSizePolicy(sizePolicy2)
        self.btn_CE.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_CE, 0, 1, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy2.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy2)
        self.btn_0.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_0, 4, 1, 1, 1)

        self.btn_mul = QPushButton(self.centralwidget)
        self.btn_mul.setObjectName(u"btn_mul")
        sizePolicy2.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy2)
        self.btn_mul.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_mul, 1, 3, 1, 1)

        self.btn_dot = QPushButton(self.centralwidget)
        self.btn_dot.setObjectName(u"btn_dot")
        sizePolicy2.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy2)
        self.btn_dot.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_dot, 4, 2, 1, 1)

        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy2.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy2)
        self.btn_add.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_add, 3, 3, 1, 1)

        self.btn_sqrt = QPushButton(self.centralwidget)
        self.btn_sqrt.setObjectName(u"btn_sqrt")
        sizePolicy2.setHeightForWidth(self.btn_sqrt.sizePolicy().hasHeightForWidth())
        self.btn_sqrt.setSizePolicy(sizePolicy2)
        self.btn_sqrt.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_sqrt, 1, 4, 1, 1)

        self.btn_tan = QPushButton(self.centralwidget)
        self.btn_tan.setObjectName(u"btn_tan")
        sizePolicy2.setHeightForWidth(self.btn_tan.sizePolicy().hasHeightForWidth())
        self.btn_tan.setSizePolicy(sizePolicy2)
        self.btn_tan.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_tan, 2, 4, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy2.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy2)
        self.btn_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy2.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy2)
        self.btn_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_ln = QPushButton(self.centralwidget)
        self.btn_ln.setObjectName(u"btn_ln")
        sizePolicy2.setHeightForWidth(self.btn_ln.sizePolicy().hasHeightForWidth())
        self.btn_ln.setSizePolicy(sizePolicy2)
        self.btn_ln.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_ln, 0, 4, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 5, 0, 1, 5)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.lbl_temp.setText("")
        self.le_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_sin.setText(QCoreApplication.translate("MainWindow", u"sin", None))
#if QT_CONFIG(shortcut)
        self.btn_sin.setShortcut(QCoreApplication.translate("MainWindow", u"\\, /", None))
#endif // QT_CONFIG(shortcut)
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_remove.setText("")
#if QT_CONFIG(shortcut)
        self.btn_remove.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.btn_sub.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_div.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
#if QT_CONFIG(shortcut)
        self.btn_div.setShortcut(QCoreApplication.translate("MainWindow", u"\\, /", None))
#endif // QT_CONFIG(shortcut)
        self.btn_calc.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.btn_calc.setShortcut(QCoreApplication.translate("MainWindow", u"=, Return", None))
#endif // QT_CONFIG(shortcut)
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_cos.setText(QCoreApplication.translate("MainWindow", u"cos", None))
#if QT_CONFIG(shortcut)
        self.btn_cos.setShortcut(QCoreApplication.translate("MainWindow", u"\\, /", None))
#endif // QT_CONFIG(shortcut)
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.btn_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
#if QT_CONFIG(shortcut)
        self.btn_C.setShortcut(QCoreApplication.translate("MainWindow", u"C, \u0421", None))
#endif // QT_CONFIG(shortcut)
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_change_sign.setText(QCoreApplication.translate("MainWindow", u"+/\u2013", None))
        self.btn_CE.setText(QCoreApplication.translate("MainWindow", u"CE", None))
#if QT_CONFIG(shortcut)
        self.btn_CE.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btn_mul.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
#if QT_CONFIG(shortcut)
        self.btn_mul.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.btn_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.btn_dot.setShortcut(QCoreApplication.translate("MainWindow", u"., \u042e", None))
#endif // QT_CONFIG(shortcut)
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.btn_add.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btn_sqrt.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
#if QT_CONFIG(shortcut)
        self.btn_sqrt.setShortcut(QCoreApplication.translate("MainWindow", u"\\, /", None))
#endif // QT_CONFIG(shortcut)
        self.btn_tan.setText(QCoreApplication.translate("MainWindow", u"tan", None))
#if QT_CONFIG(shortcut)
        self.btn_tan.setShortcut(QCoreApplication.translate("MainWindow", u"\\, /", None))
#endif // QT_CONFIG(shortcut)
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btn_ln.setText(QCoreApplication.translate("MainWindow", u"ln", None))
#if QT_CONFIG(shortcut)
        self.btn_ln.setShortcut(QCoreApplication.translate("MainWindow", u"\\, /", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0432\u0435\u0440\u0434\u043e\u0445\u043b\u0435\u0431 \u0438 \u042f\u0434\u044b\u043a\u0438\u043d\u0430", None))
    # retranslateUi

