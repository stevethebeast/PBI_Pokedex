
# PBI_Pokedex
A simple Pokédex in PowerBI using data from https://pokeapi.co/

## General aspect

This PowerBI Pokédex has a header with three filters on Name, Language and Version, a panel with the Pokémon number, name and image on the left and four tabs activated by buttons. These tabs are:

 1. About: contains the description, height, weight, the types and strenghts and weaknesses.
 2. Basic Stats: the selected Pokémon's hp, attack, defense and speed compared to the max stats of all Pokémons.
 3. Special Stats: the selected Pokémon's special-attack and special-defense compared to the max stats of all Pokémons.
 4. Evolution: a table containing the whole evolution chain of the selected Pokémon.

There are three filters at the top of the Pokédex:

 1. Searching by Pokémon name
 2. Language
 3. Pokémon version

The number, name and image of the selected Pokémon will always appear on the left pane.

### About

![image](https://github.com/stevethebeast/PBI_Pokedex/assets/126287020/7c9a36f3-2751-4be6-bd5a-3be7e57ad845)

This pane shows basic information about the selected Pokémon

### Basic Stats
![image](https://github.com/stevethebeast/PBI_Pokedex/assets/126287020/08092f96-3938-4b93-9524-ca8aea176cbc)

This pane shows graphs comparing basic stats to the corresponding MAX of all Pokémons.
### Special Stats
![image](https://github.com/stevethebeast/PBI_Pokedex/assets/126287020/b48ecefa-e352-4f1d-b6bb-8ddfc66866f2)

This pane shows graphs comparing special stats to the corresponding MAX of all Pokémons
### Evolution
![image](https://github.com/stevethebeast/PBI_Pokedex/assets/126287020/d3ccad01-6abe-42d0-a5e9-195db11447e7)

This pane shows a table displaying the evolutionary chain of the selected Pokémon
## Data
The data is sourced from the API available at [https://pokeapi.co/](https://pokeapi.co/). Each endpoint provides a distinct set of data, and a Python DataFrame is generated for each of these sets. Subsequently, all the data is combined within PowerBI's Data Model. For each table, a single request is made per Pokémon. Consequently, we had to retrieve the names for each Pokémon, followed by looping through each entry in the resulting array. The queries are located in the "Queries" folder.
### Model
![image](https://github.com/stevethebeast/PBI_Pokedex/assets/126287020/208bbdda-7903-4554-be20-244128e815ee)

### Indicators
Six indicators are computed: MAX_attack, MAX_defense, MAX_hp, MAX_special_attack, MAX_special_defense, and MAX_speed. Each of these indicators is derived from the corresponding Stat, utilizing the "statname" filter, as illustrated in this example:

```DAX
MAX_attack = CALCULATE(MAX(Stats[amount]), FILTER(Stats, [statname] = "attack"))
```
