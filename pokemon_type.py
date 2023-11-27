import requests, pandas

r = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
resultsnames = r.json()
data = []
allnames = []
for names in resultsnames['results']:
    allnames.append(names['name'])
allnames = allnames[:15]
for name in allnames:
    url = 'https://pokeapi.co/api/v2/pokemon/' + name
    r = requests.get(url)
    resultstypes = r.json()
    for types in resultstypes['types']:
        data.append([name, types['type']['name']])
PokeTypes = pandas.DataFrame(data, columns=['name', 'type'])
print(PokeTypes)