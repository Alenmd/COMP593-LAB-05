'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
    print(poke_info)

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # TODO: Clean the Pokemon name parameter
    pokemon_name = pokemon_name.lower().strip()
    # TODO: Build a clean URL and use it to send a GET request
    url = POKE_API_URL + pokemon_name 
    # TODO: If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    resp_msg = requests.get(url)
    if resp_msg.status_code == requests.codes.ok:
        print(f'Getting information for{pokemon_name}... success')
        print(f'Posting new paste to PasteBin.... success')
        return resp_msg.json()  # Convert the JSON-formatted message body text to a dictionary and return it
    else:
        print(f"Getting information for {pokemon_name}... failure")
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
        return None         #If the GET request failed, print the error reason and return None

if __name__ == '__main__':
    main()