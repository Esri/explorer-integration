"""
COPYRIGHT 2016 ESRI

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
"""

'''EXAMPLE OF HOW TO CALL -- THIS WOULD ALL BE OUTSIDE LIBRARY'''
'''import library'''
# if library is inside folder as your script you can use:
# import ExplorerURLScheme
# or explicitly point to folders with dot notation
from src.Python.ExplorerURLScheme_GeneratorLibrary.ExplorerURLScheme import ExplorerURLHyperlinks

INCLUDE_QRCODES = False

'''1) Call to libraries -- Generate multiple link pages from either explicit list of CSV'''
# prepare list of link lists from CSV and generate html page
hyperlinkObject = ExplorerURLHyperlinks()
fileLocation = './applink_testcases.csv'
csvLists = hyperlinkObject.csv2Lists(fileLocation, delimiter=",")  # change the 'csv2Lists()' indices in library if different than example csv
htmlPageTitle = "Explorer"

if INCLUDE_QRCODES:
    hyperlinkObject.generateStyledHTMLpage(csvLists, htmlPageTitle, styleFile="./styles/popup.css", includeQR=True, imageDirectory='./qrcodes/')
else:
    hyperlinkObject.generateHTMLpage(csvLists, htmlPageTitle)
