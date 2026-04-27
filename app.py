import streamlit as st
import random

st.set_page_config(page_title="Trivia Villanas Disney", page_icon="👑")

# --- Base de preguntas ---
questions = [
    {
        "question": "¿Cómo se llama la villana de La Sirenita?",
        "options": ["Úrsula", "Maléfica", "Cruella", "Reina Grimhilde"],
        "answer": "Úrsula",
        "image": "https://upload.wikimedia.org/wikipedia/en/3/3f/UrsulaTheLittleMermaid.png"
    },
    {
        "question": "¿Quién es la villana de 101 Dálmatas?",
        "options": ["Cruella de Vil", "Maléfica", "Gothel", "Yzma"],
        "answer": "Cruella de Vil",
        "image": "https://upload.wikimedia.org/wikipedia/en/5/56/Cruella_de_Vil.png"
    },
    {
        "question": "¿Qué villana se transforma en dragón?",
        "options": ["Maléfica", "Úrsula", "Reina Malvada", "Madre Gothel"],
        "answer": "Maléfica",
        "image": "https://upload.wikimedia.org/wikipedia/en/5/5d/Maleficent_Disney.png"
    },
    {
        "question": "¿Quién es la villana de Enredados?",
        "options": ["Madre Gothel", "Úrsula", "Cruella", "Yzma"],
        "answer": "Madre Gothel",
        "image": "https://upload.wikimedia.org/wikipedia/en/3/3c/Mother_Gothel.png"
    },
    {
        "question": "¿Cuál es la villana de Blancanieves?",
        "options": ["Reina Malvada", "Maléfica", "Cruella", "Úrsula"],
        "answer": "Reina Malvada",
        "image": "https://upload.wikimedia.org/wikipedia/en/6/6f/Evil_Queen_Snow_White_Disney.png"
    },
    {
        "question": "¿Qué villana usa un abrigo de piel?",
        "options": ["Cruella de Vil", "Úrsula", "Gothel", "Maléfica"],
        "answer": "Cruella de Vil",
        "image": "https://upload.wikimedia.org/wikipedia/en/5/56/Cruella_de_Vil.png"
    },
    {
        "question": "¿Quién es la villana de Kuzco?",
        "options": ["Yzma", "Cruella", "Maléfica", "Gothel"],
        "answer": "Yzma",
        "image": "https://upload.wikimedia.org/wikipedia/en/3/3d/Yzma.png"
    },
    {
        "question": "¿Qué villana roba la voz de Ariel?",
        "options": ["Úrsula", "Maléfica", "Cruella", "Reina Malvada"],
        "answer": "Úrsula",
        "image": "https://upload.wikimedia.org/wikipedia/en/3/3f/UrsulaTheLittleMermaid.png"
    },
    {
        "question": "¿Qué villana está obsesionada con la juventud?",
        "options": ["Madre Gothel", "Úrsula", "Cruella", "Yzma"],
        "answer": "Madre Gothel",
        "image": "https://upload.wikimedia.org/wikipedia/en/3/3c/Mother_Gothel.png"
    },
    {
        "question": "¿Qué villana consulta un espejo mágico?",
        "options": ["Reina Malvada", "Maléfica", "Cruella", "Gothel"],
        "answer": "Reina Malvada",
        "image": "https://upload.wikimedia.org/wikipedia/en/6/6f/Evil_Queen_Snow_White_Disney.png"
    }
]

# --- Inicializar estado ---
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.q_index = 0
    st.session_state.shuffled_questions = random.sample(questions, len(questions))

st.title("👑 Trivia de Villanas Disney")

# --- Mostrar pregunta ---
if st.session_state.q_index < len(questions):
    q = st.session_state.shuffled_questions[st.session_state.q_index]

    st.image(q["image"], use_column_width=True)
    st.subheader(f"Pregunta {st.session_state.q_index + 1}")
    st.write(q["question"])

    # Mezclar alternativas cada vez
    options = random.sample(q["options"], len(q["options"]))

    selected = st.radio("Elige una opción:", options, key=st.session_state.q_index)

    if st.button("Responder"):
        if selected == q["answer"]:
            st.success("✅ ¡Correcto!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrecto. Era: {q['answer']}")

        st.session_state.q_index += 1
        st.rerun()

# --- Resultado final ---
else:
    st.subheader(f"🎯 Puntaje final: {st.session_state.score}/10")

    if st.session_state.score == 10:
        st.balloons()
        st.success("🔥 ¡Perfecto! ¡Eres experta en villanas Disney!")
    else:
        st.info("💡 Inténtalo otra vez para lograr el puntaje perfecto")

    if st.button("Jugar de nuevo"):
        st.session_state.score = 0
        st.session_state.q_index = 0
        st.session_state.shuffled_questions = random.sample(questions, len(questions))
        st.rerun()
