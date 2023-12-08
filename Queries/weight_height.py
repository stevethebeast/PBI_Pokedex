import requests, pandas, re

r = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
resultsnames = r.json()
data = []
allnames = []
for names in resultsnames['results']:
    allnames.append(names['name'])
allnames = allnames[:15]
for weights in allnames:
    url = 'https://pokeapi.co/api/v2/pokemon/' + weights
    r = requests.get(url)
    resultsweights = r.json()
    index = re.search(r'/(\d+)/$', resultsweights['forms'][0]['url']).group(1)
    weight = resultsweights['weight']
    name = resultsweights['name']
    height = resultsweights['height']
    image = resultsweights['sprites']['other']['official-artwork']['front_default']
    data.append([index, name, weight, height, image])
HeightWeight = pandas.DataFrame(data, columns=['index', 'name', 'weight', 'height', 'image'])
print(HeightWeight)