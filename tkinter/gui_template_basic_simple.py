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
                          text='Label 1',
                          )
        label1.grid()

        entry1 = tk.Entry(frame1,
                          justify=tk.CENTER,
                          relief='ridge',
                          border=1,
                          )
        entry1.grid()

        extbtn = tk.Button(frame1,
                           text='Exit',
                           command=quit,
                           )
        extbtn.grid()
        frame1.grid()


def main():
    '''example to call Application class'''

    root = tk.Tk()

    root.geometry('400x200')
    root.title('tkinter template')
    root.grid_anchor(tk.CENTER)

    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
