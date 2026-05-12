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
# SIDEBAR CORPORATIVO
# =========================================================
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
                width=170
            )
        # =====================================================
        # EMPRESA
        # =====================================================

        # st.markdown(
        #     """
        #         <div class="sidebar-company">
        #             Elite SST
        #         </div>

        #         <div class="sidebar-subtitle">
        #             Plataforma Empresarial
        #         </div>

        #         <div class="sidebar-divider"></div>

        #     </div>
        #     """,
        #     unsafe_allow_html=True
        # )

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

        st.page_link(
            "app.py",
            label="Dashboard",
            icon="📊"
        )

        st.page_link(
            "pages/1_Admin.py",
            label="Administración",
            icon="⚙️"
        )

        st.page_link(
            "pages/2_Asistencia.py",
            label="Asistencia",
            icon="📝"
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