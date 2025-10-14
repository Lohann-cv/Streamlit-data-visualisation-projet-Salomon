import streamlit as st
import dataset as ds
import visualization as vs
import streamlit.components.v1 as components

st.title('Visualisation des réponse du questionnaire')
st.markdown('Cette application web vous permet de visualiser les réponses du questionnaire Salomon de façon interactive et éstetique')
st.image('imagevideo/salomon.png')
st.button('Reset', type='secondary')
# Set up des deux colones et boutons pour les dataframe
col1, col2, col0 = st.columns(3)
with col1:
    if st.button("Dataframe client", width='stretch', type='primary'):
        show_client = True
with col2:
    if st.button("Diagrame de genre des personnes intérogée", type='primary'):
        show_gender = True
with col0:
    if st.button("Dataframe vendeur", width='stretch', type='primary'):
        show_sellers = True


try:
    if show_client:
        st.dataframe(ds.df_client)
except NameError:
    pass

try:
    if show_gender:
        vs.plot_gender()
        st.dataframe(ds.df_gender)
except NameError:
    pass

try:
    if show_sellers:
        st.dataframe(ds.df_sellers)
except NameError:
    pass

# Bouton pour la visualisation du graphique
col7, col8 = st.columns(2)
with col7:
    if st.button('Visualisation graphique client', type='primary', width='stretch'):
        plot_client = True
with col8:
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

col3, col4 = st.columns(2)
with col3:
    st.video('imagevideo/salomonEwan1.mp4')
    st.image('imagevideo/salomonEwan1.jpeg', caption='Chaussure de randonnée GorTex JRxSalomon')
    st.video('imagevideo/pullEwan.mp4')
with col4:
    st.image('imagevideo/vestetech.png', caption='Veste technique JRxSalomon')
    st.image('imagevideo/skiAn.jpeg', caption='Pantalon de ski Coreflow JRxSalomon')

st.subheader('Les produits streetwears')
col5, col6 = st.columns(2)
with col5:
    st.image('imagevideo/surchemiseA.jpeg', caption='Surchemise épaisse JRxSalomon')
with col6:
    st.image('imagevideo/tshirtA.jpeg', caption='T-shirt Coreflow JRxSalomon')