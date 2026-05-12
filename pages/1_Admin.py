import os
from io import BytesIO

import pandas as pd
import streamlit as st
from sqlalchemy import text
from utils.db import engine

from openpyxl import load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.styles import Font, Alignment
from openpyxl.utils import get_column_letter


# =========================================================
# CONFIG
# =========================================================

st.set_page_config(
    page_title="Panel Administrador",
    page_icon="🔐",
    layout="wide"
)

# =========================================================
# CSS ERP PREMIUM
# =========================================================

st.markdown("""
<style>

/* =========================================================
GLOBAL
========================================================= */

html,
body,
[class*="css"] {

    font-family:
    "Inter",
    sans-serif;
}

/* =========================================================
APP
========================================================= */

.stApp {

    background:
        linear-gradient(
            180deg,
            #f1f5f9 0%,
            #e2e8f0 100%
        );
}

/* =========================================================
OCULTAR STREAMLIT
========================================================= */

#MainMenu,
footer,
.stDeployButton,
[data-testid="stToolbar"] {

    visibility:hidden;
}

/* =========================================================
CONTENT
========================================================= */

.block-container {

    padding-top:2rem;
    padding-left:2.5rem;
    padding-right:2.5rem;
}

/* =========================================================
SOLO HEADER ERP
========================================================= */

.header-erp {

    background:
        linear-gradient(
            135deg,
            #166534 0%,
            #15803d 45%,
            #14532d 100%
        );

    border-radius:30px;

    padding:34px 42px;

    min-height:120px;

    border:
        1px solid rgba(255,255,255,0.08);

    box-shadow:
        0 20px 40px rgba(21,128,61,0.22);

    margin-bottom:2.5rem;
}

/* =========================================================
TITLE
========================================================= */

.banner-title {

    color:#ffffff;

    font-weight:900;

    font-size:46px;

    line-height:1.1;
}

/* =========================================================
SUBTITLE
========================================================= */

.banner-sub {

    color:#dcfce7;

    font-size:16px;

    margin-top:10px;
}

/* =========================================================
BADGE
========================================================= */

.banner-badge {

    background:
        rgba(255,255,255,0.14);

    padding:12px 22px;

    border-radius:999px;

    font-size:13px;

    color:#ecfdf5;

    border:
        1px solid rgba(255,255,255,0.18);

    font-weight:700;
}

/* =========================================================
LOGIN CARD
========================================================= */

.login-card {

    width:100%;

    background:
        linear-gradient(
            180deg,
            rgba(255,255,255,0.96),
            rgba(248,250,252,0.98)
        );

    border-radius:32px;

    padding:46px 40px 30px 40px;

    border:
        1px solid #e2e8f0;

    box-shadow:
        0 24px 40px rgba(15,23,42,0.08);

    backdrop-filter:blur(18px);

    text-align:center;

    margin-top:20px;

    margin-bottom:16px;
}

/* =========================================================
ICON LOGIN
========================================================= */

.login-icon {

    font-size:58px;

    margin-bottom:18px;
}

/* =========================================================
TITLE LOGIN
========================================================= */

.login-title {

    font-size:42px;

    font-weight:900;

    color:#166534;

    margin-bottom:10px;
}

/* =========================================================
SUBTITLE LOGIN
========================================================= */

.login-subtitle {

    color:#64748b;

    font-size:16px;

    margin-bottom:30px;
}

/* =========================================================
INPUT
========================================================= */

.stTextInput input {

    border-radius:18px !important;

    border:
        1px solid #dbe4ee !important;

    padding:16px !important;

    font-size:16px !important;

    background:white !important;

    box-shadow:
        0 4px 10px rgba(0,0,0,0.03);

    transition:0.2s ease;
}

/* =========================================================
FOCUS INPUT
========================================================= */

.stTextInput input:focus {

    border:
        1px solid #22c55e !important;

    box-shadow:
        0 0 0 4px rgba(34,197,94,0.12) !important;
}

/* =========================================================
BUTTONS
========================================================= */

.stButton button {

    width:100%;

    border:none !important;

    border-radius:18px !important;

    background:
        linear-gradient(
            135deg,
            #16a34a,
            #22c55e
        ) !important;

    color:white !important;

    font-weight:800 !important;

    font-size:16px !important;

    padding:14px 18px !important;

    transition:0.25s ease !important;

    box-shadow:
        0 12px 24px rgba(34,197,94,0.18);
}

/* =========================================================
HOVER BUTTON
========================================================= */

.stButton button:hover {

    transform:
        translateY(-2px);

    box-shadow:
        0 18px 30px rgba(34,197,94,0.28);
}

/* =========================================================
TABS
========================================================= */

.stTabs [data-baseweb="tab-list"] {

    gap:12px;
}

.stTabs [data-baseweb="tab"] {

    background:white;

    border-radius:16px;

    padding:12px 18px;

    font-weight:700;

    border:
        1px solid #e2e8f0;
}

/* =========================================================
DATAFRAME
========================================================= */

[data-testid="stDataFrame"] {

    border-radius:22px;

    overflow:hidden;

    border:
        1px solid #e2e8f0;
}
/* =========================================================
LOGIN CONTAINER STREAMLIT
========================================================= */

[data-testid="stVerticalBlockBorderWrapper"] {

    border-radius:30px !important;

    border:
        1px solid rgba(255,255,255,0.08) !important;

    background:
        linear-gradient(
            180deg,
            rgba(255,255,255,0.96),
            rgba(248,250,252,0.98)
        ) !important;

    padding:18px !important;

    box-shadow:
        0 24px 40px rgba(15,23,42,0.08) !important;
}
div[data-testid="stHorizontalBlock"]:has(.banner-title) {

    background:
        linear-gradient(
            135deg,
            #166534 0%,
            #15803d 45%,
            #14532d 100%
        );

    border-radius:30px;

    padding:34px 42px;

    border:
        1px solid rgba(255,255,255,0.08);

    box-shadow:
        0 20px 40px rgba(21,128,61,0.22);

    margin-bottom:2.5rem;

    ali            

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER ERP
# =========================================================

header_col1, header_col2 = st.columns([5, 1])

with header_col1:

    st.markdown(
        """
        <div class="banner-title">
            🔐 Panel Administrador
        </div>

        <div class="banner-sub">
            Gestión corporativa Elite Ingenieros
        </div>
        """,
        unsafe_allow_html=True
    )

with header_col2:

    st.markdown(
        """
        <div class="banner-badge">
            Sistema Seguro
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# CONTROL LOGIN
# =========================================================

ADMIN_PASSWORD = st.secrets["ADMIN_PASSWORD"]

if "admin_autenticado" not in st.session_state:
    st.session_state.admin_autenticado = False

if not st.session_state.admin_autenticado:

    col1, col2, col3 = st.columns([1, 1.3, 1])

    with col2:
      with st.container(border=True):      
        st.markdown("## 🔐 Acceso Admin")

        st.caption(
            "Ingrese credenciales corporativas"
        )

        password = st.text_input(
            "Contraseña",
            type="password",
            label_visibility="collapsed",
            placeholder="Ingrese contraseña administrador"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button(
            "Ingresar al Panel",
            use_container_width=True
        ):

            if password == ADMIN_PASSWORD:

                st.session_state.admin_autenticado = True
                st.rerun()

            else:

                st.error(
                    "❌ Contraseña incorrecta"
                )

    st.stop()

# =========================================================
# TABS
# =========================================================

tab_formacion, tab_empleados, tab_asistencias = st.tabs(
    [
        "📚 Crear Formación",
        "👥 Gestión Empleados",
        "📋 Asistencias y Reportes"
    ]
)

# =========================================================
# TAB FORMACIÓN
# =========================================================

with tab_formacion:

    st.subheader("📚 Crear Formación")

    col1, col2 = st.columns(2)

    with col1:
        nombre_formacion = st.text_input(
            "Nombre capacitación"
        )

    with col2:
        fecha = st.date_input(
            "Fecha asistencia"
        )

    formador = st.text_input(
        "Formador",
        value="Eduardo Florez"
    )

    if st.button(
        "Crear formación",
        use_container_width=True
    ):

        if not nombre_formacion:

            st.warning(
                "⚠️ Debe ingresar el nombre"
            )

        else:

            try:

                with engine.begin() as conn:

                    resultado = conn.execute(
                        text("""
                            INSERT INTO formaciones (
                                nombre_formacion,
                                fecha_asistencia,
                                formador
                            )
                            VALUES (
                                :nombre_formacion,
                                :fecha_asistencia,
                                :formador
                            )
                            RETURNING id
                        """),
                        {
                            "nombre_formacion": nombre_formacion.strip(),
                            "fecha_asistencia": fecha,
                            "formador": formador.strip()
                        }
                    )

                    id_formacion = resultado.fetchone()[0]

                url = f"https://elite-sst.streamlit.app/Asistencia?formacion={id_formacion}"

                st.success(
                    "✅ Formación creada correctamente"
                )

                st.code(url)

            except Exception as e:

                st.error(
                    f"❌ Error: {e}"
                )

# =========================================================
# TAB EMPLEADOS
# =========================================================

with tab_empleados:

    st.subheader("👥 Gestión Empleados")

    subtab_agregar, subtab_consultar = st.tabs(
        [
            "➕ Agregar",
            "🔎 Consultar"
        ]
    )

    with subtab_agregar:

        col1, col2 = st.columns(2)

        with col1:
            cedula_emp = st.text_input("Cédula")
            nombre_emp = st.text_input("Nombre")

        with col2:
            cargo_emp = st.text_input("Cargo")
            zona_emp = st.text_input(
                "Zona",
                value="Metropolitano"
            )

        proyecto_emp = st.text_input(
            "Proyecto",
            value="CONEXIÓN Y VINCULACIÓN METROPOLITANO"
        )

        if st.button(
            "Guardar empleado",
            use_container_width=True
        ):

            if not cedula_emp or not nombre_emp or not cargo_emp:

                st.warning(
                    "⚠️ Campos obligatorios"
                )

            else:

                try:

                    with engine.begin() as conn:

                        conn.execute(
                            text("""
                                INSERT INTO empleados (
                                    cedula,
                                    nombre_completo,
                                    cargo,
                                    proyecto,
                                    zona,
                                    estado
                                )
                                VALUES (
                                    :cedula,
                                    :nombre_completo,
                                    :cargo,
                                    :proyecto,
                                    :zona,
                                    'ACTIVO'
                                )
                            """),
                            {
                                "cedula": cedula_emp.strip(),
                                "nombre_completo": nombre_emp.strip(),
                                "cargo": cargo_emp.strip(),
                                "proyecto": proyecto_emp.strip(),
                                "zona": zona_emp.strip()
                            }
                        )

                    st.success(
                        "✅ Empleado guardado"
                    )

                except Exception as e:

                    st.error(
                        f"❌ Error: {e}"
                    )

    with subtab_consultar:

        buscar = st.text_input(
            "Buscar empleado"
        )

        with engine.begin() as conn:

            df_empleados = pd.read_sql(
                text("""
                    SELECT
                        cedula,
                        nombre_completo,
                        cargo,
                        proyecto,
                        zona,
                        estado,
                        fecha_creacion
                    FROM empleados
                    WHERE
                        :buscar = ''
                        OR cedula ILIKE :patron
                        OR nombre_completo ILIKE :patron
                        OR cargo ILIKE :patron
                    ORDER BY nombre_completo
                """),
                conn,
                params={
                    "buscar": buscar.strip(),
                    "patron": f"%{buscar.strip()}%"
                }
            )

        st.dataframe(
            df_empleados,
            use_container_width=True
        )

# =========================================================
# TAB ASISTENCIAS
# =========================================================

with tab_asistencias:

    st.subheader(
        "📋 Reportes Asistencia"
    )

    with engine.begin() as conn:

        df_formaciones = pd.read_sql(
            text("""
                SELECT
                    id,
                    nombre_formacion,
                    fecha_asistencia
                FROM formaciones
                ORDER BY id DESC
            """),
            conn
        )

    opciones = {
        f"{row.id} - {row.nombre_formacion}": row.id
        for row in df_formaciones.itertuples()
    }

    seleccion = st.selectbox(
        "Seleccione formación",
        list(opciones.keys())
    )

    id_seleccionado = opciones[seleccion]

    with engine.begin() as conn:

        df_asistencias = pd.read_sql(
            text("""
                SELECT
                    a.cedula,
                    a.nombre_completo,
                    a.cargo,
                    a.proyecto,
                    a.zona,
                    a.formador,
                    a.fecha_registro
                FROM asistencias a
                WHERE a.id_formacion = :id_formacion
                ORDER BY a.fecha_registro DESC
            """),
            conn,
            params={
                "id_formacion": id_seleccionado
            }
        )

    st.dataframe(
        df_asistencias,
        use_container_width=True
    )