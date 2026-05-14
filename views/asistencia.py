import streamlit as st

from sqlalchemy import text
from utils.db import get_connection
from pathlib import Path
import base64


# =========================================================
# RENDER ASISTENCIA
# =========================================================

def render_asistencia():

    st.markdown("""
    <style>

    html,
    body,
    [class*="css"] {
        overflow-x: hidden !important;
    }

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

    section[data-testid="stSidebar"] {
        display: none !important;
    }

    .block-container {
        max-width: 680px !important;
        padding-top: 2rem !important;
        padding-left: 1.2rem !important;
        padding-right: 1.2rem !important;
        padding-bottom: 170px !important;
        margin: auto !important;
    }

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

    .stButton {
        margin-top: 20px !important;
        margin-bottom: 40px !important;
    }

    .stButton button {
        border-radius: 16px !important;
        height: 52px !important;
        font-weight: 700 !important;
        background: linear-gradient(135deg, #16a34a, #22c55e) !important;
        border: none !important;
        color: white !important;
    }

    .stTextInput input {
        border-radius: 14px !important;
        border: 1px solid #dbe4ee !important;
        padding: 14px !important;
    }

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

        st.error("❌ No se recibió el ID de la formación.")
        st.info("Ingrese desde el enlace generado.")
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
                        formador,
                        tipo_registro,

                        pregunta_1,
                        p1_opcion_a,
                        p1_opcion_b,
                        p1_opcion_c,
                        p1_opcion_d,
                        p1_correcta,

                        pregunta_2,
                        p2_opcion_a,
                        p2_opcion_b,
                        p2_opcion_c,
                        p2_opcion_d,
                        p2_correcta,

                        pregunta_3,
                        p3_opcion_a,
                        p3_opcion_b,
                        p3_opcion_c,
                        p3_opcion_d,
                        p3_correcta,

                        pregunta_4,
                        p4_opcion_a,
                        p4_opcion_b,
                        p4_opcion_c,
                        p4_opcion_d,
                        p4_correcta,

                        pregunta_5,
                        p5_opcion_a,
                        p5_opcion_b,
                        p5_opcion_c,
                        p5_opcion_d,
                        p5_correcta
                    FROM formaciones
                    WHERE id = :id
                """),
                {
                    "id": int(id_formacion)
                }
            ).fetchone()

    except Exception:

        st.error("⚠️ No fue posible conectar con el sistema.")
        st.stop()

    if not formacion:

        st.error("❌ Formación no encontrada.")
        st.stop()

    # =========================================================
    # VARIABLES FORMACIÓN
    # =========================================================

    id_formacion = formacion[0]
    nombre_formacion = formacion[1]
    fecha_asistencia = formacion[2]
    formador = formacion[3]
    tipo_registro = formacion[4] or "Charla"

    preguntas = [
        {
            "numero": 1,
            "pregunta": formacion[5],
            "opciones": {
                "A": formacion[6],
                "B": formacion[7],
                "C": formacion[8],
                "D": formacion[9],
            },
            "correcta": formacion[10],
        },
        {
            "numero": 2,
            "pregunta": formacion[11],
            "opciones": {
                "A": formacion[12],
                "B": formacion[13],
                "C": formacion[14],
                "D": formacion[15],
            },
            "correcta": formacion[16],
        },
        {
            "numero": 3,
            "pregunta": formacion[17],
            "opciones": {
                "A": formacion[18],
                "B": formacion[19],
                "C": formacion[20],
                "D": formacion[21],
            },
            "correcta": formacion[22],
        },
        {
            "numero": 4,
            "pregunta": formacion[23],
            "opciones": {
                "A": formacion[24],
                "B": formacion[25],
                "C": formacion[26],
                "D": formacion[27],
            },
            "correcta": formacion[28],
        },
        {
            "numero": 5,
            "pregunta": formacion[29],
            "opciones": {
                "A": formacion[30],
                "B": formacion[31],
                "C": formacion[32],
                "D": formacion[33],
            },
            "correcta": formacion[34],
        },
    ]

    # =========================================================
    # HEADER
    # =========================================================

    logo_path = Path("assets/logo_elite_sin_fondo.png")

    if logo_path.exists():

        logo_base64 = base64.b64encode(
            logo_path.read_bytes()
        ).decode()

        st.markdown(
            f"""
            <div style="text-align:center; margin-bottom:12px;">
                <img src="data:image/png;base64,{logo_base64}" style="width:150px;">
            </div>
            """,
            unsafe_allow_html=True
        )

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

    cedula = st.text_input("Digite su cédula")

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

            st.error("⚠️ No fue posible consultar la información.")
            st.stop()

        if empleado:

            nombre_completo = empleado[0]
            cargo = empleado[1]
            proyecto = empleado[2]
            zona = empleado[3]

            st.success("✅ Empleado encontrado")

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

            st.error("❌ Cédula no encontrada.")

    # =========================================================
    # FORMULARIO
    # =========================================================

    clasificacion = st.radio(
        "Clasificación de formación",
        [
            "Charla",
            "Capacitación"
        ],
        index=0 if tipo_registro == "Charla" else 1
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
    # EVALUACIÓN CAPACITACIÓN
    # =========================================================

    respuesta_1 = None
    respuesta_2 = None
    respuesta_3 = None
    respuesta_4 = None
    respuesta_5 = None

    resultado_1 = None
    resultado_2 = None
    resultado_3 = None
    resultado_4 = None
    resultado_5 = None

    puntaje = 0

    respuestas = {}

    if tipo_registro == "Capacitación":

        st.markdown("### 📝 Evaluación de la capacitación")

        for item in preguntas:

            numero = item["numero"]
            pregunta = item["pregunta"]
            correcta = item["correcta"]

            opciones_validas = []

            for letra, texto_opcion in item["opciones"].items():

                if texto_opcion:

                    opciones_validas.append(
                        f"{letra}. {texto_opcion}"
                    )

            if pregunta and opciones_validas:

                respuesta = st.radio(
                    f"{numero}. {pregunta}",
                    opciones_validas,
                    key=f"respuesta_{numero}"
                )

                letra_respuesta = respuesta.split(".")[0]

                resultado = (
                    "Correcta"
                    if letra_respuesta == correcta
                    else "Incorrecta"
                )

                respuestas[numero] = {
                    "respuesta": respuesta,
                    "resultado": resultado
                }

        respuesta_1 = respuestas.get(1, {}).get("respuesta")
        respuesta_2 = respuestas.get(2, {}).get("respuesta")
        respuesta_3 = respuestas.get(3, {}).get("respuesta")
        respuesta_4 = respuestas.get(4, {}).get("respuesta")
        respuesta_5 = respuestas.get(5, {}).get("respuesta")

        resultado_1 = respuestas.get(1, {}).get("resultado")
        resultado_2 = respuestas.get(2, {}).get("resultado")
        resultado_3 = respuestas.get(3, {}).get("resultado")
        resultado_4 = respuestas.get(4, {}).get("resultado")
        resultado_5 = respuestas.get(5, {}).get("resultado")

        puntaje = sum(
            1
            for item in respuestas.values()
            if item.get("resultado") == "Correcta"
        )

    # =========================================================
    # GUARDAR
    # =========================================================

    if st.button(
        "Enviar asistencia",
        use_container_width=True
    ):

        if not cedula:

            st.warning("⚠️ Debe ingresar la cédula.")

        elif not empleado:

            st.error("❌ La cédula no existe o está inactiva.")

        elif autoriza_datos == "No":

            st.warning("⚠️ Debe autorizar el tratamiento de datos.")

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
                                autoriza_datos,
                                respuesta_1,
                                respuesta_2,
                                respuesta_3,
                                respuesta_4,
                                respuesta_5,
                                resultado_1,
                                resultado_2,
                                resultado_3,
                                resultado_4,
                                resultado_5,
                                puntaje
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
                                :autoriza_datos,
                                :respuesta_1,
                                :respuesta_2,
                                :respuesta_3,
                                :respuesta_4,
                                :respuesta_5,
                                :resultado_1,
                                :resultado_2,
                                :resultado_3,
                                :resultado_4,
                                :resultado_5,
                                :puntaje
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
                            "autoriza_datos": autoriza_datos,
                            "respuesta_1": respuesta_1,
                            "respuesta_2": respuesta_2,
                            "respuesta_3": respuesta_3,
                            "respuesta_4": respuesta_4,
                            "respuesta_5": respuesta_5,
                            "resultado_1": resultado_1,
                            "resultado_2": resultado_2,
                            "resultado_3": resultado_3,
                            "resultado_4": resultado_4,
                            "resultado_5": resultado_5,
                            "puntaje": puntaje
                        }
                    )

                    conn.commit()

                st.success("✅ Asistencia registrada correctamente.")

            except Exception as e:

                if (
                    "unique" in str(e).lower()
                    or
                    "duplicate" in str(e).lower()
                ):

                    st.warning("⚠️ Esta cédula ya registró asistencia.")

                else:

                    st.error("⚠️ No fue posible registrar la asistencia.")

            st.markdown(
                "<br><br><br><br>",
                unsafe_allow_html=True
            )