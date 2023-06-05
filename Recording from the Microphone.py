import pyaudio
import wave

def test_microphone():
    chunk = 1024  # Buffer size
    format = pyaudio.paInt16  # Audio format
    channels = 1  # Number of channels
    sample_rate = 44100  # Sample rate (Hz)
    duration = 5  # Duration of recording (seconds)
    record_frames = []  # List to store audio frames

    try:
        # Initialize PyAudio
        audio = pyaudio.PyAudio()

        # Open microphone stream
        stream = audio.open(format=format,
                            channels=channels,
                            rate=sample_rate,
                            input=True,
                            frames_per_buffer=chunk)

        print("Recording audio...")
        for _ in range(0, int(sample_rate / chunk * duration)):
            # Read audio data from the microphone
            data = stream.read(chunk)
            record_frames.append(data)

        print("Recording complete")

        # Stop the microphone stream
        stream.stop_stream()
        stream.close()

        # Terminate PyAudio
        audio.terminate()

        # Save the recorded audio to a WAV file
        with wave.open("recorded_audio.wav", "wb") as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(audio.get_sample_size(format))
            wf.setframerate(sample_rate)
            wf.writeframes(b"".join(record_frames))

        print("Audio saved to recorded_audio.wav")

    except OSError:
        print("Error: Failed to access the microphone.")

# Example usage
test_microphone()
