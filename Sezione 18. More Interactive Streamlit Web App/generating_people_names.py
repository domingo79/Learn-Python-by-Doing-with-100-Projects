from generatore import genera_anagrafica
import streamlit as st


def genera_nomi(num):
    nomi = [genera_anagrafica()['nome'] for _ in range(num)]
    return nomi


st.title(":red[Random Name] :blue[Generator]")
input_number = st.number_input("Enter the number of names to generate:",
                               min_value=1, max_value=100, value=5, step=1)

if st.button("Generate"):
    nomi = genera_nomi(input_number)

    if len(nomi) == 1:
        st.subheader("Il nome generato è:", divider='rainbow')
    else:
        st.subheader("Ecco la lista dei nomi generati:", divider='rainbow')

    for nome in nomi:
        st.markdown(f"👤 {nome}")
