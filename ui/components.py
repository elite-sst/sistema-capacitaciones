import streamlit as st

from sqlalchemy import text
from utils.db import engine


# =========================================================
# HERO
# =========================================================

def render_hero():

    st.html("""
<div class="banner">

    <div class="banner-left">

        <div class="banner-title">
            📋 Portal de Formación Elite
        </div>

        <div class="banner-sub">
            Gestión corporativa de formación y asistencia
        </div>

    </div>

    <div class="banner-badge">
        Sistema Activo
    </div>

</div>
""")


# =========================================================
# KPI
# =========================================================

def render_kpi(valor, texto):

    st.html(f"""
<div class="kpi-box">

    <div class="kpi-number">
        {valor}
    </div>

    <div class="kpi-text">
        {texto}
    </div>

</div>
""")


# =========================================================
# KPIS DINÁMICOS
# =========================================================

def render_kpis():

    try:

        with engine.begin() as conn:

            total_formaciones = conn.execute(
                text("""
                    SELECT COUNT(*)
                    FROM formaciones
                """)
            ).scalar() or 0

            total_empleados = conn.execute(
                text("""
                    SELECT COUNT(*)
                    FROM empleados
                    WHERE estado = 'ACTIVO'
                """)
            ).scalar() or 0

            total_asistencias = conn.execute(
                text("""
                    SELECT COUNT(*)
                    FROM asistencias
                """)
            ).scalar() or 0

    except Exception:

        total_formaciones = 0
        total_empleados = 0
        total_asistencias = 0

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        render_kpi(total_formaciones, "Formaciones")

    with col2:
        render_kpi(total_empleados, "Empleados")

    with col3:
        render_kpi(total_asistencias, "Asistencias")

    with col4:
        render_kpi("Activo", "Estado")


# =========================================================
# MODULES
# =========================================================

def render_modules():

    col1, col2 = st.columns(2)

    with col1:

        st.html("""
<div class="module-box">

    <div class="module-title">
        ⚙ Administración
    </div>

    <div class="module-description">
        Gestión de empleados,
        formaciones y reportes.
    </div>

</div>
""")

    with col2:

        st.html("""
<div class="module-box">

    <div class="module-title">
        📝 Asistencia
    </div>

    <div class="module-description">
        Registro de asistencia empresarial.
    </div>

</div>
""")