import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

st.set_page_config(page_title="ORT Receiver Network", layout="wide")
st.title("📡 ORT Receiver System – Interactive Network Diagram")

# Define nodes
nodes = [
    Node(id="Antenna", label="Antenna\n326.5 MHz", shape="box"),
    Node(id="RF Amp", label="RF Amp\n30 dB / 15 MHz", shape="box"),
    Node(id="Image Filter", label="Image Filter", shape="box"),
    Node(id="Mixer", label="Mixer", shape="box"),
    Node(id="IF Amp 27", label="IF Amp\n27 dB / 15 MHz", shape="box"),
    Node(id="LO Branching", label="LO Branching\n296.5 MHz", shape="box"),
    Node(id="LO Phase Shifter", label="LO Phase Shifter", shape="box"),
    Node(id="Coax Cable", label="300m Coax Cable", shape="box"),
    Node(id="PA1", label="IF Amp\n30 dB", shape="box"),
    Node(id="Delay Line", label="Delay Line", shape="box"),
    Node(id="PA2", label="IF Amp\n30 dB", shape="box"),
    Node(id="Beam Forming", label="Beam Forming Network", shape="box"),
    Node(id="PA3", label="IF Amp\n70 dB / 4 MHz", shape="box"),
    Node(id="Correlator", label="Correlator", shape="box"),
    Node(id="Total Power", label="Total Power", shape="box"),
    Node(id="ADC", label="To ADC", shape="ellipse")
]

# Define edges (signal path)
edges = [
    Edge(source="Antenna", target="RF Amp"),
    Edge(source="RF Amp", target="Image Filter"),
    Edge(source="Image Filter", target="Mixer"),
    Edge(source="LO Branching", target="LO Phase Shifter"),
    Edge(source="LO Phase Shifter", target="Mixer"),
    Edge(source="Mixer", target="IF Amp 27"),
    Edge(source="IF Amp 27", target="Coax Cable"),
    Edge(source="Coax Cable", target="PA1"),
    Edge(source="PA1", target="Delay Line"),
    Edge(source="Delay Line", target="PA2"),
    Edge(source="PA2", target="Beam Forming"),
    Edge(source="Beam Forming", target="PA3"),
    Edge(source="PA3", target="Correlator"),
    Edge(source="Correlator", target="Total Power"),
    Edge(source="Total Power", target="ADC")
]

# Configure layout
config = Config(
    width=1000,
    height=600,
    directed=True,
    nodeHighlightBehavior=True,
    highlightColor="#F7A7A6",
    collapsible=True,
    physics=True,
)

# Draw graph
data = agraph(nodes=nodes, edges=edges, config=config)

# Info panel
descriptions = {
    "Antenna": "Collects radio waves at 326.5 MHz using arrayed elements.",
    "RF Amp": "Initial amplification: 30 dB gain, 15 MHz bandwidth.",
    "Image Filter": "Removes unwanted frequency reflections before mixing.",
    "Mixer": "Combines signal with LO for downconversion to IF.",
    "IF Amp 27": "Intermediate frequency amplifier stage with 27 dB gain.",
    "LO Branching": "Splits LO (296.5 MHz) for use in dual mixers.",
    "LO Phase Shifter": "Applies phase alignment to LO signal.",
    "Coax Cable": "300m coaxial cable for IF signal transmission.",
    "PA1": "Post-cable IF amp with 30 dB gain.",
    "Delay Line": "Applies delay to align multi-antenna paths.",
    "PA2": "Second IF amp for boosted signal.",
    "Beam Forming": "Combines multiple antenna paths into spatial beams.",
    "PA3": "Final IF amplifier: 70 dB gain, 4 MHz bandwidth.",
    "Correlator": "Performs spatial correlation of signals.",
    "Total Power": "Monitors overall signal strength.",
    "ADC": "Converts analog signal to digital for backend processing."
}

# Show component details
if data and data.get("selected_node"):
    node = data["selected_node"]
    st.markdown(f"### 🔍 {node}")
    st.write(descriptions.get(node, "No details available."))
