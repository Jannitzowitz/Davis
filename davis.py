import streamlit as st

# Titel der App
st.title("Handy App")

# --- Leinwand ---
st.subheader("Leinwand-Einstellungen")
leinwand_check = st.checkbox("Leinwand aktiv")
leinwand_auswahl = st.selectbox("Leinwand:", ["A5", "A4", "A3"], index=1) # A4 als Standard

# --- Style ---
st.subheader("Style-Auswahl")
style_auswahl = st.selectbox("Style:", ["Schwarz-Weiß"])

# --- Pinselstärke ---
st.subheader("Pinselstärke")
pinsel_staerke = st.slider("Stärke wählen:", 1, 20, 5)

# --- Button zum Berechnen/Ausgeben ---
if st.button("Ausführen"):
    st.write("---")
    st.write("### Aktuelle Werte:")
    st.write(f"Checkbox Leinwand: {leinwand_check}")
    st.write(f"Ausgewählte Leinwand: {leinwand_auswahl}")
    st.write(f"Style: {style_auswahl}")
    st.write(f"Pinselstärke: {pinsel_staerke}")