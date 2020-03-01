filename = 'article-iii.txt'

with open(filename) as f:
    content = f.readlines()

content = [x.strip() for x in content]

if __name__ == "__main__":
    print(content)
    pass
