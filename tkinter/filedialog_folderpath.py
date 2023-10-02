'''tkinter filedialog sample

    open filedialog to select directory/folder. returns file object
'''

import os
from tkinter import filedialog

currentPath, basename = os.path.split(__file__)
dirPath = filedialog.askdirectory(initialdir=currentPath)
