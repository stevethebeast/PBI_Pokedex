import requests, pandas

r = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
resultsnames = r.json()
data = []
allnames = []
for names in resultsnames['results']:
    allnames.append(names['name'])
allnames = allnames[:15]
for root in allnames:
    url = 'https://pokeapi.co/api/v2/pokemon/' + root
    r = requests.get(url)
    resultsstats = r.json()
    name = resultsstats['name']
    for stats in resultsstats['stats']:
        data.append([name, stats['base_stat'], stats['stat']['name']])
Stats = pandas.DataFrame(data, columns=['name', 'amount', 'statname'])
print(Stats)