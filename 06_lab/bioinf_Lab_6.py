test_text_1 = "ACAACTATGCATACTATCGGGAACTATCCT"
test_pattern = "ACTAT"
test_text_2 = "CGATATATCCATAG"
test_k_2 = 3
test_text_3 = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
test_k_3 = 4

text_kim_6 = "TATCCACTGACCAGCTATGAGGTCATACATCGTCATAGCACCAACTGTTAATTAAATTAAAAAGGAAATAAAAATGTTTAAACGTAAATCTACTGCTGAACTCGCTGCACAAATGGCTAAACTGGCTGGAAATAAAGGTGGTTTTTCTTCTGAAGATAAAGGCGAGTGGAAACTGAAACTCGACAATGCGGGTAACGGTCAAGCAGTAATTCGTTTTCTTCCGTCTAAAAATGATGAACAAGCACCATTTGCAATTCTTGTAAATCACGGTTTCAAGAAAAACGGTAAATGGTATATCGAAAATTGCTCATCTACCCACGGTGATTACGATTCTTGTCCAGTATGTCAGTACATCAGTAAAAATGATTTGTACAACACTGACAATAAAGAGTACGGTCTTGTTAAACGTAAAA"


def pattern_count(text, pattern):
    count = 0
    k = len(pattern)
    for i in range(abs(len(text) - k + 1)):
        if text[i : (i + k)] == pattern:
            count += 1
    return count


def count_dict(text, k):
    count_dict = {}
    text_length = len(text)
    for i in range(text_length - k + 1):
        pattern = text[i : i + k]
        count_dict[i] = pattern_count(text, pattern)
    return count_dict


def frequent_words(text, k):
    frequent_patterns = set()
    count = count_dict(text, k)
    max_count = max(count.values())

    for i in range(len(text) - k + 1):
        if count[i] == max_count:
            frequent_patterns.add(text[i : (i + k)])

    return frequent_patterns


def main():
    # print(
    #     f"Число k-меров {test_pattern} в строке {test_text_1}: {pattern_count(test_text_1, test_pattern)}"
    # )
    # print(
    #     f"Словарь, где каждому k-меру, k={test_k_2}, сопоставлено количество его вхождений в строку {test_text_2}:\n{count_dict(test_text_2, test_k_2)}"
    # )
    # print(
    #     f"Наиболее часто встречающийся k-мер, k={test_k_3}, в строке {test_text_3}:\n{frequent_words(test_text_3, test_k_3)}"
    # )
    print(f"Для строки {text_kim_6}\n введите k < {len(text_kim_6)}, k: ")
    k_kim_6 = int(input())
    print(
        f"Наиболее часто встречающийся k-мер, k={k_kim_6}:\n{frequent_words(text_kim_6,k_kim_6)}"
    )


if __name__ == "__main__":
    main()
