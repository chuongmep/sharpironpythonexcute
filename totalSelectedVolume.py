"""Calculates total volume of all selected elements."""

import clr
clr.AddReference('RevitAPI')
import Autodesk
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import TaskDialog
clr.AddReference('RevitServices')

myDialog = TaskDialog("Volume Result:")
myDialog.MainInstruction = "Hello1"
myDialog.ExpandedContent = "Hello2"
myDialog.Show()
#print(unitTypes)
