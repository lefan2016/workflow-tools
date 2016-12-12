from PySide import QtCore, QtGui
from subprocess import Popen, PIPE
import sys
import os

def ressource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Application(QtGui.QWidget):
    """docstring for Application"""

    def __init__(self):
        super(Application, self).__init__()
        self.softwares = []
        self.env_vars = {}
        self.set_default_software()
        self.setup_ui()
        self.setWindowTitle("App launcher")
        self.resize(400, 300)
        self.createActions()
        self.createTrayIcon()
        self.trayIcon.show()
        self.setIcon()

        self.trayIcon.activated.connect(self.trayIconClicked)
        self.add_button.clicked.connect(self.add_env_var)
        self.run_button.clicked.connect(self.run_software)

    def trayIconClicked(self, reason):
        if reason == QtGui.QSystemTrayIcon.ActivationReason.DoubleClick:
            self.showNormal()

    def set_default_software(self):
        maya_icon = ressource_path("Maya-icon.png")
        maya_exe = "C:\\Program Files\\Autodesk\\Maya2017\\bin\\maya.exe"
        maya_name = "Maya 2017"

        maya_software = {
            "name": maya_name,
            "icon": maya_icon,
            "exe": maya_exe
        }

        blender_software = {
            "name": "Blender",
            "icon": ressource_path("Blender-icon.png"),
            "exe": "C:\\Program Files\\Blender Foundation\\Blender\\blender.exe"}
        self.softwares.append(maya_software)
        self.softwares.append(blender_software)

    def setup_ui(self):
        # Apps-------------------------------------------------------
        self.applicationGroupBox = QtGui.QGroupBox("Application")
        self.applicationLabel = QtGui.QLabel("Application:")

        self.applicationComboBox = QtGui.QComboBox()
        for soft in self.softwares:
            self.applicationComboBox.addItem(
                QtGui.QIcon(soft['icon']), soft['name'])

        app_layout = QtGui.QHBoxLayout()
        app_layout.addWidget(self.applicationLabel)
        app_layout.addWidget(self.applicationComboBox)
        app_layout.addStretch()
        self.applicationGroupBox.setLayout(app_layout)
        # ENV VARS ------------------------------------------------------
        self.variablesGroupBox = QtGui.QGroupBox("Environment variables")

        typeLabel = QtGui.QLabel("Name:")
        titleLabel = QtGui.QLabel("Value:")

        self.var_layout = QtGui.QFormLayout()
        self.var_layout.addRow(typeLabel, titleLabel)

        self.var_layout.addRow(QtGui.QLineEdit(), QtGui.QLineEdit())
        self.add_button = QtGui.QPushButton("Add")
        self.var_layout.setWidget(2, QtGui.QFormLayout.LabelRole, self.add_button)
        # self.var_layout.addRow()
        self.variablesGroupBox.setLayout(self.var_layout)

        self.run_button = QtGui.QPushButton("Run")
        self.mainLayout = QtGui.QVBoxLayout()
        self.mainLayout.addWidget(self.applicationGroupBox)
        self.mainLayout.addWidget(self.variablesGroupBox)
        self.mainLayout.addWidget(self.run_button)
        # self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.mainLayout)

    def update_UI(self):
        pass

    def add_env_var(self):
        self.var_layout.removeWidget(self.add_button)
        # self.add_button.deleteLater()
        self.var_layout.addRow(QtGui.QLineEdit(), QtGui.QLineEdit())
        self.var_layout.setWidget(self.var_layout.rowCount(), QtGui.QFormLayout.LabelRole, self.add_button)
        # print self.var_layout.itemAt(self.var_layout.count()-1).widget().text()

    def get_env_var(self):
        env_name_list = []
        env_value_list = []
        new_dict = {}

        for i in range(self.var_layout.count() - 3):
            if i % 2 == 0:
                env_name_list.append(self.var_layout.itemAt(i + 2).widget().text())
            else:
                env_value_list.append(self.var_layout.itemAt(i + 2).widget().text())

        for name, value in zip(env_name_list, env_value_list):
            if (name != "") and (value != ""):
                if name in new_dict:
                    # append the new number to the existing array at this slot
                    new_dict[name].append(value)
                else:
                    # create a new array in this slot
                    new_dict[name] = [value]

        self.env_vars = new_dict

    def setIcon(self):
        icon = QtGui.QIcon(ressource_path("Cassette.ico"))
        self.trayIcon.setIcon(icon)
        self.setWindowIcon(icon)

    def run_software(self):
        self.get_env_var()
        exe = self.softwares[self.applicationComboBox.currentIndex()]['exe']

        if self.env_vars != {}:
            for env_name, env_var in self.env_vars.iteritems():
                for var in env_var:
                    try:
                        print os.environ[env_name][-1]
                        if os.environ[env_name][-1] != os.pathsep:
                            os.environ[env_name] += os.pathsep + var
                        else:
                            os.environ[env_name] += var
                    except KeyError:
                        os.environ[env_name] = var
                    print env_name + " : " + os.environ[env_name]

        process = Popen(exe, close_fds=True)

    def createActions(self):
        self.minimizeAction = QtGui.QAction("Mi&nimize", self,
                                            triggered=self.hide)

        self.restoreAction = QtGui.QAction("&Restore", self,
                                           triggered=self.showNormal)

        self.quitAction = QtGui.QAction("&Quit", self,
                                        triggered=QtGui.qApp.quit)

    def createTrayIcon(self):
        self.trayIconMenu = QtGui.QMenu(self)
        self.trayIconMenu.addAction(self.minimizeAction)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)

        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    if not QtGui.QSystemTrayIcon.isSystemTrayAvailable():
        QtGui.QMessageBox.critical(None, "Systray",
                                   "I couldn't detect any system tray on this system.")
        sys.exit(1)

    QtGui.QApplication.setQuitOnLastWindowClosed(False)

    my_app = Application()
    my_app.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
    my_app.show()
    sys.exit(app.exec_())
