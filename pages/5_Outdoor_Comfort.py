import streamlit as st
from Upload_EPW import hide_streamlit_style
from bokeh_plots.utci import utciHeatmap

st.set_page_config(
   page_title="EPW Explorer - Outdoor Comfort",
   page_icon="🧭",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
df = st.session_state['df']

if st.session_state['df'] is not None:
    with st.container():
        st.header("Universal Thermal Climate Index (UTCI) Heatmap")
        st.bokeh_chart(utciHeatmap(df), use_container_width=True)
else:
    st.header("Upload an EPW weather file to visualise the plots")