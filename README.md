# AudioEditor_BespokeTool



### Overview

The Game Audio Editor and Mixer is a comprehensive tool designed for game developers to edit, mix, and generate audio files. It provides a user-friendly interface for trimming, applying effects, and visualizing audio waveforms. The tool supports multiple audio formats and offers advanced features like multi-track editing, effects chains, and sound banks for organizing game sounds.

### Features

- **Audio Editing**: Trim, fade in/out, pitch adjustment, volume adjustment.
- **Effects**: Echo, reverb, noise reduction, compression.
- **Playback Controls**: Play, pause, stop, with a visual playhead indicator.
- **Waveform Visualization**: Interactive waveform with markers for effects and key points.
- **Sound Generation**: Generate sounds for coins, gunshots, footsteps, and random audio.
- **Multi-Track Mixing**: Mix multiple audio tracks.
- **Undo/Redo History**: View and navigate through editing history.
- **Sound Banks**: Organize and manage sound effects by category.
- **Export Options**: Save audio in various formats (WAV, MP3, FLAC).

### Libraries Used

- **PyQt5**: GUI framework for the application.
- **PyQtGraph**: Interactive plotting and visualization.
- **pydub**: Audio processing.
- **simpleaudio**: Audio playback.
- **numpy**: Numerical operations.
- **scipy**: Signal processing.

### Installation Guide

#### Prerequisites

- **Python 3.6 or higher**: Ensure you have Python installed on your system.

#### Step-by-Step Installation

1. **Clone the Repository**
    ```sh
    git clone https://github.com/Shivabhandari-7/AudioEditor_BespokeTool.git
    ```

2. **Set Up Virtual Environment**
    ```sh
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install Required Libraries**
    ```sh
    pip install -r requirements.txt
    ```

    **or**
   

5. **Install Required Libraries**
    ```sh
    pip install pyqt5 pyqtgraph pydub simpleaudio numpy scipy
    ```

6. **Run the Application**
    ```sh
    python main.py
    ```

### How to Use the Tool

#### Opening and Editing Audio Files

1. **Open an Audio File**
    - Click the "Open Audio File" button.
    - Select an audio file from your file system (supported formats: WAV, MP3, FLAC).

2. **Visualize the Waveform**
    - The waveform of the loaded audio will be displayed in the main window.

3. **Play, Pause, Stop**
    - Use the "Play", "Pause", and "Stop" buttons to control audio playback.
    - A yellow playhead line indicates the current playback position.

4. **Adjust Volume**
    - Use the volume slider to increase or decrease the volume. The waveform updates to reflect the changes.

5. **Trim Audio**
    - Enter the start and end times in milliseconds in the input fields.
    - Click the "Trim Selected" button to trim the audio.

6. **Fade In/Out**
    - Click the "Fade In" button to apply a fade-in effect at the beginning of the audio.
    - Click the "Fade Out" button to apply a fade-out effect at the end of the audio.
    - Visual markers indicate where the effects are applied.

7. **Add Echo/Reverb**
    - Click the "Add Echo" button to apply an echo effect.
    - Click the "Add Reverb" button to apply a reverb effect.
    - Visual markers indicate where the effects are applied.

8. **Pitch Adjustment**
    - Click the "Pitch Up" button to increase the pitch.
    - Click the "Pitch Down" button to decrease the pitch.

9. **Export Audio**
    - Click the "Export Audio" button to save the edited audio file in various formats (WAV, MP3, FLAC).

10. **Generate Custom Audio**
    - Enter frequency, duration, and volume in the input fields.
    - Click the "Export Custom Audio" button to generate and save custom audio files.

#### Multi-Track Mixing

1. **Add Audio Files**
    - Click the "Add Audio File" button to upload additional audio files for mixing.

2. **Mix Audio Tracks**
    - Select two audio files from the dropdowns.
    - Click the "Mix Audio" button to mix them together.

#### Advanced Features

1. **Undo/Redo History**
    - Use the "Undo" and "Redo" buttons to navigate through your editing history.

2. **Noise Reduction**
    - Click the "Apply Noise Reduction" button to reduce background noise in the audio.

3. **Dynamic Range Compression**
    - Click the "Apply Compression" button to compress the dynamic range of the audio.

4. **Sound Banks**
    - Organize and manage sounds by categories such as footsteps, gunshots, and ambient sounds.
    - Generate predefined sounds like coin, gunshot, and steps.
    - Click the respective buttons to generate and play these sounds.

5. **Random Audio Generation**
    - Click the "Generate Random Audio" button to create and play a random audio effect.

### Contributing

We welcome contributions! Please read our [contributing guide](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- Thanks to the developers of PyQt5, PyQtGraph, pydub, simpleaudio, numpy, and scipy for their fantastic libraries that made this project possible.
