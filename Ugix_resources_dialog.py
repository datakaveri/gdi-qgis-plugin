# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Ugix_resourcesDialog
                                 A QGIS plugin
 This plugin is used to get the data from ugix server
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-07-03
        git sha              : $Format:%H$
        copyright            : (C) 2024 by Sirpi
        email                : shine@sirpi.io
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'Ugix_resources_dialog_base.ui'))


class Ugix_resourcesDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(Ugix_resourcesDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        # Connect radio buttons to the filtering slot
        self.radioButtonAll.toggled.connect(self.filter_data)
        self.radioButtonPrivate.toggled.connect(self.filter_data)
        # Update the widget name if it's different
        self.radioButtonPublic.toggled.connect(self.filter_data)
        
        # Store the original data to be filtered
        self.original_data = []

    def filter_data(self):
        """Filter data based on the selected radio button."""
        if not self.original_data:
            return  # No data to filter
        
        # Determine which radio button is selected
        if self.radioButtonAll.isChecked():
            filtered_data = self.original_data
        elif self.radioButtonPublic.isChecked():
            filtered_data = [item for item in self.original_data if item.get('accessPolicy') == 'OPEN']
        elif self.radioButtonPrivate.isChecked():
            filtered_data = [item for item in self.original_data if item.get('accessPolicy') == 'SECURE']
        else:
            filtered_data = []
        
        # Update the display with the filtered data
        self.display_data_in_scroll_area(filtered_data)