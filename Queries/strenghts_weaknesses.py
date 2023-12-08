import requests, pandas

r = requests.get('https://pokeapi.co/api/v2/type')
resultstypes = r.json()
strenghts = []
weaknesses = []
alltypes = []
for names in resultstypes['results']:
    alltypes.append(names['name'])
for types in alltypes:
    url = 'https://pokeapi.co/api/v2/type/' + types
    r = requests.get(url)
    resultstypestats = r.json()
    for text in resultstypestats['damage_relations']['double_damage_from']:
        weaknesses.append([types, text['name']])
    for text in resultstypestats['damage_relations']['double_damage_to']:
        strenghts.append([types, text['name']])
    for text in resultstypestats['damage_relations']['half_damage_from']:
        strenghts.append([types, text['name']])
    for text in resultstypestats['damage_relations']['half_damage_to']:
        weaknesses.append([types, text['name']])
    for text in resultstypestats['damage_relations']['no_damage_from']:
        strenghts.append([types, text['name']])
    for text in resultstypestats['damage_relations']['no_damage_to']:
        weaknesses.append([types, text['name']])
TypeStrengths = pandas.DataFrame(strenghts, columns=['type', 'strenght']).drop_duplicates()
TypeWeaknesses = pandas.DataFrame(weaknesses, columns=['type', 'weakness']).drop_duplicates()