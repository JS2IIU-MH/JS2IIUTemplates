''' matplotlib graph on tkinter window sample '''

import tkinter as tk
# from tkinter import ttk
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Application(tk.Frame):
    ''' GUI Application '''
    def __init__(self, master) -> None:
        super().__init__(master)
        self.grid()

        frame1 = tk.Frame()
        self.gen_mpl_graph(frame1)
        frame1.grid()

        frame2 = tk.Frame()
        extbtn = tk.Button(frame2,
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
        frame2.grid()

    def gen_mpl_graph(self, master):
        ''' generate matplotlib graph on tk canvas '''
        # MatplotlibのFigureを作成
        fig = plt.figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)

        # 三角関数のデータを生成
        x = np.linspace(0, 2 * np.pi, 100)
        y = np.sin(x)

        # グラフをプロット
        ax.plot(x, y)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_title('trigonometric function')
        ax.grid()

        # MatplotlibのFigureをTkinterのCanvasに埋め込む
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def main():
    ''' main function generating window instance '''
    # tkinterウィンドウを作成
    root = tk.Tk()
    root.title("matplotlib on tkinter")
    root.geometry('650x500')
    root.grid_anchor(tk.CENTER)

    app = Application(master=root)

    # ウィンドウを表示
    app.mainloop()


if __name__ == '__main__':
    main()
