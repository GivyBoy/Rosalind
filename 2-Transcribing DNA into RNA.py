from helper_functions import read_and_format_single


def find_replace(string: str) -> str:
    new_str = ""
    for char in string:

        if char == "T":
            new_str += "U"
        else:
            new_str += char
    return new_str


string = read_and_format_single("2-rosalind_rna2.txt")
new_str = find_replace(string)
print(new_str)
