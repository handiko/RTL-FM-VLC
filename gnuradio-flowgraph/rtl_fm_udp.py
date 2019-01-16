#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: RTL FM UDP - Handiko Gesang
# Generated: Wed Jan 16 07:41:44 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import osmosdr
import sip
import sys
import time


class rtl_fm_udp(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "RTL FM UDP - Handiko Gesang")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("RTL FM UDP - Handiko Gesang")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
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

        self.settings = Qt.QSettings("GNU Radio", "rtl_fm_udp")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.volume = volume = 0.0
        self.samp_rate = samp_rate = 2.88e6
        self.rfgain = rfgain = 10.0
        self.freq = freq = 104.6

        ##################################################
        # Blocks
        ##################################################
        self._volume_range = Range(-30.0, 20.0, 1.0, 0.0, 200)
        self._volume_win = RangeWidget(self._volume_range, self.set_volume, 'Volume (dB)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._volume_win, 2,1,1,1)
        self._rfgain_range = Range(0.0, 49.0, 0.1, 10.0, 200)
        self._rfgain_win = RangeWidget(self._rfgain_range, self.set_rfgain, 'RF Gain (dB)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rfgain_win, 2,0,1,1)
        self._freq_range = Range(88.0, 108.8, 0.1, 104.6, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, 'Freq', "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_win, 1,0,1,2)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=int(192e3),
                decimation=int(samp_rate),
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq*1e6, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-120, -20)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,2)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(freq*1e6, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(rfgain, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.fft_filter_xxx_0 = filter.fft_filter_fff(1, (firdes.low_pass(0.1*(pow(10.0,volume/10.0)),48e3,10e3,5e3,firdes.WIN_BLACKMAN)), 1)
        self.fft_filter_xxx_0.declare_sample_delay(0)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_short*1, 'localhost', 7355, 1472, True)
        self.blocks_float_to_short_0 = blocks.float_to_short(1, 500)
        self.blocks_endian_swap_0 = blocks.endian_swap(2)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=192e3,
        	audio_decimation=4,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.fft_filter_xxx_0, 0))    
        self.connect((self.blocks_endian_swap_0, 0), (self.blocks_udp_sink_0, 0))    
        self.connect((self.blocks_float_to_short_0, 0), (self.blocks_endian_swap_0, 0))    
        self.connect((self.fft_filter_xxx_0, 0), (self.blocks_float_to_short_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_wfm_rcv_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "rtl_fm_udp")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.fft_filter_xxx_0.set_taps((firdes.low_pass(0.1*(pow(10.0,self.volume/10.0)),48e3,10e3,5e3,firdes.WIN_BLACKMAN)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(self.freq*1e6, self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)

    def get_rfgain(self):
        return self.rfgain

    def set_rfgain(self, rfgain):
        self.rfgain = rfgain
        self.osmosdr_source_0.set_gain(self.rfgain, 0)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.qtgui_freq_sink_x_0.set_frequency_range(self.freq*1e6, self.samp_rate)
        self.osmosdr_source_0.set_center_freq(self.freq*1e6, 0)


def main(top_block_cls=rtl_fm_udp, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
