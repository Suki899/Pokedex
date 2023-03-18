import csv

# Import pokemon data from csv file into a list of dictionaries
pokemon_data = []
with open('pokemon.csv', newline='') as f:
    reader = csv.DictReader(f)
    for line in reader:
        pokemon_data.append(line)

# Function to format a single line of pokemon data for printing
def format_pokemon_line(pokemon):
    print("{:<3} {:<30} {:<12} {:<12}{:<8} {:<8} {:<8} {:<8}{:<8} {:<8} {:<8} {:<12}{:<8}".format(pokemon['No'], pokemon['Name'], pokemon["Type 1"], pokemon['Type 2'], pokemon['Total'], pokemon["HP"], pokemon["Attack"], pokemon['Defense'], pokemon["Sp.Atk"], pokemon["Sp.Def"], pokemon["Speed"], pokemon["Generation"], pokemon["Legendary"]))

# Function to search for Pokemon based on given requirements and print matching results
def search_pokemon(list_of_requirements, allow_multiple_results):
    pokemon_shown = 0
    # Create a copy of the original list of requirements to avoid modifying it
    updated_requirements = [list(r) for r in list_of_requirements] 
    # Ask for user input for requirements that are not "given"
    for requirements in updated_requirements:
        if requirements[1] != "given":
            requirements.append(input(f"Enter the {requirements[1]} {requirements[0]}:"))
    for pokemon in pokemon_data:
        # Initialize a counter for the number of requirements that the Pokemon meets
        checks = 0
        # Loop over each search requirement in the list
        for requirement in updated_requirements:
            if requirement[1] == "given" and pokemon[requirement[0]].lower() == requirement[2].lower():
              checks += 1
            elif requirement[1] == "exact" and pokemon[requirement[0]].lower() == requirement[2].lower():
                checks += 1
            elif requirement[1] == "minimum" and int(pokemon[requirement[0]]) >= int(requirement[2]):
                checks += 1
            elif requirement[1] == "maximum" and int(pokemon[requirement[0]]) <= int(requirement[2]):
                checks +=1
        if checks == len(list_of_requirements):
            format_pokemon_line(pokemon)
            pokemon_shown += 1
            if not allow_multiple_results:
              break
    if pokemon_shown == 0: print("No matching Pokemon found")
    elif pokemon_shown == 1:
      if not allow_multiple_results: print("Here is the first matching Pokemon")
      else: print("1 Pokemon matches the given criteria")
    else: print(f"{pokemon_shown} Pokemons match the given criteria")

# Function to display the first Pokemon of a specific type entered by the user
def display_first_pokemon_of_type():
    type_to_look_for = input("Enter type to look for:").lower()
    exists = False
    for pokemon in pokemon_data:
        if type_to_look_for == pokemon['Type 1'].lower() or type_to_look_for == pokemon['Type 2'].lower():
            format_pokemon_line(pokemon)
            exists = True
            break
    if not exists: print("No Pokemon of that type found. Please try again.")

# Main menu loop
quit_program = False
while not quit_program:
  print("\nPokemon Super Search Engine\n1. Display Pokemon with their types and statistics\n2. Display the first Pokemon of a Type of your Choice\n3. Display all Pokemons with Total Base stat of your choice\n4. Display all Pokemons with a minimum set of stats\n5. Display all legendary Pokemons of specific Type1 and Type2\n0. Quit\n")
  
  selected_option = input()
  if selected_option == '1':
    search_pokemon([], True)
  if selected_option == '2':
    display_first_pokemon_of_type()
  if selected_option == '3':
    search_pokemon([["Total", "minimum"]], True)
  if selected_option == '4':
    search_pokemon([["Sp.Atk", "minimum"], ["Sp.Def", "minimum"], ["Speed","minimum"]], True)
  if selected_option == '5':
    search_pokemon([["Legendary", "given", "TRUE"], ["Type 1", "exact"], ["Type 2","exact"]], True)
  if selected_option == '0':
    quit_program = True