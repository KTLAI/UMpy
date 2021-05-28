import json
import os
import string


def read_json(filepath):
    """Reads a JSON document, decodes the file content, and returns a list or dictionary if
    provided with a valid filepath.

    Parameters:
        filepath (str): path to file.

    Returns:
        dict/list: dictionary or list representations of the decoded JSON document.
    """

    with open(filepath, 'r', encoding='utf-8') as file_obj:
        return json.load(file_obj)


def write_json(filepath, data):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file.
        data (dict)/(list): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf-8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)


def main():
    """Entry point for program. Orchestrates workflow."""

    # abs_path = os.path.dirname(os.path.abspath(__file__))
    # print(f"\n0.0: Absolute directory path = {abs_path}")

    # CHANGE FILE NAMES
    # filepath = os.path.join(abs_path, 'input', 'swapi_planets.json')
    # filepath = './input/swapi_planets.json'
    # swapi_planets = read_json(filepath)


    # CHALLENGE 01: LIST TO DICT

    west_africa = [
        ('Benin', 'BEN'),
        ('Burkina Faso', 'BFA'),
        ('Cabo Verde', 'CPV'),
        ("Cote d'Ivoire", 'CIV'),
        ('Gambia', 'GMB'),
        ('Ghana', 'GHA'),
        ('Guinea', 'GIN'),
        ('Guinea-Bissau', 'GNB'),
        ('Liberia', 'LBR'),
        ('Mali', 'MLI'),
        ('Mauritania', 'MRT'),
        ('Niger', 'NER'),
        ('Nigeria', 'NGA'),
        ('Saint Helena', 'SHN'),
        ('Senegal', 'SEN'),
        ('Sierra Leone', 'SLE'),
        ('Togo', 'TGO')
    ]

    country_codes = {t[0]: t[1] for t in west_africa}

    print(f"\nChallenge 01: list to dict = {country_codes}")


    # CHALLENGE 02: INNER PLANETS

    planets = {
        "mercury" : {'category': 'inner', 'satellites': 0},
        "venus" : {'category': 'inner', 'satellites': 0},
        "earth" : {'category': 'inner', 'satellites': 1},
        "mars" : {'category': 'inner', 'satellites': 2},
        "jupiter" : {'category': 'outer', 'satellites': 79},
        "saturn" : {'category': 'outer', 'satellites': 82},
        "uranus" : {'category': 'outer', 'satellites': 27},
        "neptune" : {'category': 'outer', 'satellites': 14}
    }

    inner_planets = {key: val for key, val in planets.items() if val['category'] == 'inner'}

    print(f"\nChallenge 02: Inner planets = {inner_planets}")

    # CHALLENGE 03: OUTER PLANETS WITH 10-30 SATELLITES (INCLUSIVE)

    outer_planets = {
        key: val
        for key, val in planets.items()
        if val['category'] == 'outer'
        and 10 <= val['satellites'] <= 30
    }

    print(f"\nChallenge 03: Outer planets 10-30 satellites = {outer_planets}")

    # CHALLENGE 04: SATELLITE COUNTS BY PLANET CATEGORY

    # { (some_key if condition else default_key):(something_if_true if condition
    #      else something_if_false) for key, value in dict_.items() }

    satellite_counts = {'inner': 0, 'outer': 0}
    for val in planets.values():
        if val['category'] == 'inner':
            satellite_counts['inner'] += val['satellites']
        else:
            satellite_counts['outer'] += val['satellites']

    print(f"\nChallenge 03: satellite counts = {satellite_counts}")

    # list comprehension passed to sum()
    satellite_counts = {'inner': 0, 'outer': 0}
    satellite_counts['inner'] = sum(val['satellites'] for val in planets.values() if val['category'] == 'inner')
    satellite_counts['outer'] = sum(val['satellites'] for val in planets.values() if val['category'] == 'outer')

    print(f"\nChallenge 04: satellite_counts = {satellite_counts}")

    # CHALLENGE 05

    # Word Frequency
    # Amanda Gorman
    hill_we_climb = """
    When day comes we ask ourselves, where can we find light in this never-ending shade?
    The loss we carry, a sea we must wade.
    We’ve braved the belly of the beast, we’ve learned that quiet isn’t always peace and the norms and notions of what just is, isn’t always justice.
    And yet the dawn is ours before we knew it, somehow we do it, somehow we’ve weathered and witnessed a nation that isn’t broken but simply unfinished.
    We, the successors of a country and a time where a skinny black girl descended from slaves and raised by a single mother can dream of becoming president only to find herself reciting for one.
    And, yes, we are far from polished, far from pristine, but that doesn’t mean we are striving to form a union that is perfect, we are striving to forge a union with purpose, to compose a country committed to all cultures, colors, characters and conditions of man.
    So we lift our gazes not to what stands between us, but what stands before us.
    We close the divide because we know to put our future first, we must first put our differences aside.
    We lay down our arms so we can reach out our arms to one another, we seek harm to none and harmony for all.
    Let the globe, if nothing else, say this is true: that even as we grieved, we grew, even as we hurt, we hoped, that even as we tired, we tried, that we’ll forever be tied together victorious, not because we will never again know defeat but because we will never again sow division.
    """

    # Remove punctuation
    hill_we_climb = hill_we_climb.translate(str.maketrans('','', string.punctuation)) # remove punctuation

    word_counts = {}
    for word in hill_we_climb.split():
        if word not in word_counts.keys():
            word_counts[word] = 1
        else:
            word_counts[word] += 1

    # word_counts = {}
    # for word in hill_we_climb.split():
    #     word_counts[word] = word_counts.get(word, 0) + 1 # default to zero if key does not exist

    print(f"\nChallenge 05: word count loop (we) = {word_counts['we']}")

    word_counts = {word: hill_we_climb.split().count(word) for word in set(hill_we_climb.split())} # unlike a list a set is unordered and cannot include multiple occurences of the same value

    print(f"\nChallenge 05: word count comp (we) = {word_counts['we']}")




if __name__ == '__main__':
    main()