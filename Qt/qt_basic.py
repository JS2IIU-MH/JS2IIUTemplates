""" Qt basic sample """

import sys

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtWidgets import QWidget


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # window size
        w_width = 200
        w_height = 300
        # window location
        x_pos = 10
        y_pos = 10

        self.setGeometry(x_pos, y_pos, w_width, w_height)
        self.setWindowTitle('Qt sample')

        self.generate_widgets()

    def generate_widgets(self):
        # Vertical Layout
        vertical_box_layout = QVBoxLayout()
        self.setLayout(vertical_box_layout)

        # Label
        label1 = QLabel('Qt Label', self)

        # Button
        button_text = 'Button'
        button = QPushButton(button_text, self)
        button.resize(50, 20)
        button.clicked.connect(self.command_button)

        # tkinterのpack/gridみたいなこと
        vertical_box_layout.addWidget(label1)
        vertical_box_layout.addWidget(button)

    def command_button(self):
        print('button clicked')


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
