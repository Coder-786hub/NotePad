import cx_Freeze
import sys
import os
base = None
if sys.platform == "win32" :
    base = "Win32Gui"

os.environ['TCL_LIBRARY'] = r"C:\Python312\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Python312\tcl\tk8.6"

executables = [cx_Freeze.Executable("Notepad.py",base=base)]


cx_Freeze.setup(
    name = "Ak_Notepad",
    options = {"build_exe":{"packages":["tkinter","os"],"include_files":['tcl86t.dll','tk86t.dll']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
)