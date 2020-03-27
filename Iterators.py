import json


class Countries:

    def __init__(self, path):
        self.path = path
        self.number = -1
        self.read = open(self.path, encoding= 'UTF-8')
        self.data = json.load(self.read)
        self.file_write = open('result.json', 'w', encoding='UTF-8')

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.number += 1
            country = self.data[self.number]['name']['common']
            replace_country = country.replace(' ', '_')
            link = 'https://wikipedia.org/wiki/' + replace_country
            self.file_write.write(f'{country} - https://wikipedia.org/wiki/{replace_country}\n')
        except IndexError:
            raise StopIteration
        return link

if __name__ == "__main__":
    for link in Countries('countries.json'):
        print(link)