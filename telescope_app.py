import streamlit as st
import graphviz as graphviz

st.set_page_config(page_title="ORT Receiver Flow", layout="wide")
st.title("🔧 ORT Receiver System – Interactive Flow Diagram")

st.markdown("Select a component from the flowchart below to view its function.")

# Define flowchart with Graphviz
diagram = graphviz.Digraph(format='png')

# Antenna Subsystem
diagram.node("Antenna", "Antenna\n(326.5 MHz)")
diagram.node("RF Amp", "RF Amp\nGain: 30 dB\nBW: 15 MHz")
diagram.node("Image Filter", "Image Rejection Filter")
diagram.node("Mixer", "Mixer")
diagram.node("IF Amp 27", "IF Amp\nGain: 27 dB\nBW: 15 MHz")

# LO system
diagram.node("LO Branch", "LO Branching\n296.5 MHz")
diagram.node("LO Shift", "LO Phase Shifter")

# Receiver subsystem
diagram.node("Cable", "300m Coax Cable")
diagram.node("PA1", "IF Amp\nGain: 30 dB")
diagram.node("Delay", "Delay Line")
diagram.node("PA2", "IF Amp\nGain: 30 dB")
diagram.node("Beamform", "Beam Forming Network")
diagram.node("PA3", "IF Amp\nGain: 70 dB\nBW: 4 MHz")
diagram.node("Correlator", "Correlator")
diagram.node("Power", "Total Power")
diagram.node("ADC", "To ADC")

# Flow connections
diagram.edges([("Antenna", "RF Amp"),
                ("RF Amp", "Image Filter"),
                ("Image Filter", "Mixer"),
                ("Mixer", "IF Amp 27"),
                ("IF Amp 27", "Cable"),
                ("Cable", "PA1"),
                ("PA1", "Delay"),
                ("Delay", "PA2"),
                ("PA2", "Beamform"),
                ("Beamform", "PA3"),
                ("PA3", "Correlator"),
                ("Correlator", "Power"),
                ("Power", "ADC")])

# LO branches
diagram.edge("LO Branch", "LO Shift")
diagram.edge("LO Shift", "Mixer")

# Display the diagram
st.graphviz_chart(diagram)

# Component selector
component = st.selectbox("🔍 Select a component to inspect:", [
    "Antenna",
    "RF Amp",
    "Image Rejection Filter",
    "Mixer",
    "IF Amp (27 dB)",
    "LO Branching",
    "LO Phase Shifter",
    "300m Coax Cable",
    "IF Amp (30 dB)",
    "Delay Line",
    "Beam Forming Network",
    "IF Amp (70 dB)",
    "Correlator",
    "Total Power",
    "To ADC"
])

# Info dictionary
info = {
    "Antenna": "Receives cosmic radio waves at 326.5 MHz, part of the antenna subsystem.",
    "RF Amp": "First amplification stage at RF, 30 dB gain with 15 MHz bandwidth.",
    "Image Rejection Filter": "Suppresses image frequencies before downconversion.",
    "Mixer": "Mixes incoming RF with LO to produce IF signal.",
    "IF Amp (27 dB)": "Intermediate frequency amplifier (27 dB gain).",
    "LO Branching": "Distributes 296.5 MHz LO signal to mixers.",
    "LO Phase Shifter": "Applies necessary phase shift before mixing.",
    "300m Coax Cable": "Long-distance transmission of IF signal to receiver room.",
    "IF Amp (30 dB)": "Post-cable IF amplification stage.",
    "Delay Line": "Applies calibrated delay for phase alignment across antennas.",
    "Beam Forming Network": "Combines multiple inputs to create directional sensitivity.",
    "IF Amp (70 dB)": "Final gain stage before backend, narrow 4 MHz bandwidth.",
    "Correlator": "Computes correlations between signals for interferometry.",
    "Total Power": "Monitors total power for calibration and signal quality.",
    "To ADC": "Signals passed to digitizers for digital backend processing."
}

# Display info
st.markdown(f"### 🧠 {component}")
st.write(info[component])
