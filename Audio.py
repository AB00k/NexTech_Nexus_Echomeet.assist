import sounddevice as sd
import numpy as np
import wave
import os

# Get the current directory of your script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Navigate up one directory to the parent directory
parent_directory = os.path.dirname(script_directory)

# Navigate up one Directory again to reach recording Directory
rec_directory= os.path.dirname(parent_directory)

# Construct the path to the voice file in the parent directory
rec_path = os.path.join(rec_directory, "recording.wav")


class AudioRecorder:
    def __init__(self):
        self.recording = False
        self.audio_data = []

    def start_recording(self):
        if not self.recording:
            self.recording = True
            self.audio_data = []

            def callback(indata, frames, time, status):
                if status:
                    print("Error:", status)
                self.audio_data.append(indata.copy())

            with sd.InputStream(callback=callback, samplerate=22000):
                print("Recording started. Press Enter to stop recording...")
                input()

            self.recording = False
            self.stop_recording("recording.wav")

    def stop_recording(self, output_file):
        if self.recording:
            print("Recording is still in progress. Please stop recording first.")
            return

        if not self.audio_data:
            print("No audio recorded.")
            return

        audio_data = np.concatenate(self.audio_data, axis=0)
        audio_data = (audio_data * (2 ** 15 - 1)).astype(np.int16)

        wf = wave.open(output_file, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 2 bytes per sample (16-bit audio)
        wf.setframerate(44100) #Setting the Sampling rate
        wf.writeframes(audio_data.tobytes())
        wf.close()

        print(f"Audio saved to '{output_file}'.")