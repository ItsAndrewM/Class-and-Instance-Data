import doctest
from pet import Pet
from date import Date

# represents a pet as (name, species)
PetNameSpecies = tuple[str,str]

# columns of values within input file row and within PetNameSpecies tuple
NAME    = 0
SPECIES = 1
MONTH   = 2
DAY     = 3
YEAR    = 4

def read_file(filename: str) -> list[Pet]:
    ''' returns a list of Pets populated with data from filename
    
    Preconditions: filename exists.
    If filename is not empty, each row has a single Pet's information
    separated by commas with expected values at columns:
    NAME, SPECIES, MONTH, DAY and YEAR.

    >>> read_file('empty.csv')
    []
    >>> read_file('pet_data.csv')
    [Pet('Rover', 'Dog', Date(12, 31, 2010)), Pet('Red', 'Cat', Date(9, 15, 2016)), Pet('Chewie', 'Hamster', Date(1, 23, 2009)), Pet('Sam', 'Budgie', Date(3, 29, 1990)), Pet('Ollie', 'Dog', Date(2, 8, 2009)), Pet('Scout', 'Dog', Date(9, 15, 2016))]
    '''
    # TODO: complete this function
    list_of_pets = []
    
    file_handle = open(filename, 'r')  
  
    for line in file_handle:
        
        line = line.strip()
        list_of_str = line.split(',')
        if list_of_str == ['']:
            return list_of_pets
        else:
            pet_name = list_of_str[NAME]
            pet_species = list_of_str[SPECIES] 
            pet_birthdate = Date(int(list_of_str[MONTH]), int(list_of_str[DAY]), int(list_of_str[YEAR]))
            pet = Pet(pet_name, pet_species, pet_birthdate)
            list_of_pets.append(pet)           
        
    file_handle.close()
    
    return list_of_pets    

def find_pet(lopets: list[Pet], name: str) -> int:
    ''' returns the position of pet with given name in lopets
    Returns -1 if name not found
    Returns the position of the first found if there >1 Pet with the given name
    
    Precondition: name must match case exactly
    ie. 'rover' does not match 'Rover'

    >>> find_pet([], 'Fred')
    -1
    >>> find_pet([Pet('Rover', 'Dog', Date(12, 22, 2020)), Pet('Red', 'Cat', Date(1, 2, 2019))], 'Red')
    1
    >>> find_pet([Pet('Rover', 'Dog', Date(12, 22, 2020)), Pet('Red', 'Cat', Date(1, 2, 2019))], 'Bowser')
    -1
    >>> find_pet([Pet('Red', 'Dog', Date(12, 22, 2020)), Pet('Red', 'Cat', Date(1, 2, 2019))], 'Red')
    0
    '''
    # TODO: complete this function
    if lopets == []:
        return -1
    for pet in lopets:
        pet_name = pet.get_name()
        if pet_name == name:
            index_of_name = lopets.index(pet)
            return index_of_name
    else:
        return -1


def get_all_of_species(lopets: list[Pet], species: str) -> list[Pet]:
    ''' returns a list of all pets of the given species.
    Result list is not necessarily unique, if >1 Pet in lopets has the same name.
    
    Precondition: species must match case exactly
    ie. 'dog' does not match 'Dog'
    
    >>> pets = [Pet('Rover', 'Dog', Date(12, 31, 2010)), Pet('Red', 'Cat', Date(9, 15, 2016)), Pet('Chewie', 'Hamster', Date(1, 23, 2009)), Pet('Sam', 'Budgie', Date(3, 29, 1990)), Pet('Ollie', 'Dog', Date(2, 8, 2009)), Pet('Scout', 'Dog', Date(9, 15, 2016))]

    >>> get_all_of_species([], 'Dog')
    []
    >>> get_all_of_species(pets, 'Dog')
    [Pet('Rover', 'Dog', Date(12, 31, 2010)), Pet('Ollie', 'Dog', Date(2, 8, 2009)), Pet('Scout', 'Dog', Date(9, 15, 2016))]
    >>> get_all_of_species(pets, 'Tiger')
    []
    >>> get_all_of_species(pets, 'Hamster')
    [Pet('Chewie', 'Hamster', Date(1, 23, 2009))]
    '''
    # TODO: complete this function
    list_of_pet_species = []
    
    if lopets == []:
        return list_of_pet_species
    else:
        for pet in lopets:
            pet_species = pet.get_species()
            if pet_species == species:
                list_of_pet_species.append(pet)
        return list_of_pet_species

def get_latest_birthdate(lopets: list[Pet]) -> Date:
    ''' returns the latest Date of all birthdates of Pet instances in lopets
    Precondition: lopets is not empty
    >>> pets = [Pet('Rover', 'Dog', Date(12, 31, 2010)), Pet('Red', 'Cat', Date(9, 15, 2016)), Pet('Chewie', 'Hamster', Date(1, 23, 2009)), Pet('Sam', 'Budgie', Date(3, 29, 1990)), Pet('Ollie', 'Dog', Date(2, 8, 2009)), Pet('Scout', 'Dog', Date(9, 15, 2016))]

    >>> get_latest_birthdate([Pet('Rover', 'Dog', Date(12, 31, 2010))])
    Date(12, 31, 2010)
    >>> get_latest_birthdate(pets)
    Date(9, 15, 2016)
    '''
    # TODO: complete this function
    latest_birthdate = lopets[0].get_birthdate()

    for pet in lopets:
        pet_birthdate = pet.get_birthdate()
        if latest_birthdate.is_after(pet_birthdate) == False:
            latest_birthdate = pet_birthdate

    return latest_birthdate
   



def get_youngest_pets(lopets: list[Pet]) -> list[PetNameSpecies]:
    ''' returns a list of PetNameSpecies of all the youngest pets in lopets
    >>> pets = [Pet('Rover', 'Dog', Date(12, 31, 2010)), Pet('Red', 'Cat', Date(9, 15, 2016)), Pet('Chewie', 'Hamster', Date(1, 23, 2009)), Pet('Sam', 'Budgie', Date(3, 29, 1990)), Pet('Ollie', 'Dog', Date(2, 8, 2009)), Pet('Scout', 'Dog', Date(9, 15, 2016))]
    >>> get_youngest_pets([])
    []
    >>> get_youngest_pets(pets)
    [('Red', 'Cat'), ('Scout', 'Dog')]
    '''
    # TODO: complete this function
    
    
    list_of_youngest_pets = []

    if lopets == []:
        return list_of_youngest_pets
    else:
        latest_birthdate = get_latest_birthdate(lopets)
        for pet in lopets:
            pet_birthdate = pet.get_birthdate()
            pet_name = pet.get_name()
            pet_species = pet.get_species()
            if pet_birthdate == latest_birthdate:
                PetNameSpecies = (pet_name, pet_species)
                list_of_youngest_pets.append(PetNameSpecies)
                
        return list_of_youngest_pets
        