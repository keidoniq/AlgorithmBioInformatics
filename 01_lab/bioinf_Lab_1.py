def task_1(n: int, k: int):
    """
    Simulate rabbit population growth using a modified Fibonacci sequence.

    Args:
        n (int): The number of months to simulate.
        k (int): The reproduction rate of rabbit pairs.

    Returns:
        int: The total number of rabbit pairs after n months.
    """
    print(f"n = {n}\t k = {k}")
    prev, curr = 0, 1
    for i in range(1, n):
        curr, prev = curr + prev * k, curr
        print(f"pairs of rabbits after {i} month: {curr}")
    return curr


def task_2(s: str):
    """
    Count occurrences of each nucleotide base (A, C, G, T) in a given DNA string.

    Args:
        s (str): A DNA sequence consisting of the letters 'A', 'C', 'G', 'T'.

    Returns:
        dict: A dictionary with nucleotide bases as keys and their respective counts as values.
    """
    dict_nucleo = {nucleo_base: 0 for nucleo_base in "ACGT"}
    for s_letter in s:
        dict_nucleo[s_letter] += 1
    return dict_nucleo


def task_3(s: str, t: str):
    """
    Compute the Hamming distance - the number of positions at which the corresponding
    nucleotides differ - between two equal-length DNA sequences.

    Args:
        s (str): The first DNA sequence.
        t (str): The second DNA sequence of the same length as 's'.

    Returns:
        int: The Hamming distance between the two sequences.
    """
    dist_h = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            dist_h += 1
    return dist_h


def task_4(s: str):
    """
    Transcribe a DNA sequence into RNA by replacing all occurrences of 'T' with 'U'.

    Args:
        s (str): A DNA sequence containing the nucleotide bases 'A', 'C', 'G', 'T'.

    Returns:
        str: The corresponding RNA sequence where 'T' is replaced by 'U'.
    """
    return s.replace("T", "U")


dict_codon_to_AK = {
    "UUU": "F",
    "CUU": "L",
    "AUU": "I",
    "GUU": "V",
    "UUC": "F",
    "CUC": "L",
    "AUC": "I",
    "GUC": "V",
    "UUA": "L",
    "CUA": "L",
    "AUA": "I",
    "GUA": "V",
    "UUG": "L",
    "CUG": "L",
    "AUG": "M",
    "GUG": "V",
    "UCU": "S",
    "CCU": "P",
    "ACU": "T",
    "GCU": "A",
    "UCC": "S",
    "CCC": "P",
    "ACC": "T",
    "GCC": "A",
    "UCA": "S",
    "CCA": "P",
    "ACA": "T",
    "GCA": "A",
    "UCG": "S",
    "CCG": "P",
    "ACG": "T",
    "GCG": "A",
    "UAU": "Y",
    "CAU": "H",
    "AAU": "N",
    "GAU": "D",
    "UAC": "Y",
    "CAC": "H",
    "AAC": "N",
    "GAC": "D",
    "UAA": "Stop",
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "UAG": "Stop",
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "UGU": "C",
    "CGU": "R",
    "AGU": "S",
    "GGU": "G",
    "UGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "UGA": "Stop",
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "UGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G",
}


def task_5(s: str):
    """
    Translate an RNA sequence into a protein sequence using a codon to AK table.

    Args:
        s (str): An RNA sequence consisting of codons.

    Returns:
        t (str): The translated protein sequence.
    """
    t = ""
    AK = dict_codon_to_AK[s[0:3]]
    i = 3
    while AK != "Stop":
        t += AK
        AK = dict_codon_to_AK[s[i : (i + 3)]]
        i += 3
    return t


def main():
    task_number = int(input("Problem to solve, from 1 to 5: "))
    if task_number == 1:
        n, k = map(int, input().split())
        print(task_1(n, k))
    elif task_number == 2:
        dict_nucleotid = task_2(input())
        for n_nucl in dict_nucleotid.values():
            print(n_nucl, end=" ")
    elif task_number == 3:
        s = input()
        t = input()
        print(task_3(s, t))
    elif task_number == 4:
        print(task_4(input()))
    elif task_number == 5:
        print(task_5(input()))


if __name__ == "__main__":
    main()
