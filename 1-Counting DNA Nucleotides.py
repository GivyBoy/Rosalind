from helper_functions import read_and_format_single


def count_chars(word: str) -> list[tuple[str, int]]:

    count = {}

    for i in word:
        count[i] = 1 + count.get(i, 0)

    counts = [(key, val) for key, val in count.items()]

    return counts


output = read_and_format_single("1-rosalind_dna2.txt")
counts = count_chars(output)
print(counts)


