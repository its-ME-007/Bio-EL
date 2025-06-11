import streamlit as st
from align import smith_waterman
from utils import plot_score_matrix
from sequences import (
    Rice_Nipponbare_Actin, Rice_IR64_Rubisco, Rice_Douradao_Transporter,
    Sugarcane_LA_Purple_SuSy, Sugarcane_LA_Purple_Invertase,
    Ragi_ML365_DroughtStress, Ragi_PR202_Calcium_Binding, Ragi_ML365_Nutrient_Transporter
)

# Organize sequences by species
seqs = {
    "Rice": {
        "Nipponbare Actin": Rice_Nipponbare_Actin,
        "IR64 Rubisco": Rice_IR64_Rubisco,
        "Douradao Transporter": Rice_Douradao_Transporter
    },
    "Sugarcane": {
        "LA-Purple SuSy": Sugarcane_LA_Purple_SuSy,
        "LA-Purple Invertase": Sugarcane_LA_Purple_Invertase
    },
    "Ragi": {
        "ML365 Drought Stress": Ragi_ML365_DroughtStress,
        "PR202 Calcium Binding": Ragi_PR202_Calcium_Binding,
        "ML365 Nutrient Transporter": Ragi_ML365_Nutrient_Transporter
    }
}

st.title("🧬 Plant Gene Local Alignment")
st.write("Smith-Waterman alignment for Rice, Sugarcane & Ragi genes")

# Create two columns for sequence selection
col1, col2 = st.columns(2)

with col1:
    species1 = st.selectbox("Species 1", list(seqs.keys()))
    seq1_name = st.selectbox("Sequence 1", list(seqs[species1].keys()))
    seq1 = seqs[species1][seq1_name]

with col2:
    species2 = st.selectbox("Species 2", list(seqs.keys()))
    seq2_name = st.selectbox("Sequence 2", list(seqs[species2].keys()))
    seq2 = seqs[species2][seq2_name]

if st.button("Run Smith-Waterman"):
    score, a1, a2, mat = smith_waterman(seq1, seq2)
    st.subheader(f"Alignment Score: {score}")
    st.code(f"{a1}\n{a2}", language="text")
    plt = plot_score_matrix(mat, seq1, seq2)
    st.pyplot(plt)