'''tkinter GUI sample
    open window with label, button and entry widgets.
'''

import tkinter as tk


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

        frame1 = tk.Frame(master)

        label1 = tk.Label(frame1,
                          width=15,
                          height=1,
                          text='Label 1',
                          # bg='white',
                          border=1,
                          font=('', 12, 'bold'),
                          justify=tk.CENTER,
                          padx=5,
                          pady=5,
                          # relief='ridge',
                          # textvariable=some_StringVar
                          )
        label1.grid()

        entry1 = tk.Entry(frame1,
                          background='white',
                          foreground='black',
                          width=15,
                          # font=('',10,'bold'),
                          justify=tk.CENTER,
                          relief='ridge',
                          # textvariable=some_StringVar,
                          border=1,
                          )
        entry1.grid()

        extbtn = tk.Button(frame1,
                           text='Exit',
                           # foreground='black'
                           # background='white',
                           font=('', 12, 'bold'),
                           # borderwidth=1,
                           height=1,
                           width=6,
                           justify=tk.CENTER,
                           padx=5,
                           pady=5,
                           # textvariable=some_StringVar,
                           command=quit
                           )
        extbtn.grid()
        frame1.grid()


def main():
    '''example to call Application class'''

    root = tk.Tk()

    root.geometry('400x200')
    root.title('tkinter template')

    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
