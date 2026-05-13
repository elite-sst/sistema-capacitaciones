import streamlit as st

from ui.layout import load_css
from ui.layout import render_sidebar

from ui.components import render_hero
from ui.components import render_kpis
from ui.components import render_modules

from views.admin import render_admin
from views.asistencia import render_asistencia


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
# SESSION STATE ROUTER
# =========================================================

if "page" not in st.session_state:

    st.session_state.page = "home"


# =========================================================
# CARGAR CSS
# =========================================================

load_css()


# =========================================================
# SIDEBAR ERP
# =========================================================

render_sidebar()


# =========================================================
# ROUTER PRINCIPAL
# =========================================================

if st.session_state.page == "home":

    # =====================================================
    # HERO
    # =====================================================

    render_hero()

    # =====================================================
    # ESPACIADO
    # =====================================================

    st.markdown(
        "<div style='height:10px'></div>",
        unsafe_allow_html=True
    )

    # =====================================================
    # KPIS
    # =====================================================

    render_kpis()

    # =====================================================
    # ESPACIADO
    # =====================================================

    st.markdown(
        "<div style='height:30px'></div>",
        unsafe_allow_html=True
    )

    # =====================================================
    # MÓDULOS
    # =====================================================

    render_modules()


# =========================================================
# ADMIN
# =========================================================

elif st.session_state.page == "admin":

    render_admin()


# =========================================================
# ASISTENCIA
# =========================================================

elif st.session_state.page == "asistencia":

    render_asistencia()