# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\datmant.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DATMantMainWindow(object):
    def setupUi(self, DATMantMainWindow):
        DATMantMainWindow.setObjectName("DATMantMainWindow")
        DATMantMainWindow.resize(820, 620)
        DATMantMainWindow.setMinimumSize(QtCore.QSize(820, 620))
        self.centralwidget = QtWidgets.QWidget(DATMantMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gbAnnotWindow = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gbAnnotWindow.setFont(font)
        self.gbAnnotWindow.setObjectName("gbAnnotWindow")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.gbAnnotWindow)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.figThinFigure = QtWidgets.QVBoxLayout()
        self.figThinFigure.setObjectName("figThinFigure")
        self.horizontalLayout_3.addLayout(self.figThinFigure)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.gbAnnotWindow)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_8.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.gbAnnotWindow)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.sldBrushDiameter = QtWidgets.QSlider(self.gbAnnotWindow)
        self.sldBrushDiameter.setOrientation(QtCore.Qt.Horizontal)
        self.sldBrushDiameter.setObjectName("sldBrushDiameter")
        self.horizontalLayout_2.addWidget(self.sldBrushDiameter)
        self.txtBrushDiameter = QtWidgets.QLineEdit(self.gbAnnotWindow)
        self.txtBrushDiameter.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtBrushDiameter.setFont(font)
        self.txtBrushDiameter.setReadOnly(True)
        self.txtBrushDiameter.setObjectName("txtBrushDiameter")
        self.horizontalLayout_2.addWidget(self.txtBrushDiameter)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.gbAnnotWindow)
        self.label_7.setMinimumSize(QtCore.QSize(72, 0))
        self.label_7.setMaximumSize(QtCore.QSize(72, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.txtImageDir = QtWidgets.QLineEdit(self.gbAnnotWindow)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtImageDir.setFont(font)
        self.txtImageDir.setReadOnly(True)
        self.txtImageDir.setObjectName("txtImageDir")
        self.horizontalLayout.addWidget(self.txtImageDir)
        self.btnBrowseImageDir = QtWidgets.QPushButton(self.gbAnnotWindow)
        self.btnBrowseImageDir.setObjectName("btnBrowseImageDir")
        self.horizontalLayout.addWidget(self.btnBrowseImageDir)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lstImages = QtWidgets.QComboBox(self.gbAnnotWindow)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lstImages.setFont(font)
        self.lstImages.setObjectName("lstImages")
        self.gridLayout.addWidget(self.lstImages, 2, 2, 1, 3)
        self.label = QtWidgets.QLabel(self.gbAnnotWindow)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 3, 1, 1)
        self.txtImageStatus = QtWidgets.QLineEdit(self.gbAnnotWindow)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtImageStatus.setFont(font)
        self.txtImageStatus.setReadOnly(True)
        self.txtImageStatus.setObjectName("txtImageStatus")
        self.gridLayout.addWidget(self.txtImageStatus, 3, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gbAnnotWindow)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gbAnnotWindow)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)
        self.txtImageHasDefectMask = QtWidgets.QLineEdit(self.gbAnnotWindow)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtImageHasDefectMask.setFont(font)
        self.txtImageHasDefectMask.setReadOnly(True)
        self.txtImageHasDefectMask.setObjectName("txtImageHasDefectMask")
        self.gridLayout.addWidget(self.txtImageHasDefectMask, 3, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_8.addLayout(self.verticalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnPrev = QtWidgets.QPushButton(self.gbAnnotWindow)
        self.btnPrev.setObjectName("btnPrev")
        self.horizontalLayout_4.addWidget(self.btnPrev)
        self.btnClear = QtWidgets.QPushButton(self.gbAnnotWindow)
        self.btnClear.setEnabled(True)
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout_4.addWidget(self.btnClear)
        self.btnMode = QtWidgets.QPushButton(self.gbAnnotWindow)
        self.btnMode.setObjectName("btnMode")
        self.horizontalLayout_4.addWidget(self.btnMode)
        self.btnNext = QtWidgets.QPushButton(self.gbAnnotWindow)
        self.btnNext.setObjectName("btnNext")
        self.horizontalLayout_4.addWidget(self.btnNext)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.gbAnnotWindow)
        self.gbApplicationLog = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbApplicationLog.sizePolicy().hasHeightForWidth())
        self.gbApplicationLog.setSizePolicy(sizePolicy)
        self.gbApplicationLog.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gbApplicationLog.setFont(font)
        self.gbApplicationLog.setObjectName("gbApplicationLog")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gbApplicationLog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.txtConsole = QtWidgets.QTextEdit(self.gbApplicationLog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtConsole.setFont(font)
        self.txtConsole.setObjectName("txtConsole")
        self.verticalLayout_3.addWidget(self.txtConsole)
        self.verticalLayout_2.addWidget(self.gbApplicationLog)
        DATMantMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DATMantMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        DATMantMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DATMantMainWindow)
        self.statusbar.setObjectName("statusbar")
        DATMantMainWindow.setStatusBar(self.statusbar)
        self.actionLog = QtWidgets.QAction(DATMantMainWindow)
        self.actionLog.setCheckable(True)
        self.actionLog.setObjectName("actionLog")
        self.actionRefresh_data_file = QtWidgets.QAction(DATMantMainWindow)
        self.actionRefresh_data_file.setObjectName("actionRefresh_data_file")
        self.actionRefresh_predictor = QtWidgets.QAction(DATMantMainWindow)
        self.actionRefresh_predictor.setObjectName("actionRefresh_predictor")
        self.actionSave_current_annotations = QtWidgets.QAction(DATMantMainWindow)
        self.actionSave_current_annotations.setObjectName("actionSave_current_annotations")
        self.actionLoad_marked_image = QtWidgets.QAction(DATMantMainWindow)
        self.actionLoad_marked_image.setCheckable(True)
        self.actionLoad_marked_image.setChecked(True)
        self.actionLoad_marked_image.setObjectName("actionLoad_marked_image")
        self.actionReload_original_mask = QtWidgets.QAction(DATMantMainWindow)
        self.actionReload_original_mask.setEnabled(False)
        self.actionReload_original_mask.setObjectName("actionReload_original_mask")
        self.actionProcess_original_mask = QtWidgets.QAction(DATMantMainWindow)
        self.actionProcess_original_mask.setCheckable(True)
        self.actionProcess_original_mask.setEnabled(False)
        self.actionProcess_original_mask.setObjectName("actionProcess_original_mask")
        self.actionAIMask = QtWidgets.QAction(DATMantMainWindow)
        self.actionAIMask.setObjectName("actionAIMask")
        self.menuFile.addAction(self.actionSave_current_annotations)
        self.menuFile.addAction(self.actionReload_original_mask)
        self.menuView.addAction(self.actionLoad_marked_image)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionLog)
        self.menuEdit.addAction(self.actionProcess_original_mask)
        self.menuEdit.addAction(self.actionAIMask)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(DATMantMainWindow)
        QtCore.QMetaObject.connectSlotsByName(DATMantMainWindow)

    def retranslateUi(self, DATMantMainWindow):
        _translate = QtCore.QCoreApplication.translate
        DATMantMainWindow.setWindowTitle(_translate("DATMantMainWindow", "DATM annotation tool"))
        self.gbAnnotWindow.setTitle(_translate("DATMantMainWindow", "Annotation window"))
        self.label_2.setText(_translate("DATMantMainWindow", "Brush diameter:"))
        self.label_7.setText(_translate("DATMantMainWindow", "Image folder:"))
        self.btnBrowseImageDir.setText(_translate("DATMantMainWindow", "Browse..."))
        self.label.setText(_translate("DATMantMainWindow", "Has updated mask?"))
        self.label_14.setText(_translate("DATMantMainWindow", "Image status:"))
        self.label_15.setText(_translate("DATMantMainWindow", "Current image:"))
        self.btnPrev.setText(_translate("DATMantMainWindow", "[P] Previous image"))
        self.btnPrev.setShortcut(_translate("DATMantMainWindow", "P"))
        self.btnClear.setText(_translate("DATMantMainWindow", "[R] Clear current annotations"))
        self.btnClear.setShortcut(_translate("DATMantMainWindow", "R"))
        self.btnMode.setText(_translate("DATMantMainWindow", "Mode [Marking defects]"))
        self.btnMode.setShortcut(_translate("DATMantMainWindow", "M"))
        self.btnNext.setText(_translate("DATMantMainWindow", "[N] Next image"))
        self.btnNext.setShortcut(_translate("DATMantMainWindow", "N"))
        self.gbApplicationLog.setTitle(_translate("DATMantMainWindow", "Application log"))
        self.menuFile.setTitle(_translate("DATMantMainWindow", "File"))
        self.menuView.setTitle(_translate("DATMantMainWindow", "View"))
        self.menuEdit.setTitle(_translate("DATMantMainWindow", "Edit"))
        self.actionLog.setText(_translate("DATMantMainWindow", "Log"))
        self.actionRefresh_data_file.setText(_translate("DATMantMainWindow", "Refresh data file"))
        self.actionRefresh_predictor.setText(_translate("DATMantMainWindow", "Refresh predictor"))
        self.actionSave_current_annotations.setText(_translate("DATMantMainWindow", "Save current annotations"))
        self.actionLoad_marked_image.setText(_translate("DATMantMainWindow", "Load marked image"))
        self.actionReload_original_mask.setText(_translate("DATMantMainWindow", "Reload original mask"))
        self.actionProcess_original_mask.setText(_translate("DATMantMainWindow", "Process original mask"))
        self.actionAIMask.setText(_translate("DATMantMainWindow", "Reload AUTO defect mask"))

