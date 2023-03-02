# Practice modifying object attributes and calling methods

from prettytable import PrettyTable

table = PrettyTable()

#List containing the pokemons
pokemons = ['Pikachu', 'Squirtle', 'Charmander']

#List containing the pokemon types
types = ['Electric', 'Water', 'Fire']

table.add_column('Pokemon Name', pokemons) 
table.add_column('Type', types) 

#Left align
table.align = 'l'

print(table)