# Cura-LayerNumber-Plugin
Print current layer number on the 3D printer display.

This is a plugin for [Ultimaker Cura](https://ultimaker.com/en/products/ultimaker-cura-software), which does a bit of post processing after the file is sliced, and inserts a **M117** GCode into the file, so that your printer can display the currently printing layer number on the connected LCD display.

Two scripts are provided - one for old version of Cura - version 15.X and one for new version 3.X. Copy the appropriate script into the Cura plugins directory. 

On windows, plugin directory is:
* *%APPDATA%\cura\3.4\scripts* for Cura version 3.4
* *C:\Program Files (x86)\Cura\Cura_15.04.6\plugins* for Cura 15.04

After adding, the plugin will be available under Extension -> Post Processing -> Modify GCode menu item. When the 3D printer is printing, it will display the message like: ```Layer 3/25```.
