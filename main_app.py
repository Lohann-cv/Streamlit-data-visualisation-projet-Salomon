import streamlit as st
import dataset as ds
import visualization as vs

st.title('Visualisation des réponse du questionnaire')
st.markdown('Cette application web vous permet de visualiser les réponses du questionnaire Salomon de façon interactive et éstetique')

st.image('image/salomon.png')
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