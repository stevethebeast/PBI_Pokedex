import requests, pandas

r = requests.get('https://pokeapi.co/api/v2/type')
resultstypes = r.json()
data_double_damage_from = []
data_double_damage_to = []
data_half_damage_from = []
data_half_damage_to = []
data_no_damage_from = []
data_no_damage_to = []
alltypes = []
for names in resultstypes['results']:
    alltypes.append(names['name'])
for types in alltypes:
    url = 'https://pokeapi.co/api/v2/type/' + types
    r = requests.get(url)
    resultstypestats = r.json()
    for text in resultstypestats['damage_relations']['double_damage_from']:
        data_double_damage_from.append([types, text['name']])
    for text in resultstypestats['damage_relations']['double_damage_to']:
        data_double_damage_to.append([types, text['name']])
    for text in resultstypestats['damage_relations']['half_damage_from']:
        data_half_damage_from.append([types, text['name']])
    for text in resultstypestats['damage_relations']['half_damage_to']:
        data_half_damage_to.append([types, text['name']])
    for text in resultstypestats['damage_relations']['no_damage_from']:
        data_no_damage_from.append([types, text['name']])
    for text in resultstypestats['damage_relations']['no_damage_to']:
        data_no_damage_to.append([types, text['name']])
Data_double_damage_from = pandas.DataFrame(data_double_damage_from, columns=['type', 'double_damage_from'])
Data_double_damage_to = pandas.DataFrame(data_double_damage_to, columns=['type', 'double_damage_to'])
Data_half_damage_from = pandas.DataFrame(data_half_damage_from, columns=['type', 'half_damage_from'])
Data_half_damage_to = pandas.DataFrame(data_half_damage_to, columns=['type', 'half_damage_to'])
Data_no_damage_from = pandas.DataFrame(data_no_damage_from, columns=['type', 'no_damage_from'])
Data_no_damage_to = pandas.DataFrame(data_no_damage_to, columns=['type', 'no_damage_to'])