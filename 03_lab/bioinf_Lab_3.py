from functools import wraps
import time


def measure_time(func):
    @wraps(func)
    def measure_time_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        finish_time = time.perf_counter()
        total_time = finish_time - start_time
        print(f"Выполнение функции {func.__name__} заняло {total_time:.7f} секунд")
        return result

    return measure_time_wrapper


@measure_time
def dist_full_matrix(S1, S2):
    m, n = len(S1), len(S2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif S1[i - 1] == S2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]


@measure_time
def dist_short_matrix(S1, S2):
    m, n = len(S1), len(S2)
    if m < n:
        S1, S2 = S2, S1
        m, n = n, m

    prev_row = list(range(n + 1))
    curr_row = [0] * (n + 1)

    for i in range(1, m + 1):
        curr_row[0] = i
        for j in range(1, n + 1):
            if S1[i - 1] == S2[j - 1]:
                curr_row[j] = prev_row[j - 1]
            else:
                curr_row[j] = 1 + min(prev_row[j], curr_row[j - 1], prev_row[j - 1])
        prev_row, curr_row = curr_row, prev_row

    return prev_row[n]


GarlicVirusA = "ATGATTCCTCAAGACTTTAATATCCTTTGCTGCCTACACTTTGCCAAACCCTTCATCCCTCAAGACCTCAAAGCTCATCTCTTCTTCACTTGCGTCAATGAATGTAAATTAGTAAGAATAGCTAGTCAAAATAAGCCATTTCTAGGCACTTCTAAGTGTGCTCAGCGCCGTAGAGCGAAACGCTATAATAGGTGTTTCGAGTGCGGTGCCTACTTACTAGATAACCATGAATGTAGAATCTTTGTATCACGTGCTCAATCGGATGTGCTAGCCGTCATACACGAGGGACCCGTTAAGCTACATGCTGAAAGGACCTACAGGCCAAATTCTGACGCTGCGCTGCTCATTGAGAGTGATCTACAGTACATCAAACTTTTCCAAAATCGTAAGGCTTGA"
GarlicVirusB = "TGGGCTTGTTACCACAATGGATCATCAAAGTTTACGACTTTGACCACGGACGCTCCCTGCGGCATGCCTCATGCGGAACTCAAGGACTTAGTTGAGGATTTCTGCACGTTGAGACAATTTTGCGGATTTTATGCCAAAACTTGTTATGTAACGGGCAAACAGCAGAATAAGCCTCCTGCAAACTGGTCGAGTAAAGGATTCCAAGAAGAATCAAAATTTTCGGCGTTTGACTTCTTCAATGCTGTGCTTAGCGACTCTTCTCCCGCCCCCCCTGGAGGAATGCGTTTCAAACCAACACAAGATGAAATTTTAGGTCATTCTTTGAACGCCAAAATGTCTATAATTGAATCACGCAAGGCCTCA"


def main():
    d1 = dist_full_matrix(GarlicVirusA, GarlicVirusB)
    d2 = dist_short_matrix(GarlicVirusA, GarlicVirusB)
    assert d1 == d2
    print(
        f"Редакционное расстояние между последовательностями GarlicVirusA и GarlicVirusB: {d1}."
    )


if __name__ == "__main__":
    main()
