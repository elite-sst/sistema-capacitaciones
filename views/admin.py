import os
from io import BytesIO

import pandas as pd
import streamlit as st

from sqlalchemy import text
from utils.db import engine

from openpyxl.worksheet.table import Table
from openpyxl.worksheet.table import TableStyleInfo

from openpyxl.styles import Font
from openpyxl.styles import Alignment
from openpyxl.styles import PatternFill

from openpyxl.utils import get_column_letter


# =========================================================
# RENDER ADMIN
# =========================================================

def render_admin():

    # =========================================================
    # HEADER ERP
    # =========================================================

    st.html("""

        <div class="banner">

            <div class="banner-left">

                <div class="banner-title">
                    🔐 Panel Administrador
                </div>

                <div class="banner-sub">
                    Gestión corporativa Elite Ingenieros
                </div>

            </div>

            <div class="banner-badge">
                Sistema Seguro
            </div>

        </div>

        """)

    # =========================================================
    # LOGIN ADMIN
    # =========================================================

    ADMIN_PASSWORD = st.secrets["ADMIN_PASSWORD"]

    if "admin_autenticado" not in st.session_state:

        st.session_state.admin_autenticado = False

    if not st.session_state.admin_autenticado:

        col1, col2, col3 = st.columns([1, 1.3, 1])

        with col2:

            st.markdown(
                """
                <div class="login-glow"></div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <div class="login-top-icon">
                    🛡️
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <div class="login-title">
                    Acceso Corporativo
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <div class="login-subtitle">
                    Plataforma segura de administración empresarial
                </div>
                """,
                unsafe_allow_html=True
            )

            password = st.text_input(
                "Contraseña",
                type="password",
                label_visibility="collapsed",
                placeholder="Ingrese contraseña administrador",
                key="login_password"
            )

            st.markdown(
                "<div style='height:18px'></div>",
                unsafe_allow_html=True
            )

            if st.button(
                "Ingresar al Sistema",
                use_container_width=True,
                key="login_button"
            ):

                if password == ADMIN_PASSWORD:

                    st.session_state.admin_autenticado = True

                    st.rerun()

                else:

                    st.error(
                        "❌ Contraseña incorrecta"
                    )

            st.markdown(
                """
                <div class="login-footer">
                    Elite Ingenieros · ERP SaaS
                </div>
                """,
                unsafe_allow_html=True
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

        # =====================================================
        # TIPO REGISTRO
        # =====================================================

        tipo_registro = st.radio(
            "Tipo de registro",
            [
                "Charla",
                "Capacitación"
            ],
            horizontal=True
        )

        # =====================================================
        # VARIABLES PREGUNTAS
        # =====================================================

        pregunta_1 = None
        pregunta_2 = None
        pregunta_3 = None
        pregunta_4 = None
        pregunta_5 = None

        p1_opcion_a = None
        p1_opcion_b = None
        p1_opcion_c = None
        p1_opcion_d = None
        p1_correcta = None

        p2_opcion_a = None
        p2_opcion_b = None
        p2_opcion_c = None
        p2_opcion_d = None
        p2_correcta = None

        p3_opcion_a = None
        p3_opcion_b = None
        p3_opcion_c = None
        p3_opcion_d = None
        p3_correcta = None

        p4_opcion_a = None
        p4_opcion_b = None
        p4_opcion_c = None
        p4_opcion_d = None
        p4_correcta = None

        p5_opcion_a = None
        p5_opcion_b = None
        p5_opcion_c = None
        p5_opcion_d = None
        p5_correcta = None

        # =====================================================
        # PREGUNTAS CAPACITACIÓN
        # =====================================================

        if tipo_registro == "Capacitación":

            st.markdown("### 📝 Preguntas de evaluación")

            with st.expander("Pregunta 1", expanded=True):

                pregunta_1 = st.text_input("Texto pregunta 1")

                col_a, col_b = st.columns(2)

                with col_a:

                    p1_opcion_a = st.text_input("Pregunta 1 - Opción A")
                    p1_opcion_b = st.text_input("Pregunta 1 - Opción B")

                with col_b:

                    p1_opcion_c = st.text_input("Pregunta 1 - Opción C")
                    p1_opcion_d = st.text_input("Pregunta 1 - Opción D")

                p1_correcta = st.radio(
                    "Respuesta correcta pregunta 1",
                    ["A", "B", "C", "D"],
                    horizontal=True,
                    key="p1_correcta"
                )

            with st.expander("Pregunta 2"):

                pregunta_2 = st.text_input("Texto pregunta 2")

                col_a, col_b = st.columns(2)

                with col_a:

                    p2_opcion_a = st.text_input("Pregunta 2 - Opción A")
                    p2_opcion_b = st.text_input("Pregunta 2 - Opción B")

                with col_b:

                    p2_opcion_c = st.text_input("Pregunta 2 - Opción C")
                    p2_opcion_d = st.text_input("Pregunta 2 - Opción D")

                p2_correcta = st.radio(
                    "Respuesta correcta pregunta 2",
                    ["A", "B", "C", "D"],
                    horizontal=True,
                    key="p2_correcta"
                )

            with st.expander("Pregunta 3"):

                pregunta_3 = st.text_input("Texto pregunta 3")

                col_a, col_b = st.columns(2)

                with col_a:

                    p3_opcion_a = st.text_input("Pregunta 3 - Opción A")
                    p3_opcion_b = st.text_input("Pregunta 3 - Opción B")

                with col_b:

                    p3_opcion_c = st.text_input("Pregunta 3 - Opción C")
                    p3_opcion_d = st.text_input("Pregunta 3 - Opción D")

                p3_correcta = st.radio(
                    "Respuesta correcta pregunta 3",
                    ["A", "B", "C", "D"],
                    horizontal=True,
                    key="p3_correcta"
                )

            with st.expander("Pregunta 4"):

                pregunta_4 = st.text_input("Texto pregunta 4")

                col_a, col_b = st.columns(2)

                with col_a:

                    p4_opcion_a = st.text_input("Pregunta 4 - Opción A")
                    p4_opcion_b = st.text_input("Pregunta 4 - Opción B")

                with col_b:

                    p4_opcion_c = st.text_input("Pregunta 4 - Opción C")
                    p4_opcion_d = st.text_input("Pregunta 4 - Opción D")

                p4_correcta = st.radio(
                    "Respuesta correcta pregunta 4",
                    ["A", "B", "C", "D"],
                    horizontal=True,
                    key="p4_correcta"
                )

            with st.expander("Pregunta 5"):

                pregunta_5 = st.text_input("Texto pregunta 5")

                col_a, col_b = st.columns(2)

                with col_a:

                    p5_opcion_a = st.text_input("Pregunta 5 - Opción A")
                    p5_opcion_b = st.text_input("Pregunta 5 - Opción B")

                with col_b:

                    p5_opcion_c = st.text_input("Pregunta 5 - Opción C")
                    p5_opcion_d = st.text_input("Pregunta 5 - Opción D")

                p5_correcta = st.radio(
                    "Respuesta correcta pregunta 5",
                    ["A", "B", "C", "D"],
                    horizontal=True,
                    key="p5_correcta"
                )

        # =====================================================
        # CREAR FORMACIÓN
        # =====================================================

        if st.button(
            "Crear formación",
            use_container_width=True
        ):

            if not nombre_formacion:

                st.warning(
                    "⚠️ Debe ingresar el nombre"
                )

            elif tipo_registro == "Capacitación" and not pregunta_1:

                st.warning(
                    "⚠️ Para una capacitación debe ingresar al menos la pregunta 1."
                )

            else:

                try:

                    with engine.begin() as conn:

                        resultado = conn.execute(
                            text("""
                                INSERT INTO formaciones (
                                    nombre_formacion,
                                    fecha_asistencia,
                                    formador,
                                    tipo_registro,
                                    pregunta_1,
                                    pregunta_2,
                                    pregunta_3,
                                    pregunta_4,
                                    pregunta_5,
                                    p1_opcion_a,
                                    p1_opcion_b,
                                    p1_opcion_c,
                                    p1_opcion_d,
                                    p1_correcta,
                                    p2_opcion_a,
                                    p2_opcion_b,
                                    p2_opcion_c,
                                    p2_opcion_d,
                                    p2_correcta,
                                    p3_opcion_a,
                                    p3_opcion_b,
                                    p3_opcion_c,
                                    p3_opcion_d,
                                    p3_correcta,
                                    p4_opcion_a,
                                    p4_opcion_b,
                                    p4_opcion_c,
                                    p4_opcion_d,
                                    p4_correcta,
                                    p5_opcion_a,
                                    p5_opcion_b,
                                    p5_opcion_c,
                                    p5_opcion_d,
                                    p5_correcta
                                )
                                VALUES (
                                    :nombre_formacion,
                                    :fecha_asistencia,
                                    :formador,
                                    :tipo_registro,
                                    :pregunta_1,
                                    :pregunta_2,
                                    :pregunta_3,
                                    :pregunta_4,
                                    :pregunta_5,
                                    :p1_opcion_a,
                                    :p1_opcion_b,
                                    :p1_opcion_c,
                                    :p1_opcion_d,
                                    :p1_correcta,
                                    :p2_opcion_a,
                                    :p2_opcion_b,
                                    :p2_opcion_c,
                                    :p2_opcion_d,
                                    :p2_correcta,
                                    :p3_opcion_a,
                                    :p3_opcion_b,
                                    :p3_opcion_c,
                                    :p3_opcion_d,
                                    :p3_correcta,
                                    :p4_opcion_a,
                                    :p4_opcion_b,
                                    :p4_opcion_c,
                                    :p4_opcion_d,
                                    :p4_correcta,
                                    :p5_opcion_a,
                                    :p5_opcion_b,
                                    :p5_opcion_c,
                                    :p5_opcion_d,
                                    :p5_correcta
                                )
                                RETURNING id
                            """),
                            {
                                "nombre_formacion": nombre_formacion.strip(),
                                "fecha_asistencia": fecha,
                                "formador": formador.strip(),
                                "tipo_registro": tipo_registro,
                                "pregunta_1": pregunta_1,
                                "pregunta_2": pregunta_2,
                                "pregunta_3": pregunta_3,
                                "pregunta_4": pregunta_4,
                                "pregunta_5": pregunta_5,
                                "p1_opcion_a": p1_opcion_a,
                                "p1_opcion_b": p1_opcion_b,
                                "p1_opcion_c": p1_opcion_c,
                                "p1_opcion_d": p1_opcion_d,
                                "p1_correcta": p1_correcta,
                                "p2_opcion_a": p2_opcion_a,
                                "p2_opcion_b": p2_opcion_b,
                                "p2_opcion_c": p2_opcion_c,
                                "p2_opcion_d": p2_opcion_d,
                                "p2_correcta": p2_correcta,
                                "p3_opcion_a": p3_opcion_a,
                                "p3_opcion_b": p3_opcion_b,
                                "p3_opcion_c": p3_opcion_c,
                                "p3_opcion_d": p3_opcion_d,
                                "p3_correcta": p3_correcta,
                                "p4_opcion_a": p4_opcion_a,
                                "p4_opcion_b": p4_opcion_b,
                                "p4_opcion_c": p4_opcion_c,
                                "p4_opcion_d": p4_opcion_d,
                                "p4_correcta": p4_correcta,
                                "p5_opcion_a": p5_opcion_a,
                                "p5_opcion_b": p5_opcion_b,
                                "p5_opcion_c": p5_opcion_c,
                                "p5_opcion_d": p5_opcion_d,
                                "p5_correcta": p5_correcta
                            }
                        )

                        id_formacion = resultado.fetchone()[0]

                    url = (
                        f"https://elite-sst.streamlit.app/"
                        f"?view=asistencia&formacion={id_formacion}"
                    )

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

        # =====================================================
        # AGREGAR
        # =====================================================

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

                if (
                    not cedula_emp
                    or
                    not nombre_emp
                    or
                    not cargo_emp
                ):

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

        # =====================================================
        # CONSULTAR
        # =====================================================

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

        if not opciones:

            st.warning(
                "⚠️ No existen formaciones registradas."
            )

            st.info(
                "Cree una formación para visualizar reportes."
            )

            st.stop()

        seleccion = st.selectbox(
            "Seleccione formación",
            list(opciones.keys())
        )

        id_seleccionado = opciones[seleccion]
        # =====================================================
        # ACTUALIZAR REPORTE
        # =====================================================

        if st.button(
            "🔄 Actualizar reporte",
            use_container_width=True
        ):

            st.rerun()
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
                        f.nombre_formacion,
                        f.fecha_asistencia,
                        a.clasificacion_formacion,
                        a.tipo_formacion,
                        a.autoriza_datos,
                        a.respuesta_1,
                        a.resultado_1,
                        a.respuesta_2,
                        a.resultado_2,
                        a.respuesta_3,
                        a.resultado_3,
                        a.respuesta_4,
                        a.resultado_4,
                        a.respuesta_5,
                        a.resultado_5,
                        a.puntaje,
                        a.fecha_registro
                    FROM asistencias a
                    INNER JOIN formaciones f
                        ON a.id_formacion = f.id
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

        # =====================================================
        # KPIS
        # =====================================================

        col1, col2 = st.columns([1, 3])

        with col1:

            st.metric(
                "👥 Total Asistencias",
                len(df_asistencias)
            )

        with col2:

            nombre_kpi = seleccion.split("-", 1)[1].strip()

            st.markdown(
                f"""
                <div style="
                    background:white;
                    border-radius:14px;
                    padding:14px 18px;
                    border:1px solid #e2e8f0;
                ">
                    <div style="
                        font-size:13px;
                        color:#64748b;
                        font-weight:600;
                        margin-bottom:6px;
                    ">
                        📚 Formación
                    </div>

                    <div style="
                        font-size:18px;
                        color:#0f172a;
                        font-weight:700;
                        line-height:1.25;
                    ">
                        {nombre_kpi}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        # =====================================================
        # EXPORTAR EXCEL
        # =====================================================

        if not df_asistencias.empty:

            output = BytesIO()

            with pd.ExcelWriter(
                output,
                engine="openpyxl"
            ) as writer:

                df_asistencias.to_excel(
                    writer,
                    index=False,
                    sheet_name="Reporte"
                )

                worksheet = writer.sheets["Reporte"]

                for cell in worksheet[1]:

                    cell.font = Font(
                        bold=True,
                        color="FFFFFF"
                    )

                    cell.alignment = Alignment(
                        horizontal="center",
                        vertical="center"
                    )

                    cell.fill = PatternFill(
                        start_color="166534",
                        end_color="166534",
                        fill_type="solid"
                    )

                for column_cells in worksheet.columns:

                    length = max(
                        len(str(cell.value))
                        if cell.value else 0
                        for cell in column_cells
                    )

                    worksheet.column_dimensions[
                        get_column_letter(
                            column_cells[0].column
                        )
                    ].width = length + 5

                total_filas = len(df_asistencias) + 1
                total_columnas = len(df_asistencias.columns)

                rango = (
                    f"A1:"
                    f"{get_column_letter(total_columnas)}"
                    f"{total_filas}"
                )

                tabla = Table(
                    displayName="TablaAsistencias",
                    ref=rango
                )

                estilo = TableStyleInfo(
                    name="TableStyleMedium9",
                    showRowStripes=True,
                    showColumnStripes=False
                )

                tabla.tableStyleInfo = estilo

                worksheet.add_table(tabla)

            output.seek(0)

            st.download_button(
                label="📥 Descargar Reporte Excel",
                data=output,
                file_name=(
                    f"Reporte_Asistencia_"
                    f"{id_seleccionado}.xlsx"
                ),
                mime=(
                    "application/vnd.openxmlformats-"
                    "officedocument.spreadsheetml.sheet"
                ),
                use_container_width=True
            )