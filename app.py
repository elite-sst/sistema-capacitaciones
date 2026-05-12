import streamlit as st

from ui.layout import load_css
from ui.layout import render_sidebar

from ui.components import render_hero
from ui.components import render_kpis
from ui.components import render_modules


# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================

st.set_page_config(

    page_title="Sistema Capacitaciones",

    page_icon="📋",

    layout="wide",

    initial_sidebar_state="expanded"
)


# =========================================================
# CARGAR ESTILOS
# =========================================================

load_css()


# =========================================================
# SIDEBAR
# =========================================================

render_sidebar()


# =========================================================
# HERO SECTION
# =========================================================

render_hero()


# =========================================================
# ESPACIADO
# =========================================================

st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)


# =========================================================
# KPIS
# =========================================================

render_kpis()


# =========================================================
# ESPACIADO
# =========================================================

st.markdown("<div style='height:30px'></div>", unsafe_allow_html=True)


# =========================================================
# MÓDULOS
# =========================================================

render_modules()