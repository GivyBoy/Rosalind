from helper_functions import read_and_format_single


def complement(string: str) -> str:
    swap = {"A": "T", "T": "A", "C": "G", "G": "C"}

    comp_str = ""
    for char in string:
        comp_str += swap[char]
    return comp_str


string = read_and_format_single("3-rosalind_revc.txt")[::-1]
comp_str = complement(string)
print(comp_str)
