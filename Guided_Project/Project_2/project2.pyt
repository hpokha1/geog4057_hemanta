# -*- coding: utf-8 -*-

import arcpy
from csv_gee import get_elevation_from_gee

class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = " Project 2 Toolbox"
        self.alias = "Project 2"

        # List of tool classes associated with this toolbox
        self.tools = [Gee_elev]


class Gee_elev:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""

    def getParameterInfo(self):
        """Define the tool parameters."""
        param0 = arcpy.Parameter(
            displayName="CSV File",
            name="csv_file",
            datatype="DEFile",
            parameterType="Required",
            direction="Input")
        
        #param1 is a shapefile
        param1 = arcpy.Parameter(
            displayName="Shapefile",
            name="shapefile",
            datatype="DEFile",
            parameterType="Required",
            direction="Output")
        
        #param2 is a integer for factoey code
        param2 = arcpy.Parameter(
            displayName="Factory Code",
            name="factoryCode",
            datatype="GPLong",
            parameterType="Required",
            direction="Input")
        
        params = [param0, param1, param2]
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        csv_file = parameters[0].valueAsText
        shapefile = parameters[1].valueAsText
        factoryCode = parameters[2].Value
        get_elevation_from_gee(csv_file, shapefile, factoryCode)
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
