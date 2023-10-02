'''tkinter filedialog sample

    open filedialog to select file. returns file object.
    just copy lines to your code.
'''

import os
from tkinter import filedialog

currentPath, basename = os.path.split(__file__)
fileobj = filedialog.askopenfile(
    title='Select File',
    filetypes=[('CSV file', '.csv'), ('Log File', '.log .lgf')],
    initialdir=currentPath
)
