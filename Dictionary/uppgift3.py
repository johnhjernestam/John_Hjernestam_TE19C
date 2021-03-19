pokemon_lista = {}

def readFile():
    returnablepokemon_lista = {}
    with open("pokemonlista.txt", "r") as pokemonList:
        for line in pokemonList:
            splittedLines = line.split()
            returnablepokemon_lista[splittedLines[1]] = 'Typ: '+splittedLines[2]+', Index:'+splittedLines[0]

    return returnablepokemon_lista

pokemon_lista = readFile()

print(pokemon_lista['Gastly'])