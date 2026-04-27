# --- Inicializar estado ---
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.q_index = 0
    st.session_state.shuffled_questions = random.sample(questions, len(questions))
    st.session_state.options_order = {}

# --- Mostrar pregunta ---
if st.session_state.q_index < len(questions):
    q = st.session_state.shuffled_questions[st.session_state.q_index]

    st.image(q["image"], use_column_width=True)
    st.subheader(f"Pregunta {st.session_state.q_index + 1}")
    st.write(q["question"])

    # ✅ Generar opciones solo UNA vez por pregunta
    if st.session_state.q_index not in st.session_state.options_order:
        st.session_state.options_order[st.session_state.q_index] = random.sample(
            q["options"], len(q["options"])
        )

    options = st.session_state.options_order[st.session_state.q_index]

    selected = st.radio(
        "Elige una opción:",
        options,
        key=f"q_{st.session_state.q_index}"
    )

    if st.button("Responder"):
        if selected == q["answer"]:
            st.success("✅ ¡Correcto!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrecto. Era: {q['answer']}")

        st.session_state.q_index += 1
        st.rerun()
