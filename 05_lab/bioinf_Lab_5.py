Motifs_kim_6 = [
    "CAGCAAGGGG",
    "GATATCCGCC",
    "TCTATAATCA",
    "ATCACCTTCC",
    "ACTAATTGCC",
    "TTCCTTAACA",
    "CTGGGAATTA",
    "ACAATTTTAC",
    "ATGAGATTTG",
    "GGTGGGGACA",
    "CAGAGCTAAA",
    "CTATATCAAC",
]

Motifs_test = [
    "TAGATCTGAA",
    "TGGATCCGAA",
    "TAGACCCGAA",
    "TAAATCCGAA",
    "TAGGTCCAAA",
    "TAGATTCGAA",
    "CAGATCCGAA",
    "TAGATCCGTA",
    "TAGATCCAAA",
    "TCGATCCGAA",
]


def count_matrix(motifs, length):
    count = {"A": [0] * length, "C": [0] * length, "G": [0] * length, "T": [0] * length}
    for motif in motifs:
        for i in range(length):
            count[motif[i]][i] += 1
    return count


def consensus_seq(count, length):
    consensus = ""
    for i in range(length):
        max_count = 0
        max_nucl = ""
        for nucl in "ACGT":
            if count[nucl][i] > max_count:
                max_count = count[nucl][i]
                max_nucl = nucl
        consensus += max_nucl
    return consensus


def score(motifs, consensus):
    total_score = 0
    for motif in motifs:
        for i in range(len(consensus)):
            if motif[i] != consensus[i]:
                total_score += 1
    return total_score


def main():
    count_mtr = count_matrix(Motifs_kim_6, len(Motifs_kim_6[0]))
    consensus = consensus_seq(count_mtr, len(Motifs_kim_6[0]))
    res_score = score(Motifs_kim_6, consensus)

    print("Матрица числа вхождений каждого нуклеотида в каждой столбец матрицы мотива:")
    for nuc in "ACGT":
        print(nuc + ":", count_mtr[nuc])
    print("\nКонсенсусная последовательность:", consensus)
    print("Сумма числа непопулярных букв в матрице мотива:", res_score)


if __name__ == "__main__":
    main()
