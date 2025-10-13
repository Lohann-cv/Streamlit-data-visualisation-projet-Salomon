import streamlit as st
import dataset as ds
import visualization as vs
import streamlit.components.v1 as components

st.title('Visualisation des réponse du questionnaire')
st.markdown('Cette application web vous permet de visualiser les réponses du questionnaire Salomon de façon interactive et éstetique')
st.image('image/salomon.png')

# Set up des deux colones et boutons pour les dataframe
col1, col2 = st.columns(2)
with col1:
    if st.button("Dataframe client", width='stretch', type='primary'):
        show_client = True
with col2:
    if st.button("Dataframe vendeur", width='stretch', type='primary'):
        show_sellers = True


try:
    if show_client:
        st.dataframe(ds.df_client)
except NameError:
    pass

try:
    if show_sellers:
        st.dataframe(ds.df_sellers)
except NameError:
    pass

# Bouton pour la visualisation du graphique
with col1:
    if st.button('Visualisation graphique client', type='primary', width='stretch'):
        plot_client = True
with col2:
    if st.button('Visualisation graphique vendeur', type='primary', width='stretch'):
        plot_sellers = True

try:
    if plot_client:
        vs.plot_client()
except NameError:
    pass

try:
    if plot_sellers:
        vs.plot_sellers()
except NameError:
    pass

# Partie 3D
st.title("Visualisation de modèles 3D Blender (.glb)")
layout = st.radio("Disposition des modèles :", ["Côte à côte", "L'un en dessous de l'autre"])

st.markdown("""
    https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js
""", unsafe_allow_html=True)

# Fonction affichage
def render_model(path):
    components.html(f"""
        {path}
        </model-viewer>
    """, height=500)

# Affichage selon la disposition choisie
if layout == "Côte à côte":
    col1, col2 = st.columns(2)
    with col1:
        render_model("static/modele1.glb")
    with col2:
        render_model("static/modele2.glb")
else:
    render_model("static/modele1.glb")
    render_model("static/modele2.glb")