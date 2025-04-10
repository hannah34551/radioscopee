
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Radio Telescope Simulator", layout="wide")
st.title("🔭 Radio Telescope Receiver System")

# Sidebar stage selector
stage = st.sidebar.radio("Choose a system stage:", [
    "Antenna",
    "Receiver",
    "ADC",
    "FFT",
    "Spectrum Output"
])

# Global simulation parameters
frequency = st.sidebar.slider("Signal Frequency (MHz)", 1400.0, 1440.0, 1420.0, 0.5)
noise_level = st.sidebar.slider("Noise Level", 0.0, 2.0, 0.5, 0.1)
sample_rate = st.sidebar.slider("Sample Rate (Hz)", 1000, 50000, 10000, 1000)
duration_ms = st.sidebar.slider("Duration (ms)", 1, 100, 10, 1)

# Derived values
frequency_hz = frequency * 1e6
duration = duration_ms / 1000.0
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
signal = np.sin(2 * np.pi * frequency_hz * t)
noise = np.random.normal(0, noise_level, len(t))

if stage == "Antenna":
    st.header("Stage 1: Antenna")
    st.markdown("The antenna collects incoming cosmic radio waves and produces a raw analog signal.")
    fig, ax = plt.subplots()
    ax.plot(t * 1e3, signal)
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Amplitude")
    ax.set_title("Raw Signal from Antenna")
    st.pyplot(fig)

elif stage == "Receiver":
    st.header("Stage 2: Receiver")
    st.markdown("The receiver amplifies the signal and introduces some analog filtering. For simplicity, we apply gain here.")
    gain = 5
    amplified_signal = gain * signal
    fig, ax = plt.subplots()
    ax.plot(t * 1e3, amplified_signal)
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Amplitude")
    ax.set_title("Amplified Signal")
    st.pyplot(fig)

elif stage == "ADC":
    st.header("Stage 3: Analog-to-Digital Converter (ADC)")
    st.markdown("The ADC digitizes the signal and includes noise. This is the actual signal processed by the backend.")
    received_signal = signal + noise
    fig, ax = plt.subplots()
    ax.plot(t * 1e3, received_signal)
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Amplitude")
    ax.set_title("Digitized Signal with Noise")
    st.pyplot(fig)

elif stage == "FFT":
    st.header("Stage 4: Fast Fourier Transform (FFT)")
    st.markdown("FFT converts the signal from the time domain to the frequency domain.")
    received_signal = signal + noise
    fft_result = np.fft.fft(received_signal)
    fft_freqs = np.fft.fftfreq(len(t), 1/sample_rate)
    spectrum = np.abs(fft_result)
    pos_mask = fft_freqs >= 0
    fft_freqs = fft_freqs[pos_mask] / 1e6  # Convert to MHz
    spectrum = spectrum[pos_mask]
    fig, ax = plt.subplots()
    ax.plot(fft_freqs, spectrum)
    ax.set_xlabel("Frequency (MHz)")
    ax.set_ylabel("Magnitude")
    ax.set_title("FFT Result")
    st.pyplot(fig)

elif stage == "Spectrum Output":
    st.header("Stage 5: Spectrum Output")
    st.markdown("This is the final spectrum, which scientists use to identify radio sources.")
    received_signal = signal + noise
    fft_result = np.fft.fft(received_signal)
    fft_freqs = np.fft.fftfreq(len(t), 1/sample_rate)
    spectrum = np.abs(fft_result)
    pos_mask = fft_freqs >= 0
    fft_freqs = fft_freqs[pos_mask] / 1e6
    spectrum = spectrum[pos_mask]
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(fft_freqs, spectrum)
    ax.set_xlabel("Frequency (MHz)")
    ax.set_ylabel("Intensity")
    ax.set_title("Final Radio Spectrum")
    st.pyplot(fig)
    st.success("Spectrum captured successfully.")
