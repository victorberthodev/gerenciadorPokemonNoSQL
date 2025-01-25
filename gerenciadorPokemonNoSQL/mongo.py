import json
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongo_uri = os.getenv('MONGODB_URI')
db_name = os.getenv('MONGODB_DB_NAME')

client = MongoClient(mongo_uri)
db = client[db_name]

pokemons_col = db['pokemons']
types_col = db['types']
abilities_col = db['abilities']
habitats_col = db['habitats']
evolutions_col = db['evolutions']

def insert_data(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    for pokemon in data:
        # processamento dos tipos
        type_ids = []
        for t in pokemon['types']:
            type_record = types_col.update_one({'name': t}, {'$setOnInsert': {'name': t}}, upsert=True)
            type_ids.append(type_record.upserted_id or types_col.find_one({'name': t})['_id'])

        # processamento das habilidades
        ability_ids = []
        for a in pokemon['abilities']:
            ability_record = abilities_col.update_one({'name': a}, {'$setOnInsert': {'name': a}}, upsert=True)
            ability_ids.append(ability_record.upserted_id or abilities_col.find_one({'name': a})['_id'])

        # processamento dos habitats
        habitat_record = habitats_col.update_one({'name': pokemon['habitat']}, {'$setOnInsert': {'name': pokemon['habitat']}}, upsert=True)
        habitat_id = habitat_record.upserted_id or habitats_col.find_one({'name': pokemon['habitat']})['_id']

        # pocessamento das evoluções
        evolution_ids = []
        for e in pokemon['evolutions']:
            evolution_record = evolutions_col.update_one({'pokemonOrigin': pokemon['ID'], 'pokemonEvolution': e['id']}, {'$setOnInsert': {'pokemonOrigin': pokemon['ID'], 'pokemonEvolution': e['id']}}, upsert=True)
            evolution_ids.append(evolution_record.upserted_id or evolutions_col.find_one({'pokemonOrigin': pokemon['ID'], 'pokemonEvolution': e['id']})['_id'])

        # insere o pokemon já pegando o ID gerado das outras coisas (tipos/habitats/evolutions/habilidades)
        pokemon_record = {
            'ID': pokemon['ID'],
            'name': pokemon['name'],
            'weight': pokemon['weight'],
            'height': pokemon['height'],
            'pictures': pokemon['pictures'],
            'description': pokemon['description'],
            'types': type_ids,
            'abilities': ability_ids,
            'habitat': habitat_id,
            'evolutions': evolution_ids
        }

        pokemons_col.update_one({'ID': pokemon['ID']}, {'$set': pokemon_record}, upsert=True)

insert_data('lista_pokemon.json')
