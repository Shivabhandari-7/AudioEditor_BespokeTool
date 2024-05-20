import sys
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtCore import QTimer  # Import QTimer
from ui import AudioEditorUI
from editor import AudioEditor
from utils import plot_waveform  # Ensure this import is included

class AudioEditorApp(AudioEditorUI):
    def __init__(self):
        super().__init__()
        self.audio_editor = AudioEditor()
        self.key_point_added.connect(self.add_key_point_to_editor)
        self.playhead_timer = QTimer(self)
        self.playhead_timer.timeout.connect(self.update_playhead)

    def open_file(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.wav *.mp3 *.flac)")
            if file_path:
                self.audio_editor.load_audio(file_path)
                self.plot_waveform()
                self.update_mix_selects(file_path)
        except Exception as e:
            self.show_error_message(str(e))

    def play_audio(self):
        try:
            self.audio_editor.play()
            self.playhead_timer.start(100)  # Update every 100ms
        except Exception as e:
            self.show_error_message(str(e))

    def pause_audio(self):
        try:
            self.audio_editor.pause()
            self.playhead_timer.stop()
        except Exception as e:
            self.show_error_message(str(e))

    def stop_audio(self):
        try:
            self.audio_editor.stop()
            self.playhead_timer.stop()
            self.plot_waveform()  # Reset waveform visualization
        except Exception as e:
            self.show_error_message(str(e))

    def adjust_volume(self):
        try:
            change_db = self.volume_slider.value()
            self.audio_editor.adjust_volume(change_db)
            self.plot_waveform()
        except Exception as e:
            self.show_error_message(str(e))

    def trim_audio(self):
        try:
            start_time = int(self.start_time_input.text())
            end_time = int(self.end_time_input.text())
            self.audio_editor.trim(start_time, end_time)
            self.plot_waveform()
        except ValueError as e:
            self.show_error_message(str(e))

    def fade_in(self):
        try:
            self.audio_editor.fade_in(2000)
            self.plot_waveform()
        except Exception as e:
            self.show_error_message(str(e))

    def fade_out(self):
        try:
            self.audio_editor.fade_out(2000)
            self.plot_waveform()
        except Exception as e:
            self.show_error_message(str(e))

    def add_echo(self):
        try:
            self.audio_editor.add_echo(500)
            self.plot_waveform()
        except Exception as e:
            self.show_error_message(str(e))

    def add_reverb(self):
        try:
            self.audio_editor.add_reverb(70)
            self.plot_waveform()
        except Exception as e:
            self.show_error_message(str(e))

    def pitch_up(self):
        try:
            self.audio_editor.pitch_up(1)
            self.plot_waveform()
        except Exception as e:
            self.show_error_message(str(e))

    def pitch_down(self):
        try:
            self.audio_editor.pitch_down(1)
            self.plot_waveform()
        except Exception as e:
            self.show_error_message(str(e))

    def export_audio(self):
        try:
            file_path, _ = QFileDialog.getSaveFileName(self, "Save Audio File", "", "Audio Files (*.wav *.mp3 *.flac)")
            if file_path:
                self.audio_editor.save_audio(file_path)
        except Exception as e:
            self.show_error_message(str(e))

    def export_custom_audio(self):
        try:
            freq = float(self.custom_freq_input.text())
            duration = int(self.custom_duration_input.text())
            volume = int(self.custom_volume_input.text())
            file_path, _ = QFileDialog.getSaveFileName(self, "Save Custom Audio File", "", "Audio Files (*.wav)")
            if file_path:
                self.audio_editor.export_custom_audio(file_path, freq, duration, volume)
        except ValueError as e:
            self.show_error_message(str(e))
        except Exception as e:
            self.show_error_message(str(e))

    def undo(self):
        try:
            self.audio_editor.undo()
            self.plot_waveform()
        except Exception as e:
            self.show_error_message(str(e))

    def redo(self):
        try:
            self.audio_editor.redo()
            self.plot_waveform()
        except Exception as e:
            self.show_error_message(str(e))

    def plot_waveform(self):
        try:
            plot_waveform(self.plot_widget, self.audio_editor.audio_data, self.key_points)
            self.playhead_line.setPos(self.audio_editor.playhead_position)
        except Exception as e:
            self.show_error_message(str(e))

    def generate_coin_sound(self):
        try:
            self.audio_editor.generate_coin_sound()
            self.plot_waveform()
        except Exception as e:
            self.show_error_message(str(e))

    def generate_gunshot_sound(self):
        try:
            self.audio_editor.generate_gunshot_sound()
            self.plot_waveform()
        except Exception as e:
            self.show_error_message(str(e))

    def generate_steps_sound(self):
        try:
            self.audio_editor.generate_steps_sound()
            self.plot_waveform()
        except Exception as e:
            self.show_error_message(str(e))

    def generate_random_audio(self):
        try:
            self.audio_editor.generate_random_audio()
            self.plot_waveform()
        except Exception as e:
            self.show_error_message(str(e))

    def update_mix_selects(self, file_path):
        try:
            self.mix_select1.addItem(file_path)
            self.mix_select2.addItem(file_path)
        except Exception as e:
            self.show_error_message(str(e))

    def mix_audio(self):
        try:
            file_path1 = self.mix_select1.currentText()
            file_path2 = self.mix_select2.currentText()
            self.audio_editor.mix_audio(file_path1, file_path2)
            self.plot_waveform()
        except Exception as e:
            self.show_error_message(str(e))

    def add_audio_file(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, "Add Audio File", "", "Audio Files (*.wav *.mp3 *.flac)")
            if file_path:
                self.audio_editor.add_audio_file(file_path)
                self.update_mix_selects(file_path)
        except Exception as e:
            self.show_error_message(str(e))

    def apply_noise_reduction(self):
        try:
            self.audio_editor.noise_reduction()
            self.plot_waveform()
        except Exception as e:
            self.show_error_message(str(e))

    def apply_compression(self):
        try:
            self.audio_editor.apply_compression()
            self.plot_waveform()
        except Exception as e:
            self.show_error_message(str(e))

    def add_key_point_to_editor(self, key_point):
        self.audio_editor.key_points.append(key_point)
        self.plot_waveform()

    def update_playhead(self):
        self.playhead_line.setPos(self.audio_editor.playhead_position)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioEditorApp()
    window.show()
    sys.exit(app.exec_())
