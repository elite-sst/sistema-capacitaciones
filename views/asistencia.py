import streamlit as st

from sqlalchemy import text
from utils.db import get_connection


# =========================================================
# RENDER ASISTENCIA
# =========================================================

def render_asistencia():

    # =========================================================
    # CSS FORMULARIO
    # =========================================================

    st.markdown("""
    <style>

    html,
    body,
    [class*="css"] {

        overflow-x: hidden !important;
    }

    /* =====================================================
       OCULTAR ELEMENTOS STREAMLIT
    ===================================================== */

    #MainMenu,
    footer,
    header,
    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"],
    .stDeployButton {

        display: none !important;

        visibility: hidden !important;

        height: 0 !important;
    }

    /* =====================================================
       SIDEBAR
    ===================================================== */

    section[data-testid="stSidebar"] {

        display: none !important;
    }

    /* =====================================================
       CONTENEDOR
    ===================================================== */

    .block-container {

        max-width: 680px !important;

        padding-top: 2rem !important;

        padding-left: 1.2rem !important;

        padding-right: 1.2rem !important;

        padding-bottom: 170px !important;

        margin: auto !important;
    }

    /* =====================================================
       TITULOS
    ===================================================== */

    .titulo-principal {

        text-align: center;

        font-size: 27px;

        font-weight: 800;

        line-height: 1.15;

        margin-bottom: 24px;

        color: #1e293b !important;
    }

    .titulo-formacion {

        text-align: center;

        font-size: 22px;

        font-weight: 800;

        line-height: 1.2;

        margin-bottom: 8px;

        color: #1e293b !important;
    }

    .info-formacion {

        text-align: center;

        font-size: 14px;

        margin-bottom: 8px;

        color: #1e293b !important;
    }

    /* =====================================================
       BOTÓN
    ===================================================== */

    .stButton {

        margin-top: 20px !important;

        margin-bottom: 40px !important;
    }

    .stButton button {

        border-radius: 16px !important;

        height: 52px !important;

        font-weight: 700 !important;

        background:
            linear-gradient(
                135deg,
                #16a34a,
                #22c55e
            ) !important;

        border: none !important;

        color: white !important;
    }

    /* =====================================================
       INPUTS
    ===================================================== */

    .stTextInput input {

        border-radius: 14px !important;

        border:
            1px solid #dbe4ee !important;

        padding: 14px !important;
    }

    /* =====================================================
       MOBILE
    ===================================================== */

    @media (max-width: 600px) {

        .block-container {

            max-width: 100% !important;

            padding-top: 1.5rem !important;

            padding-left: 1rem !important;

            padding-right: 1rem !important;

            padding-bottom: 220px !important;
        }

        .titulo-principal {

            font-size: 27px !important;
        }

        .titulo-formacion {

            font-size: 22px !important;
        }

        .info-formacion {

            font-size: 14px !important;
        }
    }

    </style>
    """, unsafe_allow_html=True)

    # =========================================================
    # QUERY PARAMS
    # =========================================================

    params = st.query_params

    id_formacion = params.get("formacion")

    if not id_formacion:

        st.error(
            "❌ No se recibió el ID de la formación."
        )

        st.info(
            "Ingrese desde el enlace generado."
        )

        st.stop()

    # =========================================================
    # CONSULTAR FORMACIÓN
    # =========================================================

    try:

        with get_connection() as conn:

            formacion = conn.execute(
                text("""
                    SELECT
                        id,
                        nombre_formacion,
                        fecha_asistencia,
                        formador
                    FROM formaciones
                    WHERE id = :id
                """),
                {
                    "id": int(id_formacion)
                }
            ).fetchone()

    except Exception:

        st.error("""
        ⚠️ No fue posible conectar con el sistema.
        """)

        st.stop()

    if not formacion:

        st.error(
            "❌ Formación no encontrada."
        )

        st.stop()

    # =========================================================
    # VARIABLES
    # =========================================================

    id_formacion = formacion[0]

    nombre_formacion = formacion[1]

    fecha_asistencia = formacion[2]

    formador = formacion[3]

    # =========================================================
    # HEADER
    # =========================================================

    st.markdown(
        """
        <div class="titulo-principal">
            📋 Registro de Asistencia
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="titulo-formacion">
            📚 {nombre_formacion}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="info-formacion">
            📅 Fecha: <b>{fecha_asistencia}</b>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="info-formacion">
            👨‍🏫 Formador: <b>{formador}</b>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # =========================================================
    # CONSULTA EMPLEADO
    # =========================================================

    cedula = st.text_input(
        "Digite su cédula"
    )

    empleado = None

    if cedula:

        try:

            with get_connection() as conn:

                empleado = conn.execute(
                    text("""
                        SELECT
                            nombre_completo,
                            cargo,
                            proyecto,
                            zona
                        FROM empleados
                        WHERE cedula = :cedula
                        AND estado = 'ACTIVO'
                    """),
                    {
                        "cedula": cedula.strip()
                    }
                ).fetchone()

        except Exception:

            st.error("""
            ⚠️ No fue posible consultar la información.
            """)

            st.stop()

        if empleado:

            nombre_completo = empleado[0]

            cargo = empleado[1]

            proyecto = empleado[2]

            zona = empleado[3]

            st.success(
                "✅ Empleado encontrado"
            )

            st.text_input(
                "Nombre completo",
                value=nombre_completo,
                disabled=True
            )

            st.text_input(
                "Cargo",
                value=cargo,
                disabled=True
            )

            st.text_input(
                "Proyecto",
                value=proyecto,
                disabled=True
            )

            st.text_input(
                "Zona",
                value=zona or "",
                disabled=True
            )

        else:

            st.error(
                "❌ Cédula no encontrada."
            )

    # =========================================================
    # FORMULARIO
    # =========================================================

    clasificacion = st.radio(
        "Clasificación de formación",
        [
            "Charla",
            "Capacitación"
        ]
    )

    tipo_formacion = st.radio(
        "Tipo de formación",
        [
            "Interna",
            "Externa"
        ]
    )

    autoriza_datos = st.radio(
        "¿Autoriza el tratamiento de datos?",
        [
            "Sí",
            "No"
        ]
    )

    # =========================================================
    # GUARDAR
    # =========================================================

    if st.button(
        "Enviar asistencia",
        use_container_width=True
    ):

        if not cedula:

            st.warning(
                "⚠️ Debe ingresar la cédula."
            )

        elif not empleado:

            st.error("""
            ❌ La cédula no existe o está inactiva.
            """)

        else:

            try:

                with get_connection() as conn:

                    conn.execute(
                        text("""
                            INSERT INTO asistencias (
                                id_formacion,
                                cedula,
                                nombre_completo,
                                cargo,
                                proyecto,
                                zona,
                                formador,
                                clasificacion_formacion,
                                tipo_formacion,
                                autoriza_datos
                            )
                            VALUES (
                                :id_formacion,
                                :cedula,
                                :nombre_completo,
                                :cargo,
                                :proyecto,
                                :zona,
                                :formador,
                                :clasificacion_formacion,
                                :tipo_formacion,
                                :autoriza_datos
                            )
                        """),
                        {
                            "id_formacion": id_formacion,
                            "cedula": cedula.strip(),
                            "nombre_completo": nombre_completo,
                            "cargo": cargo,
                            "proyecto": proyecto,
                            "zona": zona,
                            "formador": formador,
                            "clasificacion_formacion": clasificacion,
                            "tipo_formacion": tipo_formacion,
                            "autoriza_datos": autoriza_datos
                        }
                    )

                    conn.commit()

                st.success(
                    "✅ Asistencia registrada correctamente."
                )

            except Exception as e:

                if (
                    "unique" in str(e).lower()
                    or
                    "duplicate" in str(e).lower()
                ):

                    st.warning("""
                    ⚠️ Esta cédula ya registró asistencia.
                    """)

                else:

                    st.error("""
                    ⚠️ No fue posible registrar la asistencia.
                    """)

            st.markdown(
                "<br><br><br><br>",
                unsafe_allow_html=True
            )