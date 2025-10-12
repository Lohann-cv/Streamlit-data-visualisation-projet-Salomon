import matplotlib.pyplot as plt
import dataset as ds
import streamlit as st

def plot_client():
    questions = ds.df_client.columns.tolist()
    oui_counts = [(ds.df_client[q].astype(str).str.lower() == "oui").sum() for q in questions]
    non_counts = [(ds.df_client[q].astype(str).str.lower() == "non").sum() for q in questions]

    x = range(len(questions))
    bar_width = 0.4
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar([i - bar_width/2 for i in x], oui_counts, width=bar_width, label='Oui', color='green')
    ax.bar([i + bar_width/2 for i in x], non_counts, width=bar_width, label='Non', color='red')
    ax.set_title("Réponses des clients")
    ax.set_xticks(x)
    ax.set_xticklabels(questions, rotation=45, ha='right')
    ax.set_ylabel("Nombre de réponses")
    ax.legend()
    st.pyplot(fig)


def plot_sellers():
    questions = ds.df_sellers.columns.tolist()
    oui_counts = [(ds.df_sellers[q].astype(str).str.lower() == "oui").sum() for q in questions]
    non_counts = [(ds.df_sellers[q].astype(str).str.lower() == "non").sum() for q in questions]

    x = range(len(questions))
    bar_width = 0.4
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar([i - bar_width/2 for i in x], oui_counts, width=bar_width, label='Oui', color='blue')
    ax.bar([i + bar_width/2 for i in x], non_counts, width=bar_width, label='Non', color='orange')
    ax.set_title("Réponses des vendeurs")
    ax.set_xticks(x)
    ax.set_xticklabels(questions, rotation=45, ha='right')
    ax.set_ylabel("Nombre de réponses")
    ax.legend()
    st.pyplot(fig)
