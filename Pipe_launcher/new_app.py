from PySide import QtCore, QtGui

import systray_rc


class Window(QtGui.QDialog):
    def __init__(self):
        super(Window, self).__init__()

        #self.createIconGroupBox()
        #self.createMessageGroupBox()
        self.setupUI()
        #self.iconLabel.setMinimumWidth(self.durationLabel.sizeHint().width())

        #self.createActions()
        #self.createTrayIcon()

        #self.showMessageButton.clicked.connect(self.showMessage)
        #self.showIconCheckBox.toggled.connect(self.trayIcon.setVisible)
        #self.iconComboBox.currentIndexChanged[int].connect(self.setIcon)
        #self.trayIcon.messageClicked.connect(self.messageClicked)
        #self.trayIcon.activated.connect(self.iconActivated)



        #self.iconComboBox.setCurrentIndex(1)
        #self.trayIcon.show()

        self.setWindowTitle("App launcher")
        self.resize(400, 300)
    """
        def setVisible(self, visible):
            self.minimizeAction.setEnabled(visible)
            self.maximizeAction.setEnabled(not self.isMaximized())
            self.restoreAction.setEnabled(self.isMaximized() or not visible)
            super(Window, self).setVisible(visible)

        def closeEvent(self, event):
            if self.trayIcon.isVisible():
                QtGui.QMessageBox.information(self, "Systray",
                        "The program will keep running in the system tray. To "
                        "terminate the program, choose <b>Quit</b> in the "
                        "context menu of the system tray entry.")
                self.hide()
                event.ignore()

        def setIcon(self, index):
            icon = self.applicationComboBox.itemIcon(index)
            self.trayIcon.setIcon(icon)
            self.setWindowIcon(icon)

            self.trayIcon.setToolTip(self.applicationComboBox.itemText(index))

        def iconActivated(self, reason):
            if reason in (QtGui.QSystemTrayIcon.Trigger, QtGui.QSystemTrayIcon.DoubleClick):
                self.applicationComboBox.setCurrentIndex(
                        (self.applicationComboBox.currentIndex() + 1)
                        % self.applicationComboBox.count())
            elif reason == QtGui.QSystemTrayIcon.MiddleClick:
                self.showMessage()

        def showMessage(self):
            icon = QtGui.QSystemTrayIcon.MessageIcon(
                    self.typeComboBox.itemData(self.typeComboBox.currentIndex()))
            self.trayIcon.showMessage(self.titleEdit.text(),
                    self.bodyEdit.toPlainText(), icon,
                    self.durationSpinBox.value() * 1000)

        def messageClicked(self):
            QtGui.QMessageBox.information(None, "Systray",
                    "Sorry, I already gave what help I could.\nMaybe you should "
                    "try asking a human?")




    """
    def setupUI(self):
        self.applicationGroupBox = QtGui.QGroupBox("Application")
        self.applicationLabel = QtGui.QLabel("Application:")

        self.applicationComboBox = QtGui.QComboBox()
        self.applicationComboBox.addItem(
            QtGui.QIcon('C:\Users\Thomas\PycharmProjects\workflow-tools\Pipe_launcher\Maya-icon.png'), "Bad")
        self.applicationComboBox.addItem(QtGui.QIcon(':/images/heart.svg'), "Heart")
        self.applicationComboBox.addItem(QtGui.QIcon(':/images/trash.svg'), "Trash")

        applicationLayout = QtGui.QHBoxLayout()
        applicationLayout.addWidget(self.applicationLabel)
        applicationLayout.addWidget(self.applicationComboBox)
        applicationLayout.addStretch()
        self.applicationGroupBox.setLayout(applicationLayout)

        self.variablesGroupBox = QtGui.QGroupBox("Environment variables")

        typeLabel = QtGui.QLabel("Name:")
        titleLabel = QtGui.QLabel("Value:")

        self.titleEdit = QtGui.QLineEdit("name")
        self.variableName = QtGui.QLineEdit("value")
        messageLayout = QtGui.QGridLayout()
        messageLayout.addWidget(typeLabel, 1,1)
        messageLayout.addWidget(titleLabel, 1, 2)
        messageLayout.addWidget(self.variableName, 2, 1)
        messageLayout.addWidget(self.titleEdit, 2, 2, 1, 4)
        messageLayout.setColumnStretch(3, 1)
        messageLayout.setRowStretch(4, 1)
        self.variablesGroupBox.setLayout(messageLayout)

        self.mainLayout = QtGui.QVBoxLayout()
        self.mainLayout.addWidget(self.applicationGroupBox)
        self.mainLayout.addWidget(self.variablesGroupBox)
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.mainLayout)

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    if not QtGui.QSystemTrayIcon.isSystemTrayAvailable():
        QtGui.QMessageBox.critical(None, "Systray",
                "I couldn't detect any system tray on this system.")
        sys.exit(1)

    QtGui.QApplication.setQuitOnLastWindowClosed(False)

    window = Window()
    window.show()
    sys.exit(app.exec_())