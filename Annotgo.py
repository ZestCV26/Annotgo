from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QFrame, QHBoxLayout,
                               QLayout, QMainWindow, QMenu, QMenuBar,
                               QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
                               QTabWidget, QVBoxLayout, QWidget)


class Ui_Annotgo(object):
    def __init__(self):
        # Qframes
        self.frame_2 = QFrame(self.dockWidgetContents_5)
        self.frame = QFrame(self.dockWidgetContents_4)

        # Qlayouts
        self.verticalLayout = None
        self.dockWidget_2 = None
        self.dockWidgetContents_5 = None
        self.verticalLayout_3 = None
        self.dockWidgetContents_4 = None
        self.dockWidget = None
        self.menuHelp = None
        self.menuForms = None
        self.menuView = None
        self.menuEdit = None
        self.menuFile = None
        self.menubar = None
        self.statusbar = None
        self.imageViewer = None
        self.verticalSpacer = None
        self.OpenFile = None
        self.Save = None
        self.Draw = None
        self.PreviousFrame = None
        self.NextFrame = None
        self.Sidebar = None
        self.verticalLayout_2 = None
        self.sidebar = None
        self.horizontalLayout = None
        self.centralWidget = None
        self.OpenDir = None

    # setupUi
    def setupUi(self, Annotgo):
        if not Annotgo.objectName():
            Annotgo.setObjectName(u"Annotgo")
        Annotgo.setWindowModality(Qt.ApplicationModal)
        Annotgo.resize(620, 557)
        Annotgo.setMinimumSize(QSize(500, 500))
        Annotgo.setMaximumSize(QSize(1920, 1080))
        Annotgo.setCursor(QCursor(Qt.ArrowCursor))
        Annotgo.setMouseTracking(True)
        icon = QIcon()
        iconThemeName = u"applications-office"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile("./icons/Annotgo.png", QSize(), QIcon.Normal, QIcon.Off)
            icon.addFile("./icons/Annotgo.png", QSize(), QIcon.Disabled, QIcon.Off)
            icon.addFile("./icons/Annotgo.png", QSize(), QIcon.Selected, QIcon.Off)

        Annotgo.setWindowIcon(icon)
        Annotgo.setWindowOpacity(1.000000000000000)
        Annotgo.setToolTipDuration(0)
        Annotgo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        Annotgo.setIconSize(QSize(24, 24))
        Annotgo.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        Annotgo.setAnimated(False)
        Annotgo.setTabShape(QTabWidget.Rounded)
        self.centralWidget = QWidget(Annotgo)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setMinimumSize(QSize(300, 300))
        self.centralWidget.setMaximumSize(QSize(1920, 1080))
        self.horizontalLayout = QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sidebar = QFrame(self.centralWidget)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(250)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMinimumSize(QSize(50, 300))
        self.sidebar.setMaximumSize(QSize(50, 1080))
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sidebar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Sidebar = QVBoxLayout()
        self.Sidebar.setObjectName(u"Sidebar")
        self.Sidebar.setSizeConstraint(QLayout.SetNoConstraint)
        self.Sidebar.setContentsMargins(0, 0, 0, 0)
        self.OpenFile = QPushButton(self.sidebar)
        self.OpenFile.setObjectName(u"OpenFile")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.OpenFile.sizePolicy().hasHeightForWidth())
        self.OpenFile.setSizePolicy(sizePolicy1)
        self.OpenFile.setMaximumSize(QSize(50, 50))
        self.OpenFile.setFocusPolicy(Qt.NoFocus)
        icon1 = QIcon()
        icon1.addFile("./icons/image_file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.OpenFile.setIcon(icon1)
        self.OpenFile.setIconSize(QSize(25, 25))

        self.Sidebar.addWidget(self.OpenFile)

        self.OpenDir = QPushButton(self.sidebar)
        self.OpenDir.setObjectName(u"OpenDir")
        sizePolicy1.setHeightForWidth(self.OpenDir.sizePolicy().hasHeightForWidth())
        self.OpenDir.setSizePolicy(sizePolicy1)
        self.OpenDir.setMaximumSize(QSize(50, 50))
        self.OpenDir.setFocusPolicy(Qt.NoFocus)
        icon2 = QIcon()
        icon2.addFile("./icons/directory.png", QSize(), QIcon.Normal, QIcon.Off)
        self.OpenDir.setIcon(icon2)
        self.OpenDir.setIconSize(QSize(25, 25))

        self.Sidebar.addWidget(self.OpenDir)

        self.NextFrame = QPushButton(self.sidebar)
        self.NextFrame.setObjectName(u"NextFrame")
        sizePolicy1.setHeightForWidth(self.NextFrame.sizePolicy().hasHeightForWidth())
        self.NextFrame.setSizePolicy(sizePolicy1)
        self.NextFrame.setMaximumSize(QSize(50, 50))
        self.NextFrame.setFocusPolicy(Qt.NoFocus)
        self.NextFrame.setStyleSheet(u"font: 9pt \"Segoe Fluent Icons\";")
        icon3 = QIcon()
        icon3.addFile("./icons/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.NextFrame.setIcon(icon3)
        self.NextFrame.setIconSize(QSize(25, 25))
        self.NextFrame.setAutoDefault(False)
        self.NextFrame.setFlat(False)

        self.Sidebar.addWidget(self.NextFrame)

        self.PreviousFrame = QPushButton(self.sidebar)
        self.PreviousFrame.setObjectName(u"PreviousFrame")
        sizePolicy1.setHeightForWidth(self.PreviousFrame.sizePolicy().hasHeightForWidth())
        self.PreviousFrame.setSizePolicy(sizePolicy1)
        self.PreviousFrame.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        self.PreviousFrame.setFont(font)
        self.PreviousFrame.setFocusPolicy(Qt.NoFocus)
        self.PreviousFrame.setAcceptDrops(False)
        icon4 = QIcon()
        icon4.addFile("./icons/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.PreviousFrame.setIcon(icon4)
        self.PreviousFrame.setIconSize(QSize(25, 25))

        self.Sidebar.addWidget(self.PreviousFrame)

        self.Draw = QPushButton(self.sidebar)
        self.Draw.setObjectName(u"Draw")
        self.Draw.setMaximumSize(QSize(50, 50))
        self.Draw.setFocusPolicy(Qt.NoFocus)
        icon5 = QIcon()
        icon5.addFile("D:/Downloads/icons/bbox.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Draw.setIcon(icon5)
        self.Draw.setIconSize(QSize(25, 25))

        self.Sidebar.addWidget(self.Draw)

        self.Save = QPushButton(self.sidebar)
        self.Save.setObjectName(u"Save")
        self.Save.setMaximumSize(QSize(50, 50))
        font1 = QFont()
        font1.setStyleStrategy(QFont.NoAntialias)
        self.Save.setFont(font1)
        self.Save.setFocusPolicy(Qt.NoFocus)
        icon6 = QIcon()
        icon6.addFile("D:/Downloads/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Save.setIcon(icon6)
        self.Save.setIconSize(QSize(25, 25))

        self.Sidebar.addWidget(self.Save)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Sidebar.addItem(self.verticalSpacer)

        self.verticalLayout_2.addLayout(self.Sidebar)

        self.horizontalLayout.addWidget(self.sidebar)

        self.imageViewer = QFrame(self.centralWidget)
        self.imageViewer.setObjectName(u"imageViewer")
        self.imageViewer.setMinimumSize(QSize(300, 300))
        self.imageViewer.setMaximumSize(QSize(1344, 756))
        self.imageViewer.setFrameShape(QFrame.StyledPanel)
        self.imageViewer.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.imageViewer)

        Annotgo.setCentralWidget(self.centralWidget)
        self.statusbar = QStatusBar(Annotgo)
        self.statusbar.setObjectName(u"statusbar")
        Annotgo.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(Annotgo)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 620, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuForms = QMenu(self.menubar)
        self.menuForms.setObjectName(u"menuForms")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        Annotgo.setMenuBar(self.menubar)
        self.dockWidget = QDockWidget(Annotgo)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setMinimumSize(QSize(78, 52))
        self.dockWidget.setMaximumSize(QSize(250, 1080))
        self.dockWidget.setAutoFillBackground(False)
        self.dockWidgetContents_4 = QWidget()
        self.dockWidgetContents_4.setObjectName(u"dockWidgetContents_4")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.VLine)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame)

        self.dockWidget.setWidget(self.dockWidgetContents_4)
        Annotgo.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget)
        self.dockWidget_2 = QDockWidget(Annotgo)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        self.dockWidget_2.setMinimumSize(QSize(78, 52))
        self.dockWidget_2.setMaximumSize(QSize(250, 1080))
        self.dockWidget_2.setFocusPolicy(Qt.NoFocus)
        self.dockWidgetContents_5 = QWidget()
        self.dockWidgetContents_5.setObjectName(u"dockWidgetContents_5")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.VLine)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        self.dockWidget_2.setWidget(self.dockWidgetContents_5)
        Annotgo.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget_2)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuForms.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Annotgo)

        QMetaObject.connectSlotsByName(Annotgo)

    # retranslateUi
    def retranslateUi(self, Annotgo):
        Annotgo.setWindowTitle(QCoreApplication.translate("Annotgo", u"Annotgo", None))
        self.OpenFile.setText("")
        self.OpenDir.setText("")
        self.NextFrame.setText("")
        self.PreviousFrame.setText("")
        self.Draw.setText("")
        self.Save.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("Annotgo", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("Annotgo", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("Annotgo", u"View", None))
        self.menuForms.setTitle(QCoreApplication.translate("Annotgo", u"Forms", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Annotgo", u"Help", None))

    def pushButtonHandler(self):
        self.OpenFile
        pass

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_Annotgo()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())
