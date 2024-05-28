import json


# Function to search for city adcode with precise and fuzzy matching
def search_city_adcode(city_name):
    # Load the JSON data from the file we saved earlier
    with open('./AMap_adcode_citycode.json', 'r', encoding='utf-8') as file:
        city_data = json.load(file)
    # Precise matching
    precise_matches = [entry for entry in city_data if entry['中文名'] == city_name]
    if precise_matches:
        return precise_matches[0]['adcode']

    # Fuzzy matching
    fuzzy_matches = [entry for entry in city_data if city_name in entry['中文名']]
    # Limit to top 6 closest matches based on the length of the city name in the entries
    fuzzy_matches_sorted = sorted(fuzzy_matches, key=lambda x: abs(len(x['中文名']) - len(city_name)))
    top_fuzzy_matches = fuzzy_matches_sorted[:6]

    return {entry['中文名']: entry['adcode'] for entry in top_fuzzy_matches}


# Example usage of the function
print(search_city_adcode("北京"))  # Should return precise match
print(search_city_adcode("城"))  # Should return fuzzy matches with a limit of 6
