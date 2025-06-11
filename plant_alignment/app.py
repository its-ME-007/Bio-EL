import streamlit as st
from align import smith_waterman
from utils import plot_score_matrix
from sequences import EcPT4_Ragi, Canein1_Sugarcane, Actin7_Rice

seqs = {
    "Ragi_EcPT4": EcPT4_Ragi,
    "Sugarcane_Canein1": Canein1_Sugarcane,
    "Rice_Actin7": Actin7_Rice
}

st.title("🧬 Plant Gene Local Alignment")
st.write("Smith-Waterman alignment for Ragi, Sugarcane & Rice genes")

seq1_name = st.selectbox("Sequence 1", list(seqs.keys()))
seq2_name = st.selectbox("Sequence 2", list(seqs.keys()))
seq1, seq2 = seqs[seq1_name], seqs[seq2_name]

if st.button("Run Smith-Waterman"):
    score, a1, a2, mat = smith_waterman(seq1, seq2)
    st.subheader(f"Alignment Score: {score}")
    st.code(f"{a1}\n{a2}", language="text")
    plt = plot_score_matrix(mat, seq1, seq2)
    st.pyplot(plt)