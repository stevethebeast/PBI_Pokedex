import requests, pandas

r = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
resultsnames = r.json()
data = []
allnames = []
for names in resultsnames['results']:
    allnames.append(names['name'])
allnames = allnames[:15]
for species in allnames:
    url = 'https://pokeapi.co/api/v2/pokemon-species/' + species
    r = requests.get(url)
    resultsspecies = r.json()
    for text in resultsspecies['flavor_text_entries']:
        data.append([species, text['flavor_text'], text['version']['name'], text['language']['name']])
Description = pandas.DataFrame(data, columns=['name', 'description', 'version', 'language'])
print(Description)