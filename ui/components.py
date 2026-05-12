import streamlit as st


# =========================================================
# HERO
# =========================================================

def render_hero():

    st.html("""
<div class="banner">

    <div class="banner-left">

        <div class="banner-title">
            📋 Sistema Capacitaciones
        </div>

        <div class="banner-sub">
            Plataforma corporativa empresarial
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
# KPIS
# =========================================================

def render_kpis():

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        render_kpi("128", "Capacitaciones")

    with col2:
        render_kpi("540", "Empleados")

    with col3:
        render_kpi("98%", "Cobertura")

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
        capacitaciones y reportes.
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