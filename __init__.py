# -*- coding: utf-8 -*-
"""
/***************************************************************************
 NCViewer
                                 A QGIS plugin
 Load and view a nautical chart for the area in view.
                             -------------------
        begin                : 2017-02-21
        copyright            : (C) 2017 by Pacific Coast Fishery Services
        email                : troy@pcfish.ca
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load NCViewer class from file NCViewer.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .nc_viewer import NCViewer
    return NCViewer(iface)
