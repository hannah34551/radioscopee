import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="Radio Telescope Network Diagram", layout="wide")

st.title("📡 Radio Telescope Heterodyne Receiver Diagram")

components = [
    "Antenna",
    "Feed Horn",
    "LNA",
    "Mixer",
    "Local Oscillator",
    "IF Amplifier",
    "ADC",
    "Correlator",
    "Data Processor"
]

connections = [
    ("Antenna", "Feed Horn"),
    ("Feed Horn", "LNA"),
    ("LNA", "Mixer"),
    ("Local Oscillator", "Mixer"),
    ("Mixer", "IF Amplifier"),
    ("IF Amplifier", "ADC"),
    ("ADC", "Correlator"),
    ("Correlator", "Data Processor")
]

G = nx.DiGraph()
G.add_edges_from(connections)

pos = nx.spring_layout(G, seed=42)

fig, ax = plt.subplots(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, arrowsize=20, ax=ax)
st.pyplot(fig)
