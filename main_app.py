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
    if st.button("Dataframe client", width='stretch'):
        show_client = True
with col2:
    if st.button("Dataframe vendeur", width='stretch'):
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
    if st.button('Visualisation graphique client', type='secondary', width='stretch'):
        plot_client = True
with col2:
    if st.button('Visualisation graphique vendeur', type='secondary', width='stretch'):
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

# Partie pour le modèle 3D
st.title('Visualisation de nos produits proposés pour Salomon')
layout = st.radio("Disposition des modèles :", ["Côte à côte", "L'un en dessous de l'autre"])

def render_model(path):
    return f"""
    <model-viewer src="{path}"
                  alt="Modèle 3D"
                  auto-rotate
                  camera-controls
                  style="width: 100t/model-viewer.min.js</script>
    """,
    height=0,



# Affichage selon le layout choisi
if layout == "Côte à côte":
    col1, col2 = st.columns(2)
    with col1:
        components.html(render_model("static/modele1.glb"), height=500)
    with col2:
        components.html(render_model("static/modele2.glb"), height=500)
else:
    components.html(render_model("static/modele1.glb"), height=500)
    components.html(render_model("static/modele2.glb"), height=500)
