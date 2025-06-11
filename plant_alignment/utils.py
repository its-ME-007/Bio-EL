import matplotlib.pyplot as plt
import seaborn as sns

def plot_score_matrix(mat, seq1, seq2):
    plt.figure(figsize=(10, 8))
    sns.heatmap(mat, cmap="viridis", xticklabels=["-"] + list(seq2),
                yticklabels=["-"] + list(seq1), cbar_kws={'label': 'Score'})
    plt.xlabel("Sequence 2")
    plt.ylabel("Sequence 1")
    plt.title("Smith-Waterman Score Matrix")
    plt.tight_layout()
    return plt