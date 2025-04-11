import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ORT Receiver Interactive SVG", layout="wide")
st.title("📡 ORT Receiver System – Interactive Diagram")

st.markdown("Click a component in the diagram to view details. This is a visual prototype.")

clicked = st.session_state.get("clicked", "None")

# JavaScript handler to capture clicks
html_code = f"""
<div style='text-align:center'>
<svg width='1000' height='600' style='border:1px solid #ccc; background:#fff' onclick='handleClick(evt)'>
  <!-- Define arrow marker -->
  <defs>
    <marker id='arrow' markerWidth='10' markerHeight='10' refX='5' refY='3' orient='auto' markerUnits='strokeWidth'>
      <path d='M0,0 L0,6 L9,3 z' fill='#000' />
    </marker>
  </defs>

  <!-- Components -->
  <rect id='antenna' x='20' y='250' width='100' height='40' fill='#d9edf7' stroke='#31708f' />
  <text x='70' y='275' font-size='12' text-anchor='middle'>Antenna</text>

  <rect id='rf_amp' x='140' y='250' width='100' height='40' fill='#fcf8e3' stroke='#8a6d3b' />
  <text x='190' y='275' font-size='12' text-anchor='middle'>RF Amp</text>

  <rect id='filter' x='260' y='250' width='100' height='40' fill='#f2dede' stroke='#a94442' />
  <text x='310' y='275' font-size='12' text-anchor='middle'>Filter</text>

  <rect id='mixer' x='380' y='250' width='100' height='40' fill='#dff0d8' stroke='#3c763d' />
  <text x='430' y='275' font-size='12' text-anchor='middle'>Mixer</text>

  <rect id='if_amp' x='500' y='250' width='100' height='40' fill='#d9edf7' stroke='#31708f' />
  <text x='550' y='275' font-size='12' text-anchor='middle'>IF Amp</text>

  <rect id='cable' x='620' y='250' width='120' height='40' fill='#e2e2e2' stroke='#444' />
  <text x='680' y='275' font-size='12' text-anchor='middle'>300m Coax Cable</text>

  <!-- Arrows -->
  <line x1='120' y1='270' x2='140' y2='270' stroke='black' marker-end='url(#arrow)'/>
  <line x1='240' y1='270' x2='260' y2='270' stroke='black' marker-end='url(#arrow)'/>
  <line x1='360' y1='270' x2='380' y2='270' stroke='black' marker-end='url(#arrow)'/>
  <line x1='480' y1='270' x2='500' y2='270' stroke='black' marker-end='url(#arrow)'/>
  <line x1='600' y1='270' x2='620' y2='270' stroke='black' marker-end='url(#arrow)'/>
</svg>
<script>
function handleClick(evt) {
  const id = evt.target.id;
  if (id) {{
    const form = document.createElement('form');
    form.method = 'POST';
    form.action = '';
    const input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'clicked';
    input.value = id;
    form.appendChild(input);
    document.body.appendChild(form);
    form.submit();
  }}
}
</script>
"""

clicked_value = st.experimental_get_query_params().get("clicked")
if clicked_value:
    st.session_state.clicked = clicked_value[0]

components.html(html_code, height=650)

# Info panel
descriptions = {
    "antenna": "Collects cosmic signals at 326.5 MHz.",
    "rf_amp": "Amplifies RF signal with 30 dB gain and 15 MHz bandwidth.",
    "filter": "Image rejection filter removes unwanted mirrored frequencies.",
    "mixer": "Mixes incoming RF with local oscillator to produce IF.",
    "if_amp": "Amplifies the intermediate frequency signal.",
    "cable": "300m RG-8 coaxial cable to transmit IF signal."
}

if clicked in descriptions:
    st.markdown(f"### 🔍 {clicked.replace('_', ' ').title()}")
    st.write(descriptions[clicked])
