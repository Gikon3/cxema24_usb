import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Gui(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("Cxema-24")

        signal_frame = QGroupBox()

        radio_gps = QRadioButton("GPS")
        radio_glo = QRadioButton("Глонасс")
        radio_gps.setChecked(True)
        radio_group = QButtonGroup()
        radio_group.addButton(radio_gps)
        radio_group.addButton(radio_glo)

        signal_layout = QHBoxLayout()
        signal_layout.addStretch(1)
        signal_layout.addWidget(radio_gps)
        signal_layout.addWidget(radio_glo)

        signal_frame.set

        # mode_frame = QVBoxLayout()
        # mode_frame.addStretch(1)
        # mode_frame.addWidget(QLabel("Сигнал"))
        # mode_frame.addLayout(mode_button_frame)

        # frame1.setLayout(mode_frame)

        self.setLayout(signal_frame)
        # self.setLayout(frame1)
        self.show()

    # def _onRadioButtonClicked(self, button):
    #     self.label.setText('Current: ' + button.text())
