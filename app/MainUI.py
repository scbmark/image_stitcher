# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject,
                            QPoint, QRect, QSize, Qt, QTime, QUrl)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QLayout, QListView, QListWidget, QListWidgetItem,
                               QMainWindow, QMenu, QMenuBar, QPushButton, QRadioButton, QSizePolicy,
                               QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

import resources_rc

from .CustomWidgets import DropListWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 800)
        icon = QIcon()
        icon.addFile(":/statics/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.menu_about_about = QAction(MainWindow)
        self.menu_about_about.setObjectName("menu_about_about")
        self.menu_about_manual = QAction(MainWindow)
        self.menu_about_manual.setObjectName("menu_about_manual")
        self.menu_about_update = QAction(MainWindow)
        self.menu_about_update.setObjectName("menu_about_update")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.v_main_layout = QVBoxLayout()
        self.v_main_layout.setObjectName("v_main_layout")
        self.v_main_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.v_main_layout.setContentsMargins(10, 10, 10, 10)
        self.h_info_layout = QHBoxLayout()
        self.h_info_layout.setObjectName("h_info_layout")
        self.h_info_layout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.image_mode_lb = QLabel(self.centralwidget)
        self.image_mode_lb.setObjectName("image_mode_lb")

        self.horizontalLayout_2.addWidget(self.image_mode_lb)

        self.horizon_rtn = QRadioButton(self.centralwidget)
        self.horizon_rtn.setObjectName("horizon_rtn")
        self.horizon_rtn.setChecked(True)

        self.horizontalLayout_2.addWidget(self.horizon_rtn)

        self.vertical_rtn = QRadioButton(self.centralwidget)
        self.vertical_rtn.setObjectName("vertical_rtn")

        self.horizontalLayout_2.addWidget(self.vertical_rtn)

        self.h_info_layout.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.h_info_layout.addItem(self.horizontalSpacer)

        self.clear_list_btn = QPushButton(self.centralwidget)
        self.clear_list_btn.setObjectName("clear_list_btn")
        icon1 = QIcon()
        icon1.addFile(":/statics/clear_all.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_list_btn.setIcon(icon1)

        self.h_info_layout.addWidget(self.clear_list_btn)

        self.v_main_layout.addLayout(self.h_info_layout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.v_main_layout.addWidget(self.line)

        self.items_list = DropListWidget(self.centralwidget)
        self.items_list.setObjectName("items_list")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.items_list.sizePolicy().hasHeightForWidth())
        self.items_list.setSizePolicy(sizePolicy)
        self.items_list.setDragEnabled(True)
        self.items_list.setDragDropMode(QAbstractItemView.InternalMove)
        self.items_list.setDefaultDropAction(Qt.MoveAction)
        self.items_list.setIconSize(QSize(50, 50))
        self.items_list.setMovement(QListView.Free)
        self.items_list.setProperty("isWrapping", False)
        self.items_list.setWordWrap(True)

        self.v_main_layout.addWidget(self.items_list)

        self.item_list_info_lb = QLabel(self.centralwidget)
        self.item_list_info_lb.setObjectName("item_list_info_lb")
        self.item_list_info_lb.setAlignment(Qt.AlignCenter)

        self.v_main_layout.addWidget(self.item_list_info_lb)

        self.h_button_layout = QHBoxLayout()
        self.h_button_layout.setObjectName("h_button_layout")
        self.h_button_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.h_button_layout.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.h_button_layout.addItem(self.horizontalSpacer_2)

        self.start_btn = QPushButton(self.centralwidget)
        self.start_btn.setObjectName("start_btn")
        icon2 = QIcon()
        icon2.addFile(":/statics/play_arrow.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.start_btn.setIcon(icon2)
        self.start_btn.setIconSize(QSize(30, 30))

        self.h_button_layout.addWidget(self.start_btn)

        self.exit_btn = QPushButton(self.centralwidget)
        self.exit_btn.setObjectName("exit_btn")
        icon3 = QIcon()
        icon3.addFile(":/statics/logout.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn.setIcon(icon3)
        self.exit_btn.setIconSize(QSize(28, 28))
        self.exit_btn.setFlat(False)

        self.h_button_layout.addWidget(self.exit_btn)

        self.v_main_layout.addLayout(self.h_button_layout)

        self.v_main_layout.setStretch(0, 1)
        self.v_main_layout.setStretch(2, 10)
        self.v_main_layout.setStretch(4, 1)

        self.gridLayout.addLayout(self.v_main_layout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 720, 32))
        self.menu_about = QMenu(self.menubar)
        self.menu_about.setObjectName("menu_about")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_about.menuAction())
        self.menu_about.addAction(self.menu_about_manual)
        self.menu_about.addAction(self.menu_about_update)
        self.menu_about.addAction(self.menu_about_about)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Image Stitcher", None)
        )
        self.menu_about_about.setText(
            QCoreApplication.translate("MainWindow", "\u95dc\u65bc", None)
        )
        self.menu_about_manual.setText(
            QCoreApplication.translate("MainWindow", "\u4f7f\u7528\u8aaa\u660e", None)
        )
        self.menu_about_update.setText(
            QCoreApplication.translate("MainWindow", "\u6aa2\u67e5\u66f4\u65b0", None)
        )
        self.image_mode_lb.setText(
            QCoreApplication.translate(
                "MainWindow", "\u63a5\u5408\u6a21\u5f0f\uff1a", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.horizon_rtn.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u5716\u7247\u8b80\u53d6\u6642\u53ea\u8f09\u5165\u6a94\u540d",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.horizon_rtn.setText(
            QCoreApplication.translate("MainWindow", "\u6c34\u5e73", None)
        )
        # if QT_CONFIG(tooltip)
        self.vertical_rtn.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u5716\u7247\u8b80\u53d6\u6642\u8f09\u5165\u7e2e\u5716",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.vertical_rtn.setText(
            QCoreApplication.translate("MainWindow", "\u5782\u76f4", None)
        )
        # if QT_CONFIG(tooltip)
        self.clear_list_btn.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "\u6e05\u7a7a\u5217\u8868\u7684\u7269\u4ef6", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.clear_list_btn.setText(
            QCoreApplication.translate("MainWindow", "\u6e05\u7a7a\u5217\u8868", None)
        )
        self.item_list_info_lb.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u96d9\u64ca\u5217\u8868\u7269\u4ef6\u53ef\u986f\u793a\u653e\u5927\u5716\u7247\uff0c\u6ed1\u9f20\u53ef\u62d6\u66f3\u7269\u4ef6\u4f86\u6392\u5e8f",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.start_btn.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u958b\u555f\u5831\u544a\u532f\u51fa\u8a2d\u5b9a\u8996\u7a97",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.start_btn.setText(
            QCoreApplication.translate("MainWindow", "\u958b\u59cb", None)
        )
        # if QT_CONFIG(tooltip)
        self.exit_btn.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "\u95dc\u9589\u61c9\u7528\u7a0b\u5f0f", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.exit_btn.setText(
            QCoreApplication.translate("MainWindow", "\u96e2\u958b", None)
        )
        self.menu_about.setTitle(
            QCoreApplication.translate("MainWindow", "\u8aaa\u660e", None)
        )

    # retranslateUi
