REPLACEMENT_MATRIX = [
    [1, -5, -5, -1],
    [-5, 1, -1, -5],
    [-5, -1, 1, -5],
    [-1, -5, -5, 1],
]

SPACE_PENALTY = -2

NUCLEO = "ATGC"

GarlicVirusA = "ATGATTCCTCAAGACTTTAATATCCTTTGCTGCCTACACTTTGCCAAACCCTTCATCCCTCAAGACCTCAAAGCTCATCTCTTCTTCACTTGCGTCAATGAATGTAAATTAGTAAGAATAGCTAGTCAAAATAAGCCATTTCTAGGCACTTCTAAGTGTGCTCAGCGCCGTAGAGCGAAACGCTATAATAGGTGTTTCGAGTGCGGTGCCTACTTACTAGATAACCATGAATGTAGAATCTTTGTATCACGTGCTCAATCGGATGTGCTAGCCGTCATACACGAGGGACCCGTTAAGCTACATGCTGAAAGGACCTACAGGCCAAATTCTGACGCTGCGCTGCTCATTGAGAGTGATCTACAGTACATCAAACTTTTCCAAAATCGTAAGGCTTGA"
GarlicVirusB = "TGGGCTTGTTACCACAATGGATCATCAAAGTTTACGACTTTGACCACGGACGCTCCCTGCGGCATGCCTCATGCGGAACTCAAGGACTTAGTTGAGGATTTCTGCACGTTGAGACAATTTTGCGGATTTTATGCCAAAACTTGTTATGTAACGGGCAAACAGCAGAATAAGCCTCCTGCAAACTGGTCGAGTAAAGGATTCCAAGAAGAATCAAAATTTTCGGCGTTTGACTTCTTCAATGCTGTGCTTAGCGACTCTTCTCCCGCCCCCCCTGGAGGAATGCGTTTCAAACCAACACAAGATGAAATTTTAGGTCATTCTTTGAACGCCAAAATGTCTATAATTGAATCACGCAAGGCCTCA"


def print_matrix_pretty(matrix, n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print(matrix[i][j], end="\t")
        print("\n")


def smith_waterman(V, W, matrix, g):
    n, m = len(V), len(W)
    M = [[0] * (m + 1) for _ in range(n + 1)]
    way = [[0] * (m + 1) for _ in range(n + 1)]
    max_value = 0
    max_ind = (0, 0)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            matched = (
                M[i - 1][j - 1] + matrix[NUCLEO.index(V[i - 1])][NUCLEO.index(W[j - 1])]
            )
            deleted = M[i - 1][j] + g
            inserted = M[i][j - 1] + g

            M[i][j] = max(matched, deleted, inserted, 0)
            if M[i][j] == matched:
                way[i][j] = 1
            elif M[i][j] == deleted:
                way[i][j] = 2
            elif M[i][j] == inserted:
                way[i][j] = 3

            if M[i][j] > max_value:
                max_value = M[i][j]
                max_ind = (i, j)

    v_aligned, w_aligned = "", ""
    i, j = max_ind

    while M[i][j] > 0:
        if way[i][j] == 1:  # Диагональ
            v_aligned = V[i - 1] + v_aligned
            w_aligned = W[j - 1] + w_aligned
            i, j = i - 1, j - 1
        elif way[i][j] == 2:  # Вверх
            v_aligned = V[i - 1] + v_aligned
            w_aligned = "-" + w_aligned
            i -= 1
        elif way[i][j] == 3:  # Влево
            v_aligned = "-" + v_aligned
            w_aligned = W[j - 1] + w_aligned
            j -= 1

    return max_value, v_aligned, w_aligned


def needleman_wunsch(V, W, matrix, g):
    n, m = len(V), len(W)
    M = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        M[i][0] = i * g
    for j in range(m + 1):
        M[0][j] = j * g

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            matched = (
                M[i - 1][j - 1] + matrix[NUCLEO.index(V[i - 1])][NUCLEO.index(W[j - 1])]
            )
            deleted = M[i - 1][j] + g
            inserted = M[i][j - 1] + g

            M[i][j] = M[i][j] = max(matched, deleted, inserted)

    v_aligned, w_aligned = "", ""
    i, j = n, m
    while i > 0 or j > 0:
        if (
            i > 0
            and j > 0
            and M[i][j]
            == M[i - 1][j - 1] + matrix[NUCLEO.index(V[i - 1])][NUCLEO.index(W[j - 1])]
        ):
            v_aligned = V[i - 1] + v_aligned
            w_aligned = W[j - 1] + w_aligned
            i -= 1
            j -= 1
        elif i > 0 and M[i][j] == M[i - 1][j] + g:
            v_aligned = V[i - 1] + v_aligned
            w_aligned = "-" + w_aligned
            i -= 1
        else:
            v_aligned = "-" + v_aligned
            w_aligned = W[j - 1] + w_aligned
            j -= 1

    return M[n][m], v_aligned, w_aligned


def main():
    test_matrix = [
        [2, -3, -3, -3],
        [-3, 2, -3, -3],
        [-3, -3, 2, -3],
        [-3, -3, -3, 2],
    ]
    print(
        f'Глобальное выравнивание по алгоритму Нидлмана-Вунша:{needleman_wunsch(
        V="ACTGATTCA", W="ACGCATCA", matrix=test_matrix, g=-2
    )}'
    )
    print(
        f'Локальное выравнивание по алгоритму Смита–Ватермана:{smith_waterman(
            V="ATGCATCCCATGAC", W="TCTATATCCGT", matrix=test_matrix, g=-2
    )}'
    )

    print(
        f"Локальное выравнивание по алгоритму Смита–Ватермана:{smith_waterman(
        GarlicVirusA, GarlicVirusB, REPLACEMENT_MATRIX, g=-2
    )}"
    )
    print(
        f"Глобальное выравнивание по алгоритму Нидлмана-Вунша:{needleman_wunsch(
        GarlicVirusA, GarlicVirusB, REPLACEMENT_MATRIX, g=-2
    )}"
    )


if __name__ == "__main__":
    main()
