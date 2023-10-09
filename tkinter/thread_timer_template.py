'''tkinter GUI & thread sample
    count up timer runs as thread.
'''

import time

import tkinter as tk
import threading


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

        # valuables
        self.flg_start = False
        self.flg_quit = False
        self.count = 0

        # thread
        self.thread1 = threading.Thread(target=self.timer)
        self.thread1.start()

        frame1 = tk.Frame(master)
        self.label1 = tk.Label(frame1,
                               width=15, height=1,
                               text='Timer',
                               border=1,
                               font=('', 45, 'bold'),
                               justify=tk.CENTER,
                               padx=5, pady=5,
                               )
        self.label1.grid()
        frame1.grid()

        frame2 = tk.Frame(master)
        start_button = tk.Button(frame2,
                                 text='Start',
                                 font=('', 12, 'bold'),
                                 height=1,
                                 width=6,
                                 justify=tk.CENTER,
                                 padx=5, pady=5,
                                 command=self.start_button_click
                                 )
        start_button.grid(row=0, column=0)

        stop_button = tk.Button(frame2,
                                text='Stop',
                                font=('', 12, 'bold'),
                                height=1,
                                width=6,
                                justify=tk.CENTER,
                                padx=5, pady=5,
                                command=self.stop_button_click
                                )
        stop_button.grid(row=0, column=1)

        reset_button = tk.Button(frame2,
                                 text='Reset',
                                 font=('', 12, 'bold'),
                                 height=1, width=6,
                                 justify=tk.CENTER,
                                 padx=5, pady=5,
                                 command=self.reset_button_click
                                 )
        reset_button.grid(row=0, column=2)
        frame2.grid()

        frame3 = tk.Frame(master)
        extbtn = tk.Button(frame3,
                           text='Exit',
                           font=('', 12, 'bold'),
                           height=1,
                           width=6,
                           justify=tk.CENTER,
                           padx=5, pady=5,
                           command=self.quit_app
                           )
        extbtn.grid()
        frame3.grid()

    def start_button_click(self):
        '''function for start button'''
        self.flg_start = True

    def stop_button_click(self):
        '''function for stop button'''
        self.flg_start = False

    def reset_button_click(self):
        '''function for reset button'''
        self.count = 0
        self.label1['text'] = self.count
        self.flg_start = False

    def quit_app(self):
        '''function for quit button'''
        self.flg_quit = True

        self.thread1.join(timeout=1)

        self.master.destroy()

    def timer(self):
        '''timer function for threading'''
        while not self.flg_quit:
            if self.flg_start:
                self.label1['text'] = self.count
                self.count += 1

            time.sleep(1)


def main():
    '''example to call Application class'''

    root = tk.Tk()

    root.geometry('400x200')
    root.title('tkinter template')

    app = Application(master=root)

    app.mainloop()


if __name__ == "__main__":
    main()
