import sys

def count_lines(file):
    with open(file) as f:
        return (len(f.readlines()))


if __name__ == "__main__":
    file = sys.argv[1]
    num_lines = count_lines(file)
    print(f"There are {num_lines} lines in {file}")