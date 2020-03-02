filename = 'article-iii.txt'

with open(filename) as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

if __name__ == "__main__":
    for idx, line in enumerate(lines):
        if line == 'True Positive!':
            print(lines[idx+3][2:-3], line)
    pass
