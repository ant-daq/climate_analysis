import streamlit as st
from Upload_EPW import hide_streamlit_style
from bokeh_plots.daily import daily

# st.set_page_config(
#    page_title="EPW Explorer - Hourly",
#    page_icon="🕘",
#    layout="wide",
#    initial_sidebar_state="expanded",
# )

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
df = st.session_state['df']

if st.session_state['df'] is not None:
      with st.container():
        st.header("Daily Statistics")
        options = ['DryBulb','RelativeHumidity','DewPoint','WindSpeed','GlobalHorizontalRadiation','DirectNormalRadiation','DiffuseHorizontalRadiation']
        option = st.selectbox('Pick a variable', options, index=0)
        st.bokeh_chart(daily(df, variable=option), use_container_width=False)
else:
    st.header("Upload an EPW weather file to visualise the plots")