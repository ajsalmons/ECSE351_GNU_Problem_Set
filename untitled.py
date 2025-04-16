#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Baba Yaga's Hut
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import threading



class untitled(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Baba Yaga's Hut", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Baba Yaga's Hut")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "untitled")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.p_y2 = p_y2 = 0
        self.p_y1 = p_y1 = 0
        self.f_y2 = f_y2 = 0.5
        self.f_y1 = f_y1 = 0.5
        self.a_y2 = a_y2 = 1
        self.a_y1 = a_y1 = 1

        ##################################################
        # Blocks
        ##################################################

        if "real" == "int":
        	isFloat = False
        	scaleFactor = 1
        else:
        	isFloat = True
        	scaleFactor = 10

        _p_y2_dial_control = qtgui.GrDialControl('Phase (Y2)', self, 0,36,0,"purple",self.set_p_y2,isFloat, scaleFactor, 100, True, "'value'")
        self.p_y2 = _p_y2_dial_control

        self.top_grid_layout.addWidget(_p_y2_dial_control, 1, 5, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(5, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        if "real" == "int":
        	isFloat = False
        	scaleFactor = 1
        else:
        	isFloat = True
        	scaleFactor = 10

        _p_y1_dial_control = qtgui.GrDialControl('Phase (Y1)', self, 0,36,0,"orange",self.set_p_y1,isFloat, scaleFactor, 100, True, "'value'")
        self.p_y1 = _p_y1_dial_control

        self.top_grid_layout.addWidget(_p_y1_dial_control, 1, 2, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        if "real" == "int":
        	isFloat = False
        	scaleFactor = 1
        else:
        	isFloat = True
        	scaleFactor = 0.1

        _f_y2_dial_control = qtgui.GrDialControl('Frequency (Y2)', self, 0,40,0.5,"purple",self.set_f_y2,isFloat, scaleFactor, 100, True, "'value'")
        self.f_y2 = _f_y2_dial_control

        self.top_grid_layout.addWidget(_f_y2_dial_control, 1, 4, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        if "real" == "int":
        	isFloat = False
        	scaleFactor = 1
        else:
        	isFloat = True
        	scaleFactor = 0.1

        _f_y1_dial_control = qtgui.GrDialControl('Frequency (Y1)', self, 0,40,0.5,"orange",self.set_f_y1,isFloat, scaleFactor, 100, True, "'value'")
        self.f_y1 = _f_y1_dial_control

        self.top_grid_layout.addWidget(_f_y1_dial_control, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        if "real" == "int":
        	isFloat = False
        	scaleFactor = 1
        else:
        	isFloat = True
        	scaleFactor = 0.01

        _a_y2_dial_control = qtgui.GrDialControl('Amplitude (Y2)', self, 0,100,1,"purple",self.set_a_y2,isFloat, scaleFactor, 100, True, "'value'")
        self.a_y2 = _a_y2_dial_control

        self.top_grid_layout.addWidget(_a_y2_dial_control, 1, 3, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        if "real" == "int":
        	isFloat = False
        	scaleFactor = 1
        else:
        	isFloat = True
        	scaleFactor = 0.01

        _a_y1_dial_control = qtgui.GrDialControl('Amplitude (Y1)', self, 0,100,1,"orange",self.set_a_y1,isFloat, scaleFactor, 100, True, "'value'")
        self.a_y1 = _a_y1_dial_control

        self.top_grid_layout.addWidget(_a_y1_dial_control, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)



    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "untitled")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_p_y2(self):
        return self.p_y2

    def set_p_y2(self, p_y2):
        self.p_y2 = p_y2

    def get_p_y1(self):
        return self.p_y1

    def set_p_y1(self, p_y1):
        self.p_y1 = p_y1

    def get_f_y2(self):
        return self.f_y2

    def set_f_y2(self, f_y2):
        self.f_y2 = f_y2

    def get_f_y1(self):
        return self.f_y1

    def set_f_y1(self, f_y1):
        self.f_y1 = f_y1

    def get_a_y2(self):
        return self.a_y2

    def set_a_y2(self, a_y2):
        self.a_y2 = a_y2

    def get_a_y1(self):
        return self.a_y1

    def set_a_y1(self, a_y1):
        self.a_y1 = a_y1




def main(top_block_cls=untitled, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
