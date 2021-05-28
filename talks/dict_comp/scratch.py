import sw_utilities as utils


class Entity:
    """Base representation of a resource. Instantiate with name
    and resource identifier.

    Attributes:
        name: resource name
        url: resource identifier

    Methods:
        assign_values: convenience method for loading in dict data
        jsonable: return JSON-friendly dict representation of the object
    """

    KEYS = (
        'url',
        'name'
    )

    def __init__(self, name, url):
        self.name = name
        self.url = url


    def assign_values(self, data):
        """Bulk assign dictionary/map values. Iterate over object
        attributes (__dict__.keys()) and assign data values on matching
        keys using built-in setattr() function.

        Parameters:
            data (dict): key/value pairs to assign

        Returns:
            None
        """

        for key in self.__dict__.keys():
            if key in data.keys():
                setattr(self, key, data[key])


    def jsonable(self):
        """Return a JSON-friendly representation of the object.
        Use a dictionary literal rather than built-in dict() to avoid
        built-in lookup costs.

        Do not simply return self.__dict__. It can be intercepted and
        mutated, adding, modifying or removing instance attributes as a
        result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        return {'name': self.name, 'url': self.url}


    def __str__(self):
        return self.name


class Person(Entity):
    """Representation of a person.

    Attributes:
        name: person name
        url: person's resource identifier
        gender: person's gender
        birth_year: person's birth_year
        homeworld: person's home planet

    Methods:
        get_homeworld: retrieve home planet
        jsonable: return JSON-friendly dict representation of the object
    """

    KEYS = (
        'url',
        'name',
        'height',
        'mass',
        'hair_color',
        'skin_color',
        'eye_color',
        'birth_year',
        'gender',
        'homeworld',
        'species'
    )

    def __init__(self, name, url):
        super().__init__(name, url)
        self.height = None
        self.mass = None
        self.hair_color = None
        self.skin_color = None
        self.eye_color = None
        self.birth_year = None
        self.gender = None
        self.homeworld = None
        self.species = []


    def get_homeworld(self, url):
        """Retrieve SWAPI representation of home planet.
        Convert to Planet instance and assign to person.

        Parameters:
            url (str): resource identifier

        Returns:
            None
        """

        pass

        # if not isinstance(self.homeworld, Planet):
        #     data = get_swapi_resource(url)
        #     homeworld = Planet(data['name'], data['url'])
        #     homeworld.assign_values(data)
        #     self.homeworld = homeworld


    def jsonable(self):
        """Return a JSON-friendly representation of the object.
        Use a dictionary literal rather than built-in dict() to avoid
        built-in lookup costs.

        Do not simply return self.__dict__. It can be intercepted and
        mutated, adding, modifying or removing instance attributes as a
        result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        # return self.__dict__ # DANGEROUS
        # return copy.deepcopy(self.__dict__) # safe but slow

        return {
            'url': self.url,
            'name': self.name,
            'height': self.height,
            'mass': self.mass,
            'color': self.hair_color,
            'skin_color': self.skin_color,
            'eye_color': self.eye_color,
            'birth_year': self.birth_year,
            'gender': self.gender,
            'homeworld': self.homeworld,
            'species': self.species
            }


    def __str__(self):
        return self.name