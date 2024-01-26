MultiLC
=======

MultiLC is a mod launcher for Lethal Company that allows you to easily separate your BepInEx mods into separate instances.

### How to run
To run it, simply extract the files into its own folder. Be sure to keep main.exe and lc_loc.txt in the same folder.
After that, you can run the "main.exe" file.
You will have to select your Lethal Company folder, close the program, and then run it again.

### How it works
A folder named "Instances" is created within your BepInEx folder in Lethal Company. 
Whenever you launch an instance, your plugins folder is cleared and the contents of the instance are copied over.

<p align="center">
  <img src="https://raw.githubusercontent.com/Brfy/MultiLC/main/multiLCinstances.png" alt="MultiLC interface"/>
</p>

### Building
If you want to build the launcher yourself, you will need pyinstaller, customtkinter, shutil, and pathlib.

### Acknowledgements
<p>
Built using Python
</p>
<p>
Packaged using PyInstaller
</p>
<p>
GUI created using CustomTkinter
</p>
