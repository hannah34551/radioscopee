import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ORT Receiver Interactive SVG", layout="wide")
st.title("📡 ORT Receiver System – Interactive Diagram")

st.markdown("This is a prototype interactive version of the ORT receiver diagram. Click on a component to view details.")

# HTML + SVG layout prototype
html_code = """
<div style="text-align:center">
<svg width="800" height="600" style="border:1px solid #ccc; background:#fff">
  <!-- Antenna -->
  <rect id="antenna" x="20" y="250" width="100" height="40" fill="#d9edf7" stroke="#31708f"/>
  <text x="70" y="275" font-size="12" text-anchor="middle" fill="#000">Antenna</text>

  <!-- RF Amp -->
  <rect id="rf_amp" x="140" y="250" width="100" height="40" fill="#fcf8e3" stroke="#8a6d3b"/>
  <text x="190" y="275" font-size="12" text-anchor="middle" fill="#000">RF Amp</text>

  <!-- Filter -->
  <rect id="filter" x="260" y="250" width="100" height="40" fill="#f2dede" stroke="#a94442"/>
  <text x="310" y="275" font-size="12" text-anchor="middle" fill="#000">Filter</text>

  <!-- Mixer -->
  <rect id="mixer" x="380" y="250" width="100" height="40" fill="#dff0d8" stroke="#3c763d"/>
  <text x="430" y="275" font-size="12" text-anchor="middle" fill="#000">Mixer</text>

  <!-- Simple arrows -->
  <line x1="120" y1="270" x2="140" y2="270" stroke="black" marker-end="url(#arrow)"/>
  <line x1="240" y1="270" x2="260" y2="270" stroke="black" marker-end="url(#arrow)"/>
  <line x1="360" y1="270" x2="380" y2="270" stroke="black" marker-end="url(#arrow)"/>

  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="5" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#000" />
    </marker>
  </defs>
</svg>
</div>
"""

components.html(html_code, height=650)  # Embed in Streamlit
