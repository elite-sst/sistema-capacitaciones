import streamlit as st

from pathlib import Path


# =========================================================
# CARGAR CSS
# =========================================================

def load_css():

    css_path = Path("styles/main.css")

    if css_path.exists():

        with open(css_path, encoding="utf-8") as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

    else:

        st.error(
            "No se encontró el archivo main.css"
        )


# =========================================================
# SIDEBAR ERP
# =========================================================

def render_sidebar():

    with st.sidebar:

        # =====================================================
        # LOGO
        # =====================================================

        logo_path = Path(
            "assets/logo_elite_sin_fondo.png"
        )

        st.markdown(
            """
            <div class="sidebar-logo-wrapper">
            """,
            unsafe_allow_html=True
        )

        if logo_path.exists():

            st.image(
                str(logo_path),
                use_container_width=True
            )

        # =====================================================
        # MODULOS
        # =====================================================

        st.markdown(
            """
            <div class="sidebar-section-title">
                📂 MÓDULOS
            </div>
            """,
            unsafe_allow_html=True
        )

        # =====================================================
        # MENU ERP
        # =====================================================

        st.markdown(
            '<div class="sidebar-menu">',
            unsafe_allow_html=True
        )

        # =====================================================
        # HOME
        # =====================================================

        if st.button(
            "🏠 Inicio",
            key="btn_home",
            use_container_width=True
        ):

            st.session_state.page = "home"

            st.rerun()

        # =====================================================
        # ADMIN
        # =====================================================

        if st.button(
            "⚙️ Administración",
            key="btn_admin",
            use_container_width=True
        ):

            st.session_state.page = "admin"

            st.rerun()

        # =====================================================
        # ASISTENCIA
        # =====================================================

        if st.button(
            "📝 Asistencia",
            key="btn_asistencia",
            use_container_width=True
        ):

            st.session_state.page = "asistencia"

            st.rerun()

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

        # =====================================================
        # FOOTER
        # =====================================================

        st.markdown(
            """
            <div class="sidebar-footer">
                Sistema Corporativo v2.0
            </div>
            """,
            unsafe_allow_html=True
        )