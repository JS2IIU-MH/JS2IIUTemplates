'''tkinter GUI sample
    open window with label, button and entry widgets.
'''

import tkinter as tk
from tkinter import ttk

import pandas as pd


class Application(tk.Frame):
    '''Application - class to define GUI widgets

        tkinter widgets will be defined in Application.__init__

        Args:
            None
        Returns:
            None
    '''

    def __init__(self, master):
        super().__init__(master)
        self.grid()

        self.treeview_from_csv(master)

        frame1 = tk.Frame(master)

        label1 = tk.Label(frame1,
                          text='File: ',
                          )
        label1.grid(row=0, column=0)

        label2 = tk.Label(frame1,
                          width=15,
                          text='',
                          justify=tk.CENTER,
                          border=1,
                          )
        label2.grid(row=0, column=1)

        extbtn = tk.Button(frame1,
                           text='Exit',
                           command=quit,
                           )
        extbtn.grid(row=0, column=2)
        frame1.grid()

    def treeview_from_csv(self, master):
        ''' treeview_from_csv '''
        # read_csv
        _df = pd.read_csv('tkinter/treeview_data.csv', comment='#')
        column_list = _df.columns.to_list()

        # treeview
        self.tree = ttk.Treeview(master,
                                 columns=column_list,
                                 selectmode=tk.EXTENDED,
                                 height=5)

        # column setting
        self.tree.column('#0', width=0, stretch=tk.NO)
        for _c in column_list:
            if _c == 'ID':
                self.tree.column(_c, width=25, anchor=tk.CENTER)
            else:
                self.tree.column(_c, width=80, anchor=tk.CENTER)

        # heading
        self.tree.heading('#0', text='')
        for _c in column_list:
            self.tree.heading(_c, text=_c, anchor=tk.CENTER)

        # recoed
        for i in range(len(_df)):
            values = _df.iloc[i].to_list()
            # print(values)
            self.tree.insert(parent='', index=tk.END, iid=i, values=values)

        scrollbar = ttk.Scrollbar(master, orient=tk.VERTICAL,
                                  command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.grid(row=0, column=0)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))


def main():
    '''example to call Application class'''

    root = tk.Tk()

    root.geometry('700x200')
    root.title('Treeview Sample')
    root.grid_anchor(tk.CENTER)

    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
