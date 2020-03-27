import hashlib


def generators(path):
    with open(path, encoding='UTF-8') as value:
        for line in value:
            strip_line = line.strip()
            byte_line = strip_line.encode()
            yield hashlib.md5(byte_line)


if __name__ == "__main__":
    for result in generators('result.json'):
        print(result.hexdigest())