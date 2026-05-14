import streamlit as st

from views.asistencia import render_asistencia


# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================

st.set_page_config(

    page_title="Gestión corporativa de asistencia y formación del personal",

    page_icon="📋",

    layout="wide",

    initial_sidebar_state="collapsed"
)


# =========================================================
# QUERY PARAMS
# =========================================================

params = st.query_params

view_query = params.get("view", "")

# =========================================================
# VALIDAR LISTA QUERY PARAMS
# =========================================================

if isinstance(view_query, list):

    view_query = view_query[0]


# # =========================================================
# # DEBUG
# # =========================================================

# st.write("VIEW QUERY:", view_query)


# =========================================================
# MODO PÚBLICO
# =========================================================

if view_query == "asistencia":

    # st.write("ENTRANDO DIRECTO A ASISTENCIA")

    render_asistencia()

# =========================================================
# ERP
# =========================================================

else:

    # st.write("ENTRANDO A ERP")

    from ui.layout import load_css
    from ui.layout import render_sidebar

    from ui.components import render_hero
    from ui.components import render_kpis
    from ui.components import render_modules

    from views.admin import render_admin

    # =====================================================
    # SESSION STATE
    # =====================================================

    if "page" not in st.session_state:

        st.session_state.page = "home"

    # =====================================================
    # CSS
    # =====================================================

    load_css()

    # =====================================================
    # SIDEBAR
    # =====================================================

    render_sidebar()

    # =====================================================
    # HOME
    # =====================================================

    if st.session_state.page == "home":

        render_hero()

        st.markdown(
            "<div style='height:10px'></div>",
            unsafe_allow_html=True
        )

        render_kpis()

        st.markdown(
            "<div style='height:30px'></div>",
            unsafe_allow_html=True
        )

        render_modules()

    # =====================================================
    # ADMIN
    # =====================================================

    elif st.session_state.page == "admin":

        render_admin()