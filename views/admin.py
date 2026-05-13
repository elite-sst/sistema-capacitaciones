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
                <div class="login-wrapper">
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

            st.markdown(
                "<div style='height:12px'></div>",
                unsafe_allow_html=True
            )

            password = st.text_input(
                "Contraseña",
                type="password",
                label_visibility="collapsed",
                placeholder="Ingrese contraseña administrador"
            )

            st.markdown(
                "<div style='height:18px'></div>",
                unsafe_allow_html=True
            )

            if st.button(
                "Ingresar al Sistema",
                use_container_width=True
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

            st.markdown(
                "</div>",
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

                    url = (
                        f"https://elite-sst.streamlit.app/"
                        f"?page=asistencia&formacion={id_formacion}"
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

        # =====================================================
        # KPIS
        # =====================================================

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "👥 Total Asistencias",
                len(df_asistencias)
            )

        with col2:

            st.metric(
                "📚 Formación",
                seleccion.split("-")[1].strip()
            )

        st.markdown(
            "<br>",
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

                # =============================================
                # HEADER
                # =============================================

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

                # =============================================
                # AUTO AJUSTE
                # =============================================

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

                # =============================================
                # TABLA
                # =============================================

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