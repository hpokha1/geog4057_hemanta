# -*- coding: utf-8 -*-

import arcpy
from JsonToShapefile import importNoTaxJSON

class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""

    def getParameterInfo(self):
        """Define the tool parameters."""
        param_ws = arcpy.Parameter(
            name="workspace",
            displayName="Workspace",
            direction="Input",
            parameterType="Required",
            datatype="DEWorkspace"
        )
        
        param_json = arcpy.Parameter(
            name="json",
            displayName="No Tax JSON",
            direction="Input",
            parameterType="Required",
            datatype="DEFile"
        )
        
        param_out = arcpy.Parameter(
            name="Output",
            displayName="Output shapefile",
            parameterType="Required",
            direction="Output",
            datatype="GPString"
        )

        params = [param_ws, param_json, param_out]
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
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
