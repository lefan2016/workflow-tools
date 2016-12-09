# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\tdumonet\PycharmProjects\workflow-tools\Pipe_launcher\sources\interface.ui'
#
# Created: Mon Dec 05 14:55:21 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

import sys
from PySide import QtCore, QtGui
from interface2 import Ui_Form

class MyMainWindow(QtGui.QWidget, Ui_Form):
    """Classe qui determine l'interface"""

    def __init__(self, parent=None):
        # On initialise les classe parentes
        super(MyMainWindow, self).__init__(parent)
        # On execute la fonction de creation de l'interface
        self.setupUi(self)
        """
        La ligne dessous sers a aligner tous les elements d'un vertical layout vers le haut, c'est pas dans les options du Designer, et c'est pratique pour maya.

        self.verticalLayout.setAlignment(QtCore.Qt.AlignTop)
        """


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyMainWindow()
    myapp.show()
    sys.exit(app.exec_())
