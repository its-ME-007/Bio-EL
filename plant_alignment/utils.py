import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_score_matrix(mat, seq1, seq2):
    # Calculate appropriate figure size based on sequence lengths
    width = min(20, 8 + len(seq2) * 0.02)  # Cap maximum width
    height = min(20, 8 + len(seq1) * 0.02)  # Cap maximum height
    
    plt.figure(figsize=(width, height))
    
    # Create heatmap
    sns.heatmap(mat, cmap="viridis", cbar_kws={'label': 'Score'})
    
    # Add labels
    plt.xlabel("Sequence 2")
    plt.ylabel("Sequence 1")
    plt.title("Smith-Waterman Score Matrix")
    
    # Adjust tick labels to show fewer positions
    max_ticks = 20  # Maximum number of tick labels to show
    
    # Calculate tick positions and labels for sequence 1
    y_ticks = np.linspace(0, len(seq1), min(max_ticks, len(seq1) + 1), dtype=int)
    y_labels = ["-"] + [f"{i+1}" for i in y_ticks[1:]]
    plt.yticks(y_ticks, y_labels)
    
    # Calculate tick positions and labels for sequence 2
    x_ticks = np.linspace(0, len(seq2), min(max_ticks, len(seq2) + 1), dtype=int)
    x_labels = ["-"] + [f"{i+1}" for i in x_ticks[1:]]
    plt.xticks(x_ticks, x_labels)
    
    plt.tight_layout()
    return plt