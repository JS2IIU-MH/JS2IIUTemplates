'''tkinter filedialog sample

    open filedialog to select file. returns file full path
'''

import os
from tkinter import filedialog

currentPath, basename = os.path.split(__file__)
filepath = filedialog.askopenfilename(
    title='Select File',
    filetypes=[('CSV file', '.csv'), ('Log File', '.log .lgf')],
    initialdir=currentPath
)
