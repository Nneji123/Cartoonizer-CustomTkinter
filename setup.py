"""A very simple setup script to create a single executable using Tkinter.
test_tkinter.py is a very simple type of Tkinter application.
Run the build process by running the command 'python setup.py build'
If everything works well you should find a subdirectory in the build
subdirectory that contains the files needed to run the script without Python.
"""

import os
import sys

from cx_Freeze import Executable, setup

base = "Win32GUI" if sys.platform == "win32" else None
executables = [Executable("app.py", base=base)]
includefiles = [(os.path.abspath("logo.ico"), "logo.ico")]

setup(
    name="Cartoonizer App",
    version="0.2",
    description="Simple app to cartoonize images",
    options={"build_exe": {"include_files": includefiles}},
    executables=executables,
)