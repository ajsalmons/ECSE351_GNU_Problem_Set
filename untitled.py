#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Phase Lab
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import blocks
import math
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip
import threading



class untitled(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Phase Lab", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Phase Lab")
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
        self.samp_rate = samp_rate = 1000
        self.p_y2 = p_y2 = 90
        self.p_y1 = p_y1 = 0
        self.f_y2 = f_y2 = 0.5
        self.f_y1 = f_y1 = 0.5
        self.dc_y2 = dc_y2 = 0
        self.dc_y1 = dc_y1 = 0
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
        	scaleFactor = 5

        _p_y2_dial_control = qtgui.GrDialControl('Phase (Y2)', self, 0,72,90,"purple",self.set_p_y2,isFloat, scaleFactor, 100, True, "'value'")
        self.p_y2 = _p_y2_dial_control

        self.top_grid_layout.addWidget(_p_y2_dial_control, 9, 15, 2, 2)
        for r in range(9, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(15, 17):
            self.top_grid_layout.setColumnStretch(c, 1)
        if "real" == "int":
        	isFloat = False
        	scaleFactor = 1
        else:
        	isFloat = True
        	scaleFactor = 5

        _p_y1_dial_control = qtgui.GrDialControl('Phase (Y1)', self, 0,72,0,"aqua",self.set_p_y1,isFloat, scaleFactor, 100, True, "'value'")
        self.p_y1 = _p_y1_dial_control

        self.top_grid_layout.addWidget(_p_y1_dial_control, 9, 4, 2, 2)
        for r in range(9, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        if "real" == "int":
        	isFloat = False
        	scaleFactor = 1
        else:
        	isFloat = True
        	scaleFactor = 0.1

        _f_y2_dial_control = qtgui.GrDialControl('Frequency (Y2)', self, 1,40,0.5,"purple",self.set_f_y2,isFloat, scaleFactor, 100, True, "'value'")
        self.f_y2 = _f_y2_dial_control

        self.top_grid_layout.addWidget(_f_y2_dial_control, 9, 13, 2, 2)
        for r in range(9, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(13, 15):
            self.top_grid_layout.setColumnStretch(c, 1)
        if "real" == "int":
        	isFloat = False
        	scaleFactor = 1
        else:
        	isFloat = True
        	scaleFactor = 0.1

        _f_y1_dial_control = qtgui.GrDialControl('Frequency (Y1)', self, 1,40,0.5,"aqua",self.set_f_y1,isFloat, scaleFactor, 100, True, "'value'")
        self.f_y1 = _f_y1_dial_control

        self.top_grid_layout.addWidget(_f_y1_dial_control, 9, 2, 2, 2)
        for r in range(9, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        if "real" == "int":
        	isFloat = False
        	scaleFactor = 1
        else:
        	isFloat = True
        	scaleFactor = 0.02

        _dc_y2_dial_control = qtgui.GrDialControl('Offset (Y1)', self, (-50),50,0,"purple",self.set_dc_y2,isFloat, scaleFactor, 100, True, "'value'")
        self.dc_y2 = _dc_y2_dial_control

        self.top_grid_layout.addWidget(_dc_y2_dial_control, 9, 17, 2, 2)
        for r in range(9, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(17, 19):
            self.top_grid_layout.setColumnStretch(c, 1)
        if "real" == "int":
        	isFloat = False
        	scaleFactor = 1
        else:
        	isFloat = True
        	scaleFactor = 0.02

        _dc_y1_dial_control = qtgui.GrDialControl('Offset (Y1)', self, (-50),50,0,"aqua",self.set_dc_y1,isFloat, scaleFactor, 100, True, "'value'")
        self.dc_y1 = _dc_y1_dial_control

        self.top_grid_layout.addWidget(_dc_y1_dial_control, 9, 6, 2, 2)
        for r in range(9, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        if "real" == "int":
        	isFloat = False
        	scaleFactor = 1
        else:
        	isFloat = True
        	scaleFactor = 0.01

        _a_y2_dial_control = qtgui.GrDialControl('Amplitude (Y2)', self, 0,100,1,"purple",self.set_a_y2,isFloat, scaleFactor, 100, True, "'value'")
        self.a_y2 = _a_y2_dial_control

        self.top_grid_layout.addWidget(_a_y2_dial_control, 9, 11, 2, 2)
        for r in range(9, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(11, 13):
            self.top_grid_layout.setColumnStretch(c, 1)
        if "real" == "int":
        	isFloat = False
        	scaleFactor = 1
        else:
        	isFloat = True
        	scaleFactor = 0.01

        _a_y1_dial_control = qtgui.GrDialControl('Amplitude (Y1)', self, 0,100,1,"aqua",self.set_a_y1,isFloat, scaleFactor, 100, True, "'value'")
        self.a_y1 = _a_y1_dial_control

        self.top_grid_layout.addWidget(_a_y1_dial_control, 9, 0, 2, 2)
        for r in range(9, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            (round(samp_rate*4)), #size
            samp_rate, #samp_rate
            'Time Series', #name
            3, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(False)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Y1', 'Y2', 'Y1×Y2', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [3, 3, 3, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['cyan', 'magenta', 'black', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 3, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 0, 0, 8, 12)
        for r in range(0, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 12):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            (samp_rate*10), #size
            'XY Plot', #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.05)
        self.qtgui_const_sink_x_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(True)
        self.qtgui_const_sink_x_0.enable_axis_labels(False)

        self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 0, 12, 8, 7)
        for r in range(0, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(12, 19):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 1)
        self.blocks_phase_shift_0_0 = blocks.phase_shift(p_y2, False)
        self.blocks_phase_shift_0 = blocks.phase_shift(p_y1, False)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(a_y1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(a_y2)
        self.blocks_freqshift_cc_0_0 = blocks.rotator_cc(2.0*math.pi*(f_y2 - 1)/samp_rate)
        self.blocks_freqshift_cc_0 = blocks.rotator_cc(2.0*math.pi*(f_y1 - 1)/samp_rate)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_1_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_1 = blocks.complex_to_float(1)
        self.blocks_add_const_vxx_1_0 = blocks.add_const_ff(dc_y2)
        self.blocks_add_const_vxx_1 = blocks.add_const_ff(dc_y1)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 1, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_freqshift_cc_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_freqshift_cc_0_0, 0))
        self.connect((self.blocks_add_const_vxx_1, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_add_const_vxx_1, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_add_const_vxx_1, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_add_const_vxx_1_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_add_const_vxx_1_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_add_const_vxx_1_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_complex_to_float_1, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_complex_to_float_1_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_freqshift_cc_0, 0), (self.blocks_phase_shift_0, 0))
        self.connect((self.blocks_freqshift_cc_0_0, 0), (self.blocks_phase_shift_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_const_vxx_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_phase_shift_0, 0), (self.blocks_complex_to_float_1, 0))
        self.connect((self.blocks_phase_shift_0_0, 0), (self.blocks_complex_to_float_1_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.qtgui_const_sink_x_0, 0))


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
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.blocks_freqshift_cc_0.set_phase_inc(2.0*math.pi*(self.f_y1 - 1)/self.samp_rate)
        self.blocks_freqshift_cc_0_0.set_phase_inc(2.0*math.pi*(self.f_y2 - 1)/self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_p_y2(self):
        return self.p_y2

    def set_p_y2(self, p_y2):
        self.p_y2 = p_y2
        self.blocks_phase_shift_0_0.set_shift(self.p_y2)

    def get_p_y1(self):
        return self.p_y1

    def set_p_y1(self, p_y1):
        self.p_y1 = p_y1
        self.blocks_phase_shift_0.set_shift(self.p_y1)

    def get_f_y2(self):
        return self.f_y2

    def set_f_y2(self, f_y2):
        self.f_y2 = f_y2
        self.blocks_freqshift_cc_0_0.set_phase_inc(2.0*math.pi*(self.f_y2 - 1)/self.samp_rate)

    def get_f_y1(self):
        return self.f_y1

    def set_f_y1(self, f_y1):
        self.f_y1 = f_y1
        self.blocks_freqshift_cc_0.set_phase_inc(2.0*math.pi*(self.f_y1 - 1)/self.samp_rate)

    def get_dc_y2(self):
        return self.dc_y2

    def set_dc_y2(self, dc_y2):
        self.dc_y2 = dc_y2
        self.blocks_add_const_vxx_1_0.set_k(self.dc_y2)

    def get_dc_y1(self):
        return self.dc_y1

    def set_dc_y1(self, dc_y1):
        self.dc_y1 = dc_y1
        self.blocks_add_const_vxx_1.set_k(self.dc_y1)

    def get_a_y2(self):
        return self.a_y2

    def set_a_y2(self, a_y2):
        self.a_y2 = a_y2
        self.blocks_multiply_const_vxx_0.set_k(self.a_y2)

    def get_a_y1(self):
        return self.a_y1

    def set_a_y1(self, a_y1):
        self.a_y1 = a_y1
        self.blocks_multiply_const_vxx_0_0.set_k(self.a_y1)




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
