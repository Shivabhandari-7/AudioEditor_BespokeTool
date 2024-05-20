import numpy as np
from scipy.io.wavfile import write
import simpleaudio as sa
from pydub import AudioSegment
import random
from scipy.signal import butter, lfilter
import traceback
import pyqtgraph as pg  # Import pyqtgraph

class AudioEditor:
    def __init__(self):
        self.audio = None
        self.history = []
        self.redo_stack = []
        self.play_obj = None
        self.is_paused = False
        self.play_data = None
        self.audio_files = {}
        self.current_audio_file = None
        self.volume_level = 0
        self.key_points = []
        self.effects = []
        self.playhead_position = 0

    def load_audio(self, file_path):
        try:
            self.audio = AudioSegment.from_file(file_path)
            self.current_audio_file = file_path
            self.history.append(self.audio)
            self.audio_files[file_path] = self.audio
            self.audio_data = np.array(self.audio.get_array_of_samples())
        except Exception as e:
            self.log_error(e)

    def save_audio(self, file_path):
        try:
            if self.audio:
                self.audio.export(file_path, format="wav")
        except Exception as e:
            self.log_error(e)

    def trim(self, start_ms, end_ms):
        try:
            self.audio = self.audio[start_ms:end_ms]
            self.history.append(self.audio)
            self.audio_data = np.array(self.audio.get_array_of_samples())
        except Exception as e:
            self.log_error(e)

    def fade_in(self, duration_ms):
        try:
            self.audio = self.audio.fade_in(duration_ms)
            self.history.append(self.audio)
            self.effects.append(('fade_in', 0, duration_ms))
            self.audio_data = np.array(self.audio.get_array_of_samples())
        except Exception as e:
            self.log_error(e)

    def fade_out(self, duration_ms):
        try:
            self.audio = self.audio.fade_out(duration_ms)
            self.history.append(self.audio)
            self.effects.append(('fade_out', len(self.audio) - duration_ms, len(self.audio)))
            self.audio_data = np.array(self.audio.get_array_of_samples())
        except Exception as e:
            self.log_error(e)

    def adjust_volume(self, change_db):
        try:
            self.audio = self.audio + change_db
            self.history.append(self.audio)
            self.volume_level = change_db
            self.audio_data = np.array(self.audio.get_array_of_samples())
        except Exception as e:
            self.log_error(e)

    def add_echo(self, delay_ms):
        try:
            self.audio = self._apply_echo(self.audio, delay_ms)
            self.history.append(self.audio)
            self.effects.append(('echo', delay_ms))
            self.audio_data = np.array(self.audio.get_array_of_samples())
        except Exception as e:
            self.log_error(e)

    def add_reverb(self, reverberance=50):
        try:
            self.audio = self._apply_reverb(self.audio, reverberance)
            self.history.append(self.audio)
            self.effects.append(('reverb', reverberance))
            self.audio_data = np.array(self.audio.get_array_of_samples())
        except Exception as e:
            self.log_error(e)

    def pitch_up(self, semitones):
        try:
            self.audio = self.audio._spawn(self.audio.raw_data, overrides={"frame_rate": int(self.audio.frame_rate * (2.0 ** (semitones / 12.0)))})
            self.audio = self.audio.set_frame_rate(44100)
            self.history.append(self.audio)
            self.audio_data = np.array(self.audio.get_array_of_samples())
        except Exception as e:
            self.log_error(e)

    def pitch_down(self, semitones):
        try:
            self.audio = self.audio._spawn(self.audio.raw_data, overrides={"frame_rate": int(self.audio.frame_rate / (2.0 ** (semitones / 12.0)))})
            self.audio = self.audio.set_frame_rate(44100)
            self.history.append(self.audio)
            self.audio_data = np.array(self.audio.get_array_of_samples())
        except Exception as e:
            self.log_error(e)

    def undo(self):
        try:
            if len(self.history) > 1:
                self.redo_stack.append(self.history.pop())
                self.audio = self.history[-1]
                self.audio_data = np.array(self.audio.get_array_of_samples())
        except Exception as e:
            self.log_error(e)

    def redo(self):
        try:
            if self.redo_stack:
                self.audio = self.redo_stack.pop()
                self.history.append(self.audio)
                self.audio_data = np.array(self.audio.get_array_of_samples())
        except Exception as e:
            self.log_error(e)

    def play(self):
        try:
            if self.audio:
                if self.is_paused and self.play_data:
                    self.play_obj = sa.play_buffer(self.play_data, num_channels=2, bytes_per_sample=self.audio.sample_width, sample_rate=self.audio.frame_rate)
                    self.is_paused = False
                else:
                    self.play_data = self.audio.raw_data
                    self.play_obj = sa.play_buffer(self.play_data, num_channels=2, bytes_per_sample=self.audio.sample_width, sample_rate=self.audio.frame_rate)
                self.update_playhead()
        except Exception as e:
            self.log_error(e)

    def pause(self):
        try:
            if self.play_obj:
                if self.is_paused:
                    self.play()
                else:
                    self.play_obj.stop()
                    self.is_paused = True
        except Exception as e:
            self.log_error(e)

    def stop(self):
        try:
            if self.play_obj:
                self.play_obj.stop()
                self.is_paused = False
                self.play_obj = None
                self.playhead_position = 0
        except Exception as e:
            self.log_error(e)

    def generate_coin_sound(self):
        try:
            self._generate_sound(880, 100)
            self.play_generated_audio()
        except Exception as e:
            self.log_error(e)

    def generate_gunshot_sound(self):
        try:
            self._generate_sound(400, 300, wave_type='noise')
            self.play_generated_audio()
        except Exception as e:
            self.log_error(e)

    def generate_steps_sound(self):
        try:
            self._generate_sound(220, 200)
            self.play_generated_audio()
        except Exception as e:
            self.log_error(e)

    def generate_random_audio(self):
        try:
            wave_type = random.choice(['sine', 'square', 'noise'])
            self._generate_sound(random.uniform(100, 1000), random.uniform(100, 1000), wave_type=wave_type)
            self.play_generated_audio()
        except Exception as e:
            self.log_error(e)

    def play_generated_audio(self):
        try:
            play_data = self.audio.raw_data
            self.play_obj = sa.play_buffer(play_data, num_channels=2, bytes_per_sample=self.audio.sample_width, sample_rate=self.audio.frame_rate)
        except Exception as e:
            self.log_error(e)

    def mix_audio(self, file_path1, file_path2):
        try:
            if file_path1 in self.audio_files and file_path2 in self.audio_files:
                mixed_audio = self.audio_files[file_path1].overlay(self.audio_files[file_path2])
                self.audio = mixed_audio
                self.history.append(self.audio)
                self.audio_data = np.array(self.audio.get_array_of_samples())
                self.play_generated_audio()
        except Exception as e:
            self.log_error(e)

    def add_audio_file(self, file_path):
        try:
            audio = AudioSegment.from_file(file_path)
            self.audio_files[file_path] = audio
        except Exception as e:
            self.log_error(e)

    def export_custom_audio(self, file_path, freq, duration, volume):
        try:
            self._generate_sound(freq, duration, volume)
            self.audio.export(file_path, format="wav")
        except Exception as e:
            self.log_error(e)

    def _generate_sound(self, freq, duration, volume=50, wave_type='sine'):
        try:
            sample_rate = 44100
            t = np.linspace(0, duration / 1000, int(sample_rate * (duration / 1000)), endpoint=False)
            if wave_type == 'sine':
                wave = 0.5 * np.sin(2 * np.pi * freq * t)
            elif wave_type == 'square':
                wave = 0.5 * np.sign(np.sin(2 * np.pi * freq * t))
            elif wave_type == 'noise':
                wave = 0.5 * np.random.uniform(-1, 1, size=t.shape)

            wave = (wave * 32767 * (volume / 100)).astype(np.int16)
            write("generated_sound.wav", sample_rate, wave)
            self.audio = AudioSegment.from_wav("generated_sound.wav")
            self.history.append(self.audio)
            self.audio_data = np.array(self.audio.get_array_of_samples())
        except Exception as e:
            self.log_error(e)

    def _apply_echo(self, audio_segment, delay_ms):
        try:
            echo_segment = audio_segment.overlay(audio_segment, delay_ms)
            combined = audio_segment + echo_segment
            return combined
        except Exception as e:
            self.log_error(e)

    def _apply_reverb(self, audio_segment, reverberance):
        try:
            delay = int(reverberance / 10) * 50
            decay = reverberance / 100
            reverb_segment = audio_segment
            for i in range(1, 5):
                reverb_segment = reverb_segment.overlay(audio_segment - i * decay, delay * i)
            combined = audio_segment + reverb_segment
            return combined
        except Exception as e:
            self.log_error(e)

    def noise_reduction(self):
        try:
            self.audio = self._reduce_noise(self.audio)
            self.history.append(self.audio)
            self.audio_data = np.array(self.audio.get_array_of_samples())
        except Exception as e:
            self.log_error(e)

    def _reduce_noise(self, audio_segment):
        try:
            noise_sample = audio_segment[:1000]  # Taking the first 1000ms as noise sample
            reduced_noise_audio = audio_segment - noise_sample
            return reduced_noise_audio
        except Exception as e:
            self.log_error(e)

    def apply_compression(self, threshold=-20.0, ratio=4.0):
        try:
            self.audio = self._compress_audio(self.audio, threshold, ratio)
            self.history.append(self.audio)
            self.audio_data = np.array(self.audio.get_array_of_samples())
        except Exception as e:
            self.log_error(e)

    def _compress_audio(self, audio_segment, threshold, ratio):
        try:
            compressed_audio = audio_segment.compress_dynamic_range(threshold=threshold, ratio=ratio)
            return compressed_audio
        except Exception as e:
            self.log_error(e)

    def update_playhead(self):
        try:
            if self.play_obj:
                self.playhead_position = 0
                sample_rate = self.audio.frame_rate
                duration_ms = len(self.audio)
                self.playhead_timer = pg.QtCore.QTimer()
                self.playhead_timer.timeout.connect(lambda: self.move_playhead(sample_rate, duration_ms))
                self.playhead_timer.start(100)  # Update every 100ms
        except Exception as e:
            self.log_error(e)

    def move_playhead(self, sample_rate, duration_ms):
        if self.play_obj.is_playing():
            self.playhead_position += 1000 * (100 / sample_rate)
            if self.playhead_position >= duration_ms:
                self.playhead_timer.stop()

    def log_error(self, e):
        print(f"Error: {str(e)}")
        traceback.print_exc()
