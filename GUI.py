import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from DataPlot import *


class Ui_spirometry(object):
        def __init__(self):
               self.currentReading = 0
               self.signalobj = DataPlot()
               
        def lungTransition(self, currentPoint):
                if currentPoint == 0:
                        self.LungImagelabel.setPixmap(QtGui.QPixmap("Images/EmptyLungs.png"))                        
                elif currentPoint <= 500:
                        self.LungImagelabel.setPixmap(QtGui.QPixmap("Images/GreenLungs.png"))
                elif currentPoint > 500 and currentPoint <= 1300:
                        self.LungImagelabel.setPixmap(QtGui.QPixmap("Images/OrangeLungs.png"))
                elif currentPoint > 1300:
                        self.LungImagelabel.setPixmap(QtGui.QPixmap("Images/RedLungs.png"))


             
               
        def setupUi(self, spirometry):
                spirometry.setObjectName("spirometry")
                spirometry.resize(1079, 834)
                spirometry.setMinimumSize(QtCore.QSize(1, 0))
                spirometry.setStyleSheet(" background-repeat: no-repeat;\n"
        "/*background-image: url(C://Users//Ahmed Taha//Downloads//background.png);*/\n"
        "background-size: contain;\n"
        "background-color: #1D5181;")
                self.centralwidget = QtWidgets.QWidget(spirometry)
                self.centralwidget.setObjectName("centralwidget")
                self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
                self.gridLayout_2.setObjectName("gridLayout_2")
                self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_6.setObjectName("horizontalLayout_6")
                spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_6.addItem(spacerItem)
                self.TopBox = QtWidgets.QGroupBox(self.centralwidget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.TopBox.sizePolicy().hasHeightForWidth())
                self.TopBox.setSizePolicy(sizePolicy)
                self.TopBox.setMinimumSize(QtCore.QSize(946, 413))
                self.TopBox.setStyleSheet("border:none;")
                self.TopBox.setObjectName("TopBox")
                self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.TopBox)
                self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                self.picBox = QtWidgets.QGroupBox(self.TopBox)
                self.picBox.setMinimumSize(QtCore.QSize(500, 390))
                self.picBox.setStyleSheet("border:none;\n"
        "")
                self.picBox.setObjectName("picBox")
                self.gridLayout = QtWidgets.QGridLayout(self.picBox)
                self.gridLayout.setObjectName("gridLayout")
                self.LungImagelabel = QtWidgets.QLabel(self.picBox)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.LungImagelabel.sizePolicy().hasHeightForWidth())
                self.LungImagelabel.setSizePolicy(sizePolicy)
                self.LungImagelabel.setMinimumSize(QtCore.QSize(500, 390))
                self.LungImagelabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.LungImagelabel.setStyleSheet("color: white;\n"
        "background-color: #33628d;\n"
        "border-radius:20px")
                self.LungImagelabel.setText("")
                self.LungImagelabel.setPixmap(QtGui.QPixmap("Images/EmptyLungs.png"))
                self.LungImagelabel.setScaledContents(True)
                self.LungImagelabel.setObjectName("LungImagelabel")
                self.gridLayout.addWidget(self.LungImagelabel, 0, 0, 1, 1)
                self.measurmentsBox = QtWidgets.QGroupBox(self.picBox)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.measurmentsBox.sizePolicy().hasHeightForWidth())
                self.measurmentsBox.setSizePolicy(sizePolicy)
                self.measurmentsBox.setMinimumSize(QtCore.QSize(399, 370))
                self.measurmentsBox.setObjectName("measurmentsBox")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.measurmentsBox)
                self.verticalLayout.setObjectName("verticalLayout")
                self.FCVbox = QtWidgets.QGroupBox(self.measurmentsBox)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.FCVbox.sizePolicy().hasHeightForWidth())
                self.FCVbox.setSizePolicy(sizePolicy)
                self.FCVbox.setMinimumSize(QtCore.QSize(174, 76))
                self.FCVbox.setMaximumSize(QtCore.QSize(368, 59))
                self.FCVbox.setStyleSheet("border:none;")
                self.FCVbox.setObjectName("FCVbox")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.FCVbox)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.FVClabel = QtWidgets.QLabel(self.FCVbox)
                self.FVClabel.setMinimumSize(QtCore.QSize(174, 59))
                self.FVClabel.setMaximumSize(QtCore.QSize(174, 59))
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.FVClabel.setFont(font)
                self.FVClabel.setStyleSheet("color: white;\n"
        "background-image:white;\n"
        "background-color: #133453;\n"
        "border-radius:20px")
                self.FVClabel.setAlignment(QtCore.Qt.AlignCenter)
                self.FVClabel.setObjectName("FVClabel")
                self.horizontalLayout_2.addWidget(self.FVClabel)
                self.FVC = QtWidgets.QLabel(self.FCVbox)
                self.FVC.setMinimumSize(QtCore.QSize(174, 59))
                self.FVC.setMaximumSize(QtCore.QSize(174, 59))
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.FVC.setFont(font)
                self.FVC.setStyleSheet("color: white;\n"
        "background-image:white;\n"
        "background-color: #133453;\n"
        "border-radius:20px")
                self.FVC.setAlignment(QtCore.Qt.AlignCenter)
                self.FVC.setObjectName("FVC")
                self.horizontalLayout_2.addWidget(self.FVC)
                self.verticalLayout.addWidget(self.FCVbox)
                self.FEFbox = QtWidgets.QGroupBox(self.measurmentsBox)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.FEFbox.sizePolicy().hasHeightForWidth())
                self.FEFbox.setSizePolicy(sizePolicy)
                self.FEFbox.setMinimumSize(QtCore.QSize(174, 76))
                self.FEFbox.setMaximumSize(QtCore.QSize(368, 59))
                self.FEFbox.setStyleSheet("border:none;")
                self.FEFbox.setObjectName("FEFbox")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.FEFbox)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.FEFlabel = QtWidgets.QLabel(self.FEFbox)
                self.FEFlabel.setMinimumSize(QtCore.QSize(174, 59))
                self.FEFlabel.setMaximumSize(QtCore.QSize(174, 59))
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.FEFlabel.setFont(font)
                self.FEFlabel.setStyleSheet("color: white;\n"
        "background-image:white;\n"
        "background-color: #133453;\n"
        "border-radius:20px")
                self.FEFlabel.setAlignment(QtCore.Qt.AlignCenter)
                self.FEFlabel.setObjectName("FEFlabel")
                self.horizontalLayout_3.addWidget(self.FEFlabel)
                self.FEF = QtWidgets.QLabel(self.FEFbox)
                self.FEF.setMinimumSize(QtCore.QSize(174, 59))
                self.FEF.setMaximumSize(QtCore.QSize(174, 59))
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.FEF.setFont(font)
                self.FEF.setStyleSheet("color: white;\n"
        "background-image:white;\n"
        "background-color: #133453;\n"
        "border-radius:20px")
                self.FEF.setAlignment(QtCore.Qt.AlignCenter)
                self.FEF.setObjectName("FEF")
                self.horizontalLayout_3.addWidget(self.FEF)
                self.verticalLayout.addWidget(self.FEFbox)
                self.PEFRbox = QtWidgets.QGroupBox(self.measurmentsBox)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.PEFRbox.sizePolicy().hasHeightForWidth())
                self.PEFRbox.setSizePolicy(sizePolicy)
                self.PEFRbox.setMinimumSize(QtCore.QSize(174, 76))
                self.PEFRbox.setMaximumSize(QtCore.QSize(368, 59))
                self.PEFRbox.setStyleSheet("border:none;")
                self.PEFRbox.setObjectName("PEFRbox")
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.PEFRbox)
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                self.PEFRlabel = QtWidgets.QLabel(self.PEFRbox)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.PEFRlabel.sizePolicy().hasHeightForWidth())
                self.PEFRlabel.setSizePolicy(sizePolicy)
                self.PEFRlabel.setMinimumSize(QtCore.QSize(174, 59))
                self.PEFRlabel.setMaximumSize(QtCore.QSize(174, 59))
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.PEFRlabel.setFont(font)
                self.PEFRlabel.setStyleSheet("color: white;\n"
        "background-image:white;\n"
        "background-color: #133453;\n"
        "border-radius:20px")
                self.PEFRlabel.setAlignment(QtCore.Qt.AlignCenter)
                self.PEFRlabel.setObjectName("PEFRlabel")
                self.horizontalLayout_4.addWidget(self.PEFRlabel)
                self.PEFR = QtWidgets.QLabel(self.PEFRbox)
                self.PEFR.setMinimumSize(QtCore.QSize(174, 59))
                self.PEFR.setMaximumSize(QtCore.QSize(174, 59))
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.PEFR.setFont(font)
                self.PEFR.setStyleSheet("color: white;\n"
        "background-image:white;\n"
        "background-color: #133453;\n"
        "border-radius:20px")
                self.PEFR.setAlignment(QtCore.Qt.AlignCenter)
                self.PEFR.setObjectName("PEFR")
                self.horizontalLayout_4.addWidget(self.PEFR)
                self.verticalLayout.addWidget(self.PEFRbox)
                self.gridLayout.addWidget(self.measurmentsBox, 0, 1, 1, 1)
                self.horizontalLayout_5.addWidget(self.picBox)
                self.horizontalLayout_6.addWidget(self.TopBox)
                spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_6.addItem(spacerItem1)
                self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
                self.graphBox = QtWidgets.QGroupBox(self.centralwidget)
                self.graphBox.setMinimumSize(QtCore.QSize(954, 298))
                self.graphBox.setStyleSheet("border: none;")
                self.graphBox.setObjectName("graphBox")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.graphBox)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.FlowGraph = PlotWidget(self.graphBox)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.FlowGraph.sizePolicy().hasHeightForWidth())
                self.FlowGraph.setSizePolicy(sizePolicy)
                self.FlowGraph.setMinimumSize(QtCore.QSize(756, 280))
                self.FlowGraph.setStyleSheet("background-color: #133453;\n"
        "Border: none;")
                self.FlowGraph.setObjectName("FlowGraph")
                self.horizontalLayout.addWidget(self.FlowGraph)
                spacerItem2 = QtWidgets.QSpacerItem(37, 89, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout.addItem(spacerItem2)
                self.verticalLayout_2 = QtWidgets.QVBoxLayout()
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_2.addItem(spacerItem3)
                self.FlowValue = QtWidgets.QLabel(self.graphBox)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.FlowValue.sizePolicy().hasHeightForWidth())
                self.FlowValue.setSizePolicy(sizePolicy)
                self.FlowValue.setMinimumSize(QtCore.QSize(200, 74))
                self.FlowValue.setMaximumSize(QtCore.QSize(350, 16777215))
                font = QtGui.QFont()
                font.setPointSize(26)
                font.setBold(True)
                font.setWeight(75)
                self.FlowValue.setFont(font)
                self.FlowValue.setStyleSheet("color: white;\n"
        "background-image:white;\n"
        "background-color: #133453;\n"
        "border-radius:20px")
                self.FlowValue.setAlignment(QtCore.Qt.AlignCenter)
                self.FlowValue.setObjectName("FlowValue")
                self.verticalLayout_2.addWidget(self.FlowValue)
                spacerItem4 = QtWidgets.QSpacerItem(18, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_2.addItem(spacerItem4)
                self.horizontalLayout.addLayout(self.verticalLayout_2)
                self.gridLayout_2.addWidget(self.graphBox, 1, 0, 1, 1)
                spirometry.setCentralWidget(self.centralwidget)

                self.retranslateUi(spirometry)
                QtCore.QMetaObject.connectSlotsByName(spirometry)

        def retranslateUi(self, spirometry):
                _translate = QtCore.QCoreApplication.translate
                spirometry.setWindowTitle(_translate("spirometry", "spirometry"))
                self.FVClabel.setText(_translate("spirometry", "FVC"))
                self.FVC.setText(_translate("spirometry", "%"))
                self.FEFlabel.setText(_translate("spirometry", "FEF"))
                self.FEF.setText(_translate("spirometry", "%"))
                self.PEFRlabel.setText(_translate("spirometry", "PEFR"))
                self.PEFR.setText(_translate("spirometry", "%"))
                self.FlowValue.setText(_translate("spirometry", "Flow"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    spirometry = QtWidgets.QMainWindow()
    ui = Ui_spirometry()
    ui.setupUi(spirometry)
    spirometry.show()
    sys.exit(app.exec_())
