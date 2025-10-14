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

st.title("Les produits de la capsule JR x Salomon")
st.subheader("Les poduit techwears")
with col1:
    st.video('pullEwan.mp4')
    st.image('skiAN;jpeg')
with col2:
    st.video('salomonEwan1.mp4')
    st.image('salomonEwan1.jpeg')

st.subheader('Les produits streetwears')
with col1:
    st.image('surchemiseA.jpeg')
with col2:
    st.image('tshirtA.jpeg')