import requests, pandas, re

data = []
x = 1
while x < 10000:
    url = "https://pokeapi.co/api/v2/evolution-chain/" + str(x)
    r = requests.get(url)
    if r.status_code != 200 : break
    matches = re.findall(r'"species":\s*{\s*"name":\s*"([^"]+)"', r.text)
    matches_with_identifiers = [[f'list_{x}', len(matches) - idx + 1, name] for idx, name in enumerate(matches, start=1)]
    for el in matches_with_identifiers:
        data.append(el)
    x += 1
Evolution = pandas.DataFrame(data, columns=['evo_line', 'order', 'name'])