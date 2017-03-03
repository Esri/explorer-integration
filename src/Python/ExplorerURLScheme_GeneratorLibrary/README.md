# ExplorerURLScheme

A library that can be used to generate valid URL schemes for Explorer

Supports Python Python 3.4+

Within this repository you will find: 
* ExplorerURLScheme.py (the main library that will be used by the user
* ./Sample Data/applink_testcases.csv -- a csv file that has some test data
* ./Sample Data/applinks/ -- a directory to store input/output HTML files
* ./Sample Data/qrcodes/ -- a directory to store output QR Code images


In order to use the library:
* Copy ExplorerURLScheme.py to workspace (the directory from which you'll be calling the library)
* Use 'import ExplorerURLScheme' or 'from ExplorerURLScheme import *' 
* Instantiate either a 'ExplorerURLScheme' and/or 'ExplorerURLHyperlinks' object
* Use object methods 