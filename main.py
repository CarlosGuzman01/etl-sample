import pandas as pd
import requests

# 1- Extract Data from API Call
def fetch_pokemon_data(pokemon_names):
    pokemon_data = []
    for name in pokemon_names:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
        
        if response.status_code == 200:
            data = response.json()
            pokemon_data.append(data)
        else:
            print(f"Failed to fetch data for {name}")
    return pokemon_data


# 2- Transform Data
def transform_pokemon_data(pokemon_data):
    transformed_data = []

    for data in pokemon_data:
        transformed_data.append({})

        transformed_data[-1]["Name"] = data["name"]
        transformed_data[-1]["ID"] = data["id"]
        transformed_data[-1]["Height (m)"] = data["height"]
        transformed_data[-1]["Weight (kg)"] = data["weight"]

        types_list = []

        for t in data["types"]:
            types_list.append(t["type"]["name"])

        transformed_data[-1]["Types"] = ", ".join(types_list)
    
    
    return pd.DataFrame(transformed_data)


# 3- Load Data to CSV file
def save_to_csv(df, filename):
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")


pokemon_names = [
    "bulbasaur", "ivysaur", "venusaur", "charmander", "charmeleon", "charizard",
    "squirtle", "wartortle", "blastoise", "caterpie", "metapod", "butterfree",
    "weedle", "kakuna", "beedrill", "pidgey", "pidgeotto", "pidgeot", "rattata", "raticate",
    "spearow", "fearow", "ekans", "arbok", "pikachu", "raichu", "sandshrew", "sandslash",
    "nidorina", "nidoqueen", "nidorino", "nidoking", "clefairy", "clefable", "vulpix", "ninetales",
    "zubat", "golbat", "oddish", "gloom", "vileplume", "paras", "parasect", "venonat", "venomoth",
    "diglett", "dugtrio", "meowth", "persian", "psyduck", "golduck", "machop", "machoke", "machamp",
    "bellsprout", "weepinbell", "victreebel", "tentacool", "tentacruel", "geodude", "graveler", "golem",
    "ponyta", "rapidash", "magnemite", "magneton", "doduo", "dodrio", "seel", "dewgong", "grimer", "muk",
    "shellder", "cloyster", "gastly", "haunter", "gengar", "onix", "steelix", "drowzee", "hypno", "krabby",
    "kingler", "exeggcute", "exeggutor", "cubone", "marowak", "lickitung", "lickilicky", "koffing", "weezing",
    "rhyhorn", "rhydon", "chansey", "blissey", "tangela", "tangrowth", "kangaskhan", "horsea", "seadra",
    "goldeen", "seaking", "staryu", "starmie", "scyther", "jynx", "electabuzz", "magmar", "pinsir", "tauros",
    "magikarp", "gyarados", "lapras", "ditto", "eevee", "vaporeon", "jolteon", "flareon", "espeon", "umbreon",
    "leafeon", "glaceon", "sylveon", "munchlax", "shinx", "luxio", "luxray", "budew", "roselia", "roserade",
    "cranidos", "rampardos", "shuckle", "sableye", "aron", "lairon", "aggron", "meditite", "medicham", "swablu",
    "altaria", "zorua", "zoroark", "minccino", "cinccino", "audino", "timburr", "gurdurr", "conkeldurr", "tympole",
    "politoed", "venipede", "whirlipede", "scolipede", "cottonee", "whimsicott", "petilil", "lilligant", "sandile",
    "krokorok", "krookodile", "darumaka", "maractus", "dwebble", "crustle", "scraggy", "scrafty", "sigilyph", "yamask",
    "cofagrigus", "solosis", "duosion", "reuniclus", "gothita", "gothorita", "gothitelle", "lunala", "yveltal",
    "diancie", "hoopa", "volcanion", "rowlet", "dartrix", "decidueye", "litten", "torracat", "incineroar", "popplio",
    "brionne", "primarina", "pikipek", "trumbeak", "toucannon", "yungoos", "gumshoos", "grubbin", "charjabug", "vikavolt",
    "crabrawler", "crabominable", "cutiefly", "ribombee", "rockruff", "swablu", "fomantis", "lurantis", "sandygast",
    "palossand", "silicobra", "sandaconda", "cufant", "copperajah", "impidimp", "morgrem", "grimmsnarl", "milcery",
    "alcremie", "phantump", "trevenant", "bounsweet", "steenee", "tsareena", "swirlix", "slurpuff", "sprigatito",
    "floragato", "meowscarada", "fuecoco", "crocalor", "skeledirge", "quaxly", "quaxwell", "quaquaval"
]


#Exract
raw_data = fetch_pokemon_data(pokemon_names)

#Transform
cleaned_data = transform_pokemon_data(raw_data)

#Load
save_to_csv(cleaned_data, "pokemon_data.csv")







