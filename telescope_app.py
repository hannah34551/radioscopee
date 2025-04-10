import streamlit as st
import graphviz

st.set_page_config(page_title="ORT Receiver System", layout="wide")
st.title("📡 ORT Receiver System – Clean Signal Flow Diagram")

st.markdown("This diagram shows the structured signal path of the ORT receiver system. Select a component to see its function.")

# Graphviz Digraph with clean left-to-right flow
diagram = graphviz.Digraph(format='png')
diagram.attr(rankdir='LR', size='10', nodesep='1.2', ranksep='1.5')
diagram.attr('node', shape='box', style='filled', fillcolor='#E6F2FF', fontname='Helvetica')

# Signal chain nodes
diagram.node("Antenna", "Antenna\n326.5 MHz")
diagram.node("RF Amp", "RF Amplifier\n30 dB / 15 MHz")
diagram.node("Filter", "Image Rejection Filter")
diagram.node("Mixer", "Mixer")
diagram.node("LO", "LO Branching\n296.5 MHz")
diagram.node("Phase Shifter", "LO Phase Shifter")
diagram.node("IF Amp 27", "IF Amplifier\n27 dB / 15 MHz")
diagram.node("Cable", "300m Coax Cable")
diagram.node("PA1", "IF Amplifier\n30 dB")
diagram.node("Delay", "Delay Line")
diagram.node("PA2", "IF Amplifier\n30 dB")
diagram.node("Beamform", "Beam Forming Network")
diagram.node("PA3", "IF Amplifier\n70 dB / 4 MHz")
diagram.node("Correlator", "Correlator")
diagram.node("Power", "Total Power Monitor")
diagram.node("ADC", "To ADC")

# Connections
diagram.edge("Antenna", "RF Amp")
diagram.edge("RF Amp", "Filter")
diagram.edge("Filter", "Mixer")
diagram.edge("LO", "Phase Shifter")
diagram.edge("Phase Shifter", "Mixer")
diagram.edge("Mixer", "IF Amp 27")
diagram.edge("IF Amp 27", "Cable")
diagram.edge("Cable", "PA1")
diagram.edge("PA1", "Delay")
diagram.edge("Delay", "PA2")
diagram.edge("PA2", "Beamform")
diagram.edge("Beamform", "PA3")
diagram.edge("PA3", "Correlator")
diagram.edge("Correlator", "Power")
diagram.edge("Power", "ADC")

# Display the diagram
st.graphviz_chart(diagram, use_container_width=True)

# Select box to display descriptions
component = st.selectbox("🔍 Select a component to inspect:", [
    "Antenna",
    "RF Amplifier",
    "Image Rejection Filter",
    "Mixer",
    "LO Branching",
    "LO Phase Shifter",
    "IF Amplifier (27 dB)",
    "300m Coax Cable",
    "IF Amplifier (PA1)",
    "Delay Line",
    "IF Amplifier (PA2)",
    "Beam Forming Network",
    "IF Amplifier (PA3)",
    "Correlator",
    "Total Power Monitor",
    "To ADC"
])

# Descriptions
descriptions = {
    "Antenna": "Captures 326.5 MHz radio waves from space.",
    "RF Amplifier": "Initial amplification stage at RF level, 30 dB gain and 15 MHz bandwidth.",
    "Image Rejection Filter": "Removes unwanted mirror signals before mixing.",
    "Mixer": "Mixes RF with local oscillator to generate intermediate frequency (IF).",
    "LO Branching": "Distributes 296.5 MHz LO signal to mixers.",
    "LO Phase Shifter": "Applies phase adjustments to the LO signal path.",
    "IF Amplifier (27 dB)": "First IF gain stage with 27 dB gain and 15 MHz bandwidth.",
    "300m Coax Cable": "Transports IF signal over 300m to receiver subsystem.",
    "IF Amplifier (PA1)": "Second IF amp stage post-cable with 30 dB gain.",
    "Delay Line": "Applies time alignment to signals from different antennas.",
    "IF Amplifier (PA2)": "Third IF amp to further strengthen signal.",
    "Beam Forming Network": "Combines signal paths for directional selectivity.",
    "IF Amplifier (PA3)": "Final IF stage before backend, 70 dB gain with narrow bandwidth.",
    "Correlator": "Performs signal correlation for interferometric measurements.",
    "Total Power Monitor": "Tracks total received signal power for system health.",
    "To ADC": "Final analog signal sent to digital converters for analysis."
}

if component in descriptions:
    st.markdown(f"### ℹ️ {component}")
    st.write(descriptions[component])
