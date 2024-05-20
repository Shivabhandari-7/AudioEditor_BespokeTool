import pyqtgraph as pg

def plot_waveform(plot_widget, audio_data, key_points):
    plot_widget.clear()
    plot_widget.plot(audio_data, pen='w')
    for point in key_points:
        plot_widget.addItem(pg.InfiniteLine(pos=point, angle=90, pen='r'))
