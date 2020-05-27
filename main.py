import json

class Countries_iterator:

    def __init__(self, file_path):
        with open(file_path, 'r') as data_json:
            self.countries_list = json.load(data_json).__iter__()
        self.wiki_info = open('wiki_info.json', 'w')
        self.wiki_info.write('[\n')


    def __iter__(self):
        return self


    def __next__(self):
        try:
            next_country = next(self.countries_list)
            country_name = next_country['name']['common']
            wiki_link = 'https://en.wikipedia.org/wiki/' + country_name.replace(' ', '_')
        except StopIteration:
            self.wiki_info.write(']')
            self.wiki_info.close()
            raise StopIteration

        country_and_wiki_link = {'name': country_name, 'link': wiki_link}
        json.dump(country_and_wiki_link, self.wiki_info, indent=2, ensure_ascii=True)
        self.wiki_info.write('\n')
        return next_country


if __name__ == '__main__':
    for country in Countries_iterator('countries.json'):
        pass