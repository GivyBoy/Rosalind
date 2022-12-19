def read_and_format_single(name: str) -> str:

    with open(name) as f:
        strings = f.readlines()

    updt_str = ""
    for string in strings:
        updt_str += string.replace("\n", "")

    return updt_str


def read_and_format_multi(name: str) -> list[str]:

    with open(name) as f:
        strings = f.readlines()

    updt_str = []
    for string in strings:
        updt_str.append(string.replace("\n", ""))

    return updt_str


if __name__ == "__main__":
    print(read_and_format_single("1-rosalind_dna2.txt"))
