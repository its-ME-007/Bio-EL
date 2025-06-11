import numpy as np

def smith_waterman(seq1, seq2, match=2, mismatch=-1, gap=-2):
    m, n = len(seq1), len(seq2)
    score = np.zeros((m+1, n+1), dtype=int)
    trace = np.full((m+1, n+1), '', dtype=str)

    max_score, max_pos = 0, (0, 0)

    for i in range(1, m+1):
        for j in range(1, n+1):
            diag = score[i-1, j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
            up = score[i-1, j] + gap
            left = score[i, j-1] + gap
            current = max(0, diag, up, left)
            score[i, j] = current

            if current == diag:
                trace[i, j] = '\\'
            elif current == up:
                trace[i, j] = '|'
            elif current == left:
                trace[i, j] = '-'

            if current > max_score:
                max_score, max_pos = current, (i, j)

    i, j = max_pos
    aligned1, aligned2 = "", ""
    while i > 0 and j > 0 and score[i, j] > 0:
        if trace[i, j] == '\\':
            aligned1 = seq1[i-1] + aligned1
            aligned2 = seq2[j-1] + aligned2
            i, j = i-1, j-1
        elif trace[i, j] == '|':
            aligned1 = seq1[i-1] + aligned1
            aligned2 = '-' + aligned2
            i -= 1
        else:
            aligned1 = '-' + aligned1
            aligned2 = seq2[j-1] + aligned2
            j -= 1

    return max_score, aligned1, aligned2, score